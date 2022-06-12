from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos de nous</h1> <p>Nous adorons Merch !</p>')

def listing(request):
    return HttpResponse('<h1>Voici la liste des marchandises :</h1> <p>Tulipes : 15<br/> Roses : 12</p>')

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1> <p>Notre adresse mail : bullshit@mescouillessurlefront.com</p>')