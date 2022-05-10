# polling/urls.py

from django.urls import path
from polling.views import list_view, detail_view


# here we route to the different views based on the request.
urlpatterns = [
    path('', list_view, name="poll_index"),
    path('polls/<int:poll_id>/', detail_view, name="poll_detail"),
]