from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, add_post

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_post, name='add-post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)