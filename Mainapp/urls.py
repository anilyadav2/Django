from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name= 'Mainapp'

URLPattern=[
    path('',views.index, name='index'),
    path('topics',views.topics,name='topics' ),
    path('topics/<int:topic_id>/',views.topics,name='topics' )

]



