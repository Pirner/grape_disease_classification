from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('classify', views.classify_view, name='classify_view'),
    path('<int:grape_classification_id>/', views.detail, name='detail'),
]
