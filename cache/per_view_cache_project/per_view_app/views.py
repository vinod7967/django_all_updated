from django.shortcuts import render
# from django.views.decorators.cache import cache_page

# Create your views here.
# @cache_page(30)
def index3(request):
    return render(request, 'per_view.html')


def home(request):
    return render(request, 'per_view_home.html')