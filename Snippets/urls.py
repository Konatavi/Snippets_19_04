from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from MainApp import views

urlpatterns = [
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('snippets/form/', views.snippets_form),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

