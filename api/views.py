from rest_framework import viewsets,status
from .serializer import LoginSerializer
from .models import tbl_login
from rest_framework.decorators import action
from rest_framework.response import Response


class  LoginViewSet(viewsets.ModelViewSet):
    queryset = tbl_login.objects.all()
    serializer_class = LoginSerializer

    @action(detail=False, methods=['get'], url_path='(?P<username>\w+)/(?P<password>\w+)')
    def get_user(self, request, username=None, password=None):
        try:
            # Filter the tbl_login table with the provided username and password
            
            user = tbl_login.objects.get(username=username, password=password)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except tbl_login.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


