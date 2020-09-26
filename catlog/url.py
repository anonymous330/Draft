from django.urls import path
from . import views

urlpatterns =[
path('',views.login,name='login'),
path('index/',views.index,name='index'),
path('submit/',views.submit,name='submit'),
path('search/',views.search,name='search'),
path('change/<int:id>',views.change,name='change'),
path('number/',views.number,name='number'),
path('view/',views.view,name='view'),
path('edit_detail/<int:id>',views.edit_detail,name='edit_detail'),
path('delete_farmer/<str:name>',views.delete_farmer,name='delete_farmer'),
path('delete_number/<int:id>',views.delete_number,name='delete_number')
]
