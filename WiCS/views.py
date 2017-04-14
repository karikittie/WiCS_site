import os
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html', {'title': 'home', **getIncludes()})


def about(request):
    return render_to_response('about.html', {'title': 'about', **getIncludes()})


def contact(request):
    return render_to_response('contact.html', {'title': 'contact', **getIncludes()})

def getBaseURL():
    baseDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(baseDirectory, "static")

def getIncludes(base=None):
    baseStatic = getBaseURL()
    if base is not None:
        baseStatic = base
    staticCSS = os.listdir(os.path.join(baseStatic, "CSS"))
    staticCSS = [file for file in staticCSS if file.endswith(".css")]
    staticJS = [file for file in os.listdir(os.path.join(baseStatic, "JS")) if file.endswith(".js")]
    return {'staticCSS': staticCSS, 'staticJS': staticJS}
