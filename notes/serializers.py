from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    lead = serializers.SerializerMethodField()
    class Meta:
        model = Note
        fields = (
            'id',
            'lead',
            'title',
            'content',
            'created_at',
        )
            
    def get_lead(self, obj):
        
        return obj.get_lead_display()