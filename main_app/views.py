from django.shortcuts import render


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  return render(request, 'cats/index.html', {
    'cats': cats
  })