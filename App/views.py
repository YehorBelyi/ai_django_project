from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
import random


# Create your views here.
class HomeView(View):
    template_name = 'App/pages/home.html'

    def get(self, request):
        return render(request, self.template_name)


class UserRegisterView(View):
    template_name = 'App/pages/account/register.html'

    def get(self, request):
        form = UserRegisterForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            # user_group = Group.objects.get(name='User')
            # user.groups.add(user_group)

            login(request, user)
            return redirect('home')

        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    template_name = "App/pages/account/logout.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        return redirect('home')


class AiHomeView(View):
    template_name = 'App/pages/ai/main.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        message = request.POST.get('message', '')
        responses = [
            "test_response1",
            "test_response2",
            "test_response3",
            "test_response4",
            "test_response5",
        ]
        return JsonResponse({
            "user_message": message,
            "ai_message": random.choice(responses)
        })