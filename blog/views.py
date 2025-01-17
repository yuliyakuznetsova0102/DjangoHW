from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Blog
from django.urls import reverse_lazy, reverse

class BlogPostListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(is_published=False)

class BlogPostCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('blog:blog_list')

    def get_object(self, queryset=None):
        content = self.kwargs.get(self.content_url_kwarg)
        queryset = queryset or self.get_queryset()
        return get_object_or_404(queryset, **{self.content_field: content})


class BlogPostDetailView(DetailView):
    model = Blog

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class BlogPostUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogPostDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class ContactView(TemplateView):
    template_name = 'blog/blog_contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)