from django.db import models
from leads.models import Lead

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('processed', 'Processed')
)
# Create your models here.
class Reminder(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="reminders")
    title = models.CharField(max_length=100,)
    message = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20,default='pending')
    schedule_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return '{}'.format(self.title)
    
    def get_lead_display(self):
        return '{} {} {}'.format(self.lead.first_name, self.lead.middle_name,self.lead.last_name)