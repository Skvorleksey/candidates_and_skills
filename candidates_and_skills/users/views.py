from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    """Sign up form"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'register.html'
