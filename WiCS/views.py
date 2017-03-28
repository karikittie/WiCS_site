import os

from django.shortcuts import render_to_response

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_STATIC = os.path.join(BASE_DIR, "static")


def home(request):
    staticCSS = os.listdir(os.path.join(BASE_STATIC, "CSS"))
    staticCSS = [file for file in staticCSS if file.endswith(".css")]
    staticJS = os.listdir(os.path.join(BASE_STATIC, "JS"))
    return render_to_response('home.html', {'title': 'home', 'staticCSS': staticCSS, 'staticJS': staticJS})
