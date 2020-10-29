from rest_framework import viewsets
from .serializers import *

# @permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    #Gets all the user objects back
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     raise PermissionDenied()