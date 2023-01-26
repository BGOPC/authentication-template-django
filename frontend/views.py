from django.shortcuts import render
from django.views import View


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'frontend/main.html')

    def post(self, request):
        pass
