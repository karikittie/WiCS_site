from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from WiCS.views import getIncludes


def profile(request):
    return render_to_response('templates/profile.html', {'title': 'User Profile', **getIncludes()})


class UserRegistrationView(View):
    formClass = UserForm
    templateName = 'registrationForm.html'

    def get(self, request):
        form = self.formClass(None)
        return render_to_response(self.templateName, {'form': form})

    def post(self, request):
        form = self.formClass(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #Clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('userProfiles:profile')
        return render_to_response(self.templateName, {'form': form})
