from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, RedirectView
from django.shortcuts import redirect
from .models import CustomUser
from django import forms



class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'telefon_raqam', 'password']


class LoginForm(forms.Form):
    telefon_raqam = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)



class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        telefon_raqam = form.cleaned_data['telefon_raqam']
        password = form.cleaned_data['password']

        if CustomUser.objects.filter(telefon_raqam=telefon_raqam).exists():
            form.add_error('telefon_raqam', "Bu telefon raqam allaqachon ro‘yxatdan o‘tgan.")
            return self.form_invalid(form)

        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        messages.success(self.request, "Ro‘yxatdan o‘tish muvaffaqiyatli!")
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        telefon_raqam = form.cleaned_data['telefon_raqam']
        password = form.cleaned_data['password']
        user = authenticate(self.request, telefon_raqam=telefon_raqam, 
                            password=password)

        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, "Telefon raqam yoki parol xato.")
            return self.form_invalid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Tizimdan chiqdingiz.")
        return super().get(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = reverse_lazy('login')
