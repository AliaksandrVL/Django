from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views.generic import FormView

from django.contrib.auth import login

from . import forms

class LoginView(FormView):
    template_name = 'security/login.htm'
    success_url = reverse_lazy('articles:list')
    form_class = forms.LoginForm

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            login(request, form.user)

            return redirect(self.success_url)