from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User

class MessageSerializer(serializers.ModelSerializer):
    '''
        A serializer that handles serialization of the Message model
    '''
    sender = serializers.CharField(source="sender.username")
    receiver = serializers.CharField(source="receiver.username")
    
    class Meta:
        model = Message
        fields = ["id","sender", "receiver", "subject", "message", "creation_date", "is_readed"]

    
    def validate(self, data):
        sender = data['sender']
        receiver = data['receiver']
        if not User.objects.filter(username=receiver['username']).exists():
            raise serializers.ValidationError({'receiver':'There is no user with username ' + receiver['username']})
        if sender == receiver:
            raise serializers.ValidationError({'sender':'Cannot send message to yourself'})
        return data
        
    def create(self, validated_data):
        validated_data['sender'] = User.objects.get(username = validated_data['sender']['username'])
        validated_data['receiver'] = User.objects.get(username = validated_data['receiver']['username'])
        message = Message.objects.create(**validated_data)
        return message;
