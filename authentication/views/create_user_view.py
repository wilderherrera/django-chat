from django.views import View
from django.shortcuts import render
from authentication.forms.user_creation_form import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


class UserCreator(View):
    def get(self, request):
        return render(template_name="registration/sign_up.html", request=request)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.email = form.data["email"]
            user.save()
            raw_password = form.cleaned_data.get('password1')
            print("User created -> ", str(user))
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
        return render(template_name="registration/sign_up.html", request=request, context={'form': form})
