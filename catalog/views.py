from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from .models import Product
from django.urls import reverse
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages




class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = []  # Ничего не редактируем, только меняем статус
    permission_required = 'catalog.can_unpublish_product'  # Убедитесь, что это правильное разрешение
    template_name = 'catalog/product_unpublish.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.instance
        product.status = 'unpublished'  # Устанавливаем статус "не опубликован"
        return super().form_valid(form)

class ProductPublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = []  # Ничего не редактируем, только меняем статус
    permission_required = 'catalog.can_unpublish_product'
    template_name = 'catalog/product_publish.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.instance
        product.status = 'published'  # Устанавливаем статус "опубликован"
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        # Владелец или модератор может удалить продукт
        return product.owner == self.request.user or self.request.user.has_perm('catalog.delete_product') or self.request.user.is_superuser


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
    context_object_name = 'product'  # Имя объекта, который будет доступен в шаблоне

    # Разрешаем доступ всем пользователям (просмотр)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Добавляем проверку прав на редактирование в контекст шаблона
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user

        # Проверяем, может ли пользователь редактировать продукт
        can_edit = user.has_perm('catalog.change_product') or product.owner == user or user.is_superuser
        context['can_edit'] = can_edit

        return context


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.has_perm('catalog.change_product') or self.request.user.is_superuser


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        # Автоматически назначаем текущего пользователя владельцем продукта
        form.instance.owner = self.request.user
        return super().form_valid(form)

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