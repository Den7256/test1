from django.views.generic import TemplateView
from django.shortcuts import render
#
# Create your views here.
# def index(request):
#     title = 'Urban University'
#     text = 'text'
#     lists = [1, 2, 3]
#     len_list = len(lists)
#     context = {'text': text, 'title': title , 'lists': lists}
#     return render(request, 'index.html', context)
#
# from django.shortcuts import render
# from django.http import HttpResponse
#
# def index(request):
#     name = request.GET.get('name', "Guest")
#     return HttpResponse(f'Hello {name}')
#
# def simple_post(request):
#     if request.method == 'POST':
#         message = request.POST.get('message', '')
#         return HttpResponse(f'ваше сообщение - {message}')
#     return render(request, 'index2.html')

from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer

class PersonAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer







