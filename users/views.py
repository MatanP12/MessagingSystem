from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer, UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login

class LoginView(APIView):
    '''
        A view that handles login request
    '''
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        '''
            validated if the user exists and login
        '''
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
