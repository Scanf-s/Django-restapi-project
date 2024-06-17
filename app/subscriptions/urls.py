from django.urls import path
from subscriptions import views

urlpatterns = [
    path('', views.SubscriptionList.as_view(), name='subscription_list'),
    path('<int:user_id>/', views.SubscriptionDetail.as_view(), name='subscription_detail'),
]