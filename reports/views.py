from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .forms import IssueReportForm
from .models import IssueReport, Notification


def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)


def technician_required(view_func):
    return user_passes_test(lambda u: u.is_staff and not u.is_superuser)(view_func)


@login_required
def manage_reports(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    if request.user.is_staff:
        return redirect('technician_dashboard')
    messages.error(request, 'You do not have permission to access Manage Reports.')
    return redirect('dashboard')


def create_notification(user, report, message):
    Notification.objects.create(user=user, report=report, message=message)


@login_required
def dashboard(request):
    latest_reports = IssueReport.objects.filter(user=request.user).order_by('-created_at')[:5]
    active_reports = IssueReport.objects.exclude(status='resolved').order_by('-updated_at')[:5]
    map_reports = IssueReport.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)

    context = {
        'latest_reports': latest_reports,
        'active_reports': active_reports,
        'map_reports': map_reports,
    }
    return render(request, 'reports/dashboard.html', context)


@login_required
def report_issue(request):
    if request.method == 'POST':
        form = IssueReportForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()
            create_notification(request.user, issue, f'Your report "{issue.title}" was submitted successfully.')
            messages.success(request, 'Issue submitted successfully. You can now track it.')
            return redirect('track_issue', report_id=issue.id)
    else:
        form = IssueReportForm()

    return render(request, 'reports/report_issue.html', {'form': form})


@login_required
def my_reports(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    issue_type_filter = request.GET.get('type', '')

    reports = IssueReport.objects.filter(user=request.user).order_by('-created_at')

    if query:
        reports = reports.filter(title__icontains=query)

    if status_filter:
        reports = reports.filter(status=status_filter)

    if issue_type_filter:
        reports = reports.filter(issue_type=issue_type_filter)

    context = {
        'reports': reports,
        'query': query,
        'status_filter': status_filter,
        'issue_type_filter': issue_type_filter,
        'status_choices': IssueReport.STATUS_CHOICES,
        'issue_type_choices': IssueReport.ISSUE_TYPES,
    }
    return render(request, 'reports/my_reports.html', context)


@login_required
def track_issue(request, report_id):
    if request.user.is_superuser:
        report = get_object_or_404(IssueReport, id=report_id)
    elif request.user.is_staff:
        report = get_object_or_404(IssueReport, id=report_id, assigned_to=request.user)
    else:
        report = get_object_or_404(IssueReport, id=report_id, user=request.user)

    return render(request, 'reports/track_issue.html', {'report': report})


@login_required
def delete_report(request, report_id):
    report = get_object_or_404(IssueReport, id=report_id, user=request.user)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'Report deleted successfully.')
    return redirect('my_reports')


@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'reports/notifications.html', {'notifications': notifications})


@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications')


@admin_required
def admin_dashboard(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    issue_type_filter = request.GET.get('type', '')

    reports = IssueReport.objects.all().order_by('-created_at')
    technicians = User.objects.filter(is_staff=True, is_superuser=False)

    if query:
        reports = reports.filter(title__icontains=query)

    if status_filter:
        reports = reports.filter(status=status_filter)

    if issue_type_filter:
        reports = reports.filter(issue_type=issue_type_filter)

    context = {
        'reports': reports,
        'technicians': technicians,
        'query': query,
        'status_filter': status_filter,
        'issue_type_filter': issue_type_filter,
        'status_choices': IssueReport.STATUS_CHOICES,
        'issue_type_choices': IssueReport.ISSUE_TYPES,
    }
    return render(request, 'reports/admin_dashboard.html', context)


@admin_required
def admin_update_status(request, report_id, new_status):
    report = get_object_or_404(IssueReport, id=report_id)

    allowed_statuses = [
        'received',
        'under_review',
        'assigned',
        'in_progress',
        'resolved',
        'incomplete',
    ]

    if new_status in allowed_statuses:
        report.status = new_status
        report.save()
        create_notification(report.user, report, f'Your report "{report.title}" status changed to {report.get_status_display()}.')
        if report.assigned_to:
            create_notification(report.assigned_to, report, f'Assigned report "{report.title}" is now {report.get_status_display()}.')
        messages.success(request, f'Report status updated to {report.get_status_display()}.')

    return redirect('admin_dashboard')


@admin_required
def admin_assign_technician(request, report_id):
    report = get_object_or_404(IssueReport, id=report_id)

    if request.method == 'POST':
        technician_id = request.POST.get('technician_id')
        technician = get_object_or_404(User, id=technician_id, is_staff=True, is_superuser=False)

        report.assigned_to = technician
        report.status = 'assigned'
        report.save()

        create_notification(report.user, report, f'Your report "{report.title}" has been assigned to a technician.')
        create_notification(technician, report, f'You have been assigned to report "{report.title}".')

        messages.success(request, f'{technician.username} assigned successfully.')

    return redirect('admin_dashboard')


@admin_required
def admin_delete_report(request, report_id):
    report = get_object_or_404(IssueReport, id=report_id)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'Report deleted by admin.')
    return redirect('admin_dashboard')


@technician_required
def technician_dashboard(request):
    reports = IssueReport.objects.filter(assigned_to=request.user).order_by('-created_at')
    return render(request, 'reports/technician_dashboard.html', {'reports': reports})


@technician_required
def technician_update_status(request, report_id, new_status):
    report = get_object_or_404(IssueReport, id=report_id, assigned_to=request.user)

    allowed_statuses = ['in_progress', 'resolved', 'incomplete']

    if new_status in allowed_statuses:
        report.status = new_status
        report.save()
        create_notification(report.user, report, f'Your report "{report.title}" status changed to {report.get_status_display()}.')
        messages.success(request, f'Report updated to {report.get_status_display()}.')

    return redirect('technician_dashboard')