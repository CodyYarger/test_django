# polling/urls.py

from django.urls import path
from polling.views import PollListView, PollDetailView


# here we route to the different views based on the request.
urlpatterns = [
    path('', PollListView.as_view(), name="poll_index"),
    path('polls/<int:pk>/', PollDetailView.as_view(), name="poll_detail"),
]
