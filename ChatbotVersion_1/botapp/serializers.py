from rest_framework import serializers

class chatmessage(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    class Meta:
        fields = ['message']