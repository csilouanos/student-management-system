from rest_framework import viewsets
from .models import Lecture
from .serializers import LectureSerializer
from rest_framework.permissions import IsAuthenticated

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]