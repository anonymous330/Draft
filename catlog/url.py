from django.urls import path
from . import views

urlpatterns =[
path('',views.login,name='login'),
path('index/',views.index,name='index'),
path('submit/',views.submit,name='submit'),
path('search/',views.search,name='search'),
path('change/<int:id>',views.change,name='change')
]
