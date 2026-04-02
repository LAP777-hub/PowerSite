from django.contrib.auth.models import User
from django.db import models


class IssueReport(models.Model):
    ISSUE_TYPES = [
        ('power_outage', 'Power Outage'),
        ('loadshedding', 'Loadshedding'),
        ('cable_theft', 'Cable Theft'),
        ('damaged_cable', 'Damaged Cable'),
        ('transformer', 'Transformer Fault'),
        ('meter', 'Faulty Meter'),
        ('trip_switch', 'Main Switch Tripping'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
    ('received', 'Received'),
    ('pending', 'Pending'),
    ('under_review', 'Under Review'),
    ('assigned', 'Assigned'),
    ('in_progress', 'In Progress'),
    ('awaiting_materials', 'Awaiting Materials'),
    ('resolved', 'Resolved'),
    ('incomplete', 'Incomplete'),
]
    

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_reports'
    )
    title = models.CharField(max_length=120)
    issue_type = models.CharField(max_length=30, choices=ISSUE_TYPES)
    description = models.TextField()
    area_name = models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    image = models.ImageField(upload_to='reports/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    report = models.ForeignKey(IssueReport, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.message}"