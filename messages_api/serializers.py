from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User

class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.CharField(source="sender.username")
    receiver = serializers.CharField(source="receiver.username")
    
    class Meta:
        model = Message
        fields = ["id","sender", "receiver", "subject", "message", "creation_date", "is_readed"]

    
    def validate(self, data):
        sender = data['sender']
        receiver = data['receiver']
        if sender == receiver:
            raise serializers.ValidationError({'Sender':'Cannot send message to yourself'})
        return data
        
    def create(self, validated_data):
        validated_data['sender'] = User.objects.get(id = validated_data['sender']['username'])
        validated_data['receiver'] = User.objects.get(id = validated_data['receiver']['username'])
        #raise serializers.ValidationError({'Sender':validated_data})
        message = Message.objects.create(**validated_data)
        return message;
