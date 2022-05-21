# Create your views here.
from blog.models import Post, Category
from django.views.generic import ListView, DetailView


class Postlist(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(Postlist, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

class Postdetail(DetailView):
    model = Post