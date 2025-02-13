from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from .models import Product
from django.urls import reverse
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class HomePageView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'image', 'price']
    success_url = reverse_lazy('catalog:product_list')


class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


# FBV
#
# def home_page(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'catalog/home.html', context)
#
# def contacts_page(request):
#      return render(request, 'catalog/contacts.html')
#
#
#
# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'catalog/product_list.html', context)
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'catalog/product_detail.html', context)