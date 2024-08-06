from django.shortcuts import render

def cadastro(request):
    if request.method=="GET":
     print("cadastrado")
     return render(request, 'cadastro.html')