from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        context = get_base_context(request, 'Добавление нового сниппета')
        form = SnippetForm()
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
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

# def snippets_form(request):
# print("request = ", request)
# if request.method == "POST":
# # print("request.POST = ", request.POST)
# name = request.POST["name"]
# lang = request.POST["lang"]
# code = request.POST["code"]
# snippet = Snippet(name=name, lang=lang, code=code)
# snippet.save()
# form = SnippetForm(request.POST)
# if form.is_valid():
#     form.save()
# else:
#     ...
# return redirect('snippets-list')

# if request.method == "GET":
#     request.GET
