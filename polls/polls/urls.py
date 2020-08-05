from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:pk>/result', views.resultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]