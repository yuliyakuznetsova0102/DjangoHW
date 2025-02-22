from django.urls import path
from .views import HomePageView, ContactsPageView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductDeleteView, ProductUpdateView, ProductUnpublishView, ProductPublishView, ProductsByCategoryView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/unpublish/<int:pk>/', ProductUnpublishView.as_view(), name='unpublish_product'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='unpublish_product'),
    path('product/<int:pk>/publish/', ProductPublishView.as_view(), name='publish_product'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]


