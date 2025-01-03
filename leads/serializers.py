from rest_framework import serializers

from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'location',
            'gender',
            'created_at',
        )