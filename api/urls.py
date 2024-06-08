from django.urls import path

from .views import auth
from .views import github_cred

urlpatterns = [
    path("", auth.index, name="index"),
    path("register", auth.register, name="register"),
    path("login", auth.login, name="login"),
    path('logout', auth.logout, name='logout'),
    path("github-cred/fetch", github_cred.fetch, name="fetch"),
    path("github-cred/create", github_cred.create, name="create"),
    # path('hello-world/', views.hello_world, name='hello_world'),
]
