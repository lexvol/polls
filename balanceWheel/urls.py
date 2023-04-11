from django.urls import path

from . import views

app_name = 'balanceWheel'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/1/
    path('<int:question_id>/', views.details, name='details'),
    # ex: /polls/results/
    path('results/', views.results, name='results'),
    # ex: /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
