from django.urls import path
from . import views
urlpatterns=[path('',views.home),
path('result',views.result),
path('form',views.form),
path('questions',views.question),
path('question/<int:qid>',views.quiz)
]