from django.shortcuts import render
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy


# Create your views here.

class SignUp(CreateView):

    form_class = forms.Customer_SignUp_Form
    success_url = reverse_lazy('customers:login')
    template_name = "customers/signup.html"




