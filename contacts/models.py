from django.db import models
from leads.models import Lead
from phone_field import PhoneField

class Contact(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="contacts")
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
        constraints = [
            models.UniqueConstraint(fields=['lead', 'email'], name='unique_email_per_lead')
        ]
    
    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)
    
    def get_lead_display(self):
        return '{} {} {}'.format(self.lead.first_name, self.lead.middle_name, self.lead.last_name)
