from django.urls import path
from .views import event_list, event_detail

urlpatterns = [
    path('events/', event_list, name='event-list'),
    path('events/detail/', event_detail, name='event-detail'),
]
