from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    ItemListView, 
    ItemDetailView, 
    ItemCreateView, 
    ItemUpdateView,
    ItemDeleteView
    )

urlpatterns = [
    path('', ItemListView.as_view(), name='home'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('add/', ItemCreateView.as_view(), name='item-create'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)