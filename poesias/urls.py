from django.urls import path
from poesias.views import home_view, sobre_view, user_view, blog_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home_view),
    path("sobre/", sobre_view),
    path("user/<str:username>/", user_view),
    path("blog/", blog_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
