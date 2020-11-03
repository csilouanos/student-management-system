from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import *
from rest_framework.settings import api_settings

class UserViewSet(viewsets.ModelViewSet):
    #Gets all the user objects back
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    #Enables the django UI
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# class Login(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         print('DATA ', request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })
