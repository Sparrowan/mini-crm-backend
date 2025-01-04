from django.db import models
from leads.models import Lead

# Create your models here.
class Note(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=100,)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return '{}'.format(self.title)
    
    def get_lead_display(self):
        return '{} {} {}'.format(self.lead.first_name, self.lead.middle_name,self.lead.last_name)
