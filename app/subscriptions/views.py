from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Subscription
from .serializers import SubscriptionSerializer
from users.models import User
from rest_framework.response import Response
from rest_framework import status

class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        subscribed_channel_id = self.request.data.get('subscribed_channel')
        subscribed_channel = get_object_or_404(User, id=subscribed_channel_id)
        serializer.save(subscriber=self.request.user, subscribed_channel=subscribed_channel)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['subscriber'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubscriptionDetail(generics.RetrieveDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        subscribed_channel = get_object_or_404(User, id=self.kwargs['user_id'])
        return get_object_or_404(Subscription, subscriber=self.request.user, subscribed_channel=subscribed_channel)

    def delete(self, request, user_id, *args, **kwargs):
        subscription = self.get_object()
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)