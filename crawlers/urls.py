from django.urls import path

from . import views

app_name= 'crawlers'
urlpatterns = [
 	path('', views.IndexView.as_view(), name='index'),
 	path('process/<instruction_id>', views.process, name='process'),
 	path('list/<model_name>', views.generic_list, name='list'),
 	path('detail/<model_name>/<id>', views.generic_detail, name='detail')
]