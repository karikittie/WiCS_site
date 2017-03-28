from django.shortcuts import render_to_response
from WiCS.views import getIncludes


def profile(request):
    return render_to_response('profile.html', {'title': 'User Profile', **getIncludes()})
