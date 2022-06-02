from django.urls import path
#from blogging.views import detail_view, list_view
from blogging.views import PostListView, PostDetailView


# updated for assignment 08. using the as_view() method of our new classes
urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]


# urlpatterns = [
#     path('', list_view, name="blog_index"),
#     path('posts/<int:post_id>/', detail_view, name="blog_detail"),
# ]
