from django.shortcuts import render
from django.views.generic import View


class About(View):
    def get(self, request):
        return render(request, 'about/about.html')
