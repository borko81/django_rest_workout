from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerialzier


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer