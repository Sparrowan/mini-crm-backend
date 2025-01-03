from django.db import models
from phone_field import PhoneField

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female')
)


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    location = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.middle_name,self.last_name)
    