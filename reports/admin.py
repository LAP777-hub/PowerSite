from django.contrib import admin
from .models import IssueReport, Notification


@admin.register(IssueReport)
class IssueReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue_type', 'area_name', 'status', 'user', 'assigned_to', 'created_at')
    list_filter = ('status', 'issue_type', 'created_at')
    search_fields = ('title', 'description', 'area_name', 'user__username', 'assigned_to__username')
    list_editable = ('status', 'assigned_to')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')