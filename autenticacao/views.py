from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages


def register(req):
    # if req.user.is_authenticated:
    #     return redirect('/')

    if req.method == 'GET':
        return render(req, 'register.html')
    elif req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(req, constants.ERROR,
                                 'Preencha todos os campos')
            return redirect('/auth/register')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(
                req, constants.ERROR, 'Já existe um usuário com esse nome cadastrado')
            return redirect('/auth/register')

        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            messages.add_message(req, constants.SUCCESS,
                                 'Cadastro realizado com sucesso')

            return redirect('/auth/login')
        except:
            messages.add_message(req, constants.ERROR,
                                 'Erro interno do sistema')
            return redirect('/auth/register')

    return HttpResponse(f'')


def login(req):
    # if req.user.is_authenticated:
    #     return redirect('/')

    if req.method == "GET":
        return render(req, 'login.html')
    elif req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        usuario = auth.authenticate(username=username, password=password)

        if not usuario:
            messages.add_message(req, constants.ERROR,
                                 'Username ou senha inválidos')

            return redirect('/auth/login')
    else:
        auth.login(req, usuario)

        return redirect('/')
