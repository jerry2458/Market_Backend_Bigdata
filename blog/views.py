# Create your views here.
from blog.models import Post
from django.views.generic import ListView, DetailView


class Postlist(ListView):
    model = Post
    ordering = '-pk'

class Postdetail(DetailView):
    model = Post