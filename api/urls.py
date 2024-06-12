from django.urls import path

from .views import auth
from .views import github_repo

urlpatterns = [
    path("", auth.index, name="index"),
    path("register", auth.register, name="register"),
    path("login", auth.login, name="login"),
    path('logout', auth.logout, name='logout'),
    path("github-repo/fetch", github_repo.fetch, name="fetch"),
    path("github-repo/create", github_repo.create, name="create"),
    path('github-repo/delete/<int:id>', github_repo.delete, name='delete'),
    # path('hello-world/', views.hello_world, name='hello_world'),
]
