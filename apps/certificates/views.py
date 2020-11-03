from rest_framework import viewsets
from .models import Certificate
from .serializers import CertificateSerializer
from rest_framework.permissions import IsAuthenticated

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]