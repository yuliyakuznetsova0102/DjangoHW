from blog.apps import BlogConfig
from django.urls import path
from .views import ( BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
    ContactView,
)

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list/', BlogPostListView.as_view(), name='blog_list'),
    path('blog/create/', BlogPostCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
    path('contacts/', ContactView.as_view(), name='blog_contact'), ]