from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Message
from .serializers import MessageSerializer
from django.contrib.auth.models import User
from django.db.models import Q

class MessageListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        messages = Message.objects.filter(Q(sender = request.user.id) |Q(receiver=request.user.id))
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
    def post(self, request):

        data = {
            'subject': request.data.get('subject'), 
            'message': request.data.get('message'), 
            'receiver': User.objects.get(username=request.data.get('receiver')).id, 
            'sender': request.user.id
        }
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class NewMessageListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        messages = Message.objects.filter(receiver = request.user.id).filter(is_readed=False)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, message_id, user_id):
        #Helper method to get the object with given message_id, and user_id 
        try:
            message = Message.objects.get(Q(id=message_id) & 
                        (Q(sender = user_id) | Q(receiver=user_id)))
            message.is_readed = True;
            message.save();
            return message;
        except Message.DoesNotExist:
            return None

    def get(self, request, message_id):
        #Retrieves the Message with given message_id
        message = self.get_object(message_id, request.user.id)
        if not message:
            return Response(
                {"res": "Object with message_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, message_id):
    # Delete the message with the given message_id
        message = self.get_object(message_id, request.user.id)
        if not message:
            return Response(
                {"res": "Object with message_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = MessageSerializer(message)
        message.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)