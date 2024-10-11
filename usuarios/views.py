from django.shortcuts import render

def login(request):

    return render(request, "usuarios/login.html")

def minha_conta(request):

    return render(request, "usuarios/minha_conta.html")

def cadastro(request):

    return render(request, "usuarios/cadastro.html")

def logout(request):

    return render(request, "usuarios/logout.html")