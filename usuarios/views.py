from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from usuarios.forms import CadastroForms, LoginForms


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')

        messages.error(
            request, 'Erro no login')
        return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(
                    request, 'User com este nome já existe, tente outro.')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(
                request, f'User {nome} foi cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'logout efetuado com sucesso!')
    return redirect('login')
