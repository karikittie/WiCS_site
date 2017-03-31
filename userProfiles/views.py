import os

from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from WiCS.views import getIncludes


def profile(request):
    return render_to_response('profileTemplates/profile.html', {'title': 'User Profile', **getIncludes()})


class UserLoginView(View):
    formClass = AuthenticationForm
    templateName = 'profileTemplates/loginForm.html'

    def get(self, request):
        form = self.formClass(None)
        pathToStaticFiles = os.path.join(os.path.dirname('__file__'), 'static')
        return render_to_response(self.templateName, {'form': form, **getIncludes(pathToStaticFiles)})

    def post(self, request):
        form = self.formClass(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('userProfiles:profile')
        return render_to_response(self.templateName, {'form': form, })
