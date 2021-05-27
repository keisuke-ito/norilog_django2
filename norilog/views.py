from django.contrib.auth import login
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Noriori, CustomUser
from .forms import SignUpForm
from norilog import models

# Create your views here.
def save(request):
    Noriori(
        user = request.user,
        start = request.POST['start'],
        finish = request.POST['finish'],
        memo = request.POST['memo'],
    ).save()
    return HttpResponseRedirect(reverse('norilog:home'))

def update(request):
    return render(request, 'norilog/update.html')

def delete(request):
    return render(request, 'norilog/delete.html')

class IndexTemplateView(generic.TemplateView):
    template_name = 'norilog/index.html'

class HomeListView(LoginRequiredMixin, generic.ListView):
    template_name = 'norilog/home.html'
    model = Noriori

    def get_queryset(self):
        return Noriori.objects.filter(user=self.request.user.id).order_by('-created_at')


class NorioriUpdateView(generic.UpdateView):
    template_name = 'norilog/update.html'
    model = Noriori
    fields = ['start', 'finish', 'memo']
    success_url = reverse_lazy('norilog:home')


class NorioriDeleteView(generic.DeleteView):
    template_name = 'norilog/delete.html'
    model = Noriori
    success_url = reverse_lazy('norilog:home')
    context_object_name = "deleted_data"


class UserCreateView(generic.CreateView):
    template_name = 'norilog/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('norilog:home')

    def form_valid(self, form):
        super().form_valid(form)
        new_user = form.save()
        login(self.request, new_user)
        self.object = new_user
        return HttpResponseRedirect(self.get_success_url())

def guestlogin(request):
    guest_user = CustomUser.objects.get(pk=2)
    login(request, guest_user)
    return HttpResponseRedirect(reverse('norilog:home'))
