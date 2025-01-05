from rest_framework import serializers

from .models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    lead = serializers.SerializerMethodField()
    class Meta:
        model = Reminder
        fields = (
            'id',
            'lead',
            'title',
            'message',
            'status',
            'created_at',
        )
            
    def get_lead(self, obj):
        return obj.get_lead_display()