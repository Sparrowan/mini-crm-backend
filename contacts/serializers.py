from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    lead = serializers.SerializerMethodField()
    class Meta:
        model = Contact
        fields = (
            'id',
            'lead',
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'email',
            'created_at',
        )
            
    def get_lead(self, obj):       
        return obj.get_lead_display()