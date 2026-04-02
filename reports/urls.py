from django.urls import path
from . import views

urlpatterns = [
    path('manage-reports/', views.manage_reports, name='manage_reports'),
    path('', views.dashboard, name='dashboard'),
    path('report/', views.report_issue, name='report_issue'),
    path('my-reports/', views.my_reports, name='my_reports'),
    path('track/<int:report_id>/', views.track_issue, name='track_issue'),
    path('delete/<int:report_id>/', views.delete_report, name='delete_report'),

    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications/read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/status/<int:report_id>/<str:new_status>/', views.admin_update_status, name='admin_update_status'),
    path('admin-dashboard/assign/<int:report_id>/', views.admin_assign_technician, name='admin_assign_technician'),
    path('admin-dashboard/delete/<int:report_id>/', views.admin_delete_report, name='admin_delete_report'),

    path('technician-dashboard/', views.technician_dashboard, name='technician_dashboard'),
    path('technician-dashboard/status/<int:report_id>/<str:new_status>/', views.technician_update_status, name='technician_update_status'),
]