from typing import Any
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.urls.base import reverse_lazy
from todo.models import Post
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm

# Create your views here.
def create(request):
    form = PostForm(request.POST)
    form.save()
    return HttpResponseRedirect(reverse('todo:home'))


class HomeListView(LoginRequiredMixin, generic.ListView):
    template_name = 'todo/home.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user.id).order_by('-created_at')


class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'todo/update.html'
    model = Post
    fields = ['body',]
    success_url = reverse_lazy('todo:home')


class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'todo/delete.html'
    model = Post
    success_url = reverse_lazy('todo:home')
    context_object_name = 'deleted_data'


# def index(request):
#     posts = Post.objects.all()
#     form = PostForm()
#     context = {'posts': posts, 'form': form}
#     return render(request, 'todo/index.html', context)



# def update(request, id=None):
#     post = get_object_or_404(Post, pk=id)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('todo:index'))
#     else:
#         form = PostForm(instance=post)
#         return render(request, 'todo/update.html', {'form': form,})


# def delete(request, id=None):
#     post = get_object_or_404(Post, pk=id)
#     if request.method == 'GET':
#         return render(request, 'todo/delete.html', {'post': post,})
#     elif request.method == 'POST':
#         post.delete()
#         return HttpResponseRedirect(reverse('todo:index'))    