import os
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html', {'title': 'home', **getIncludes()})


def getIncludes():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_STATIC = os.path.join(BASE_DIR, "static")
    staticCSS = os.listdir(os.path.join(BASE_STATIC, "CSS"))
    staticCSS = [file for file in staticCSS if file.endswith(".css")]
    staticJS = [file for file in os.listdir(os.path.join(BASE_STATIC, "JS")) if file.endswith(".js")]
    return {'staticCSS': staticCSS, 'staticJS': staticJS}
