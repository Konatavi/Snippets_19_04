from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import auth
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.contrib.auth.decorators import login_required


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


@login_required
def add_snippet_page(request):
    if request.method == "GET":
        context = get_base_context(request, 'Добавление нового сниппета')
        form = SnippetForm()
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
        return redirect('snippets-list')


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = get_base_context(request, 'Просмотр сниппетов')
    context["snippets"] = snippets
    return render(request, 'pages/view_snippets.html', context)


def snippets_delete(request, id):
    snippet = Snippet.objects.get(id=id)
    snippet.delete()
    return redirect('snippets-list')


def snippets_edit(request, id):
    if request.method == "GET":
        context = get_base_context(request, 'Редактирование нового сниппета')
        snippet = Snippet.objects.get(id=id)
        form = SnippetForm(instance=snippet)
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        snippet = Snippet.objects.get(id=id)
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippets-list')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')
        # print("username =", username)
        # print("password =", password)


def logout_page(request):
    auth.logout(request)
    return redirect('home')