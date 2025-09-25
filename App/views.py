from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm


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