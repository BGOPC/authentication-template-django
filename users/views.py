from django.shortcuts import render
from django.views import View

# Create your views here.


class UserView(View):
    def get(self, request):
        return render(request, 'users/user.html')
    def post(self, request):
        pass