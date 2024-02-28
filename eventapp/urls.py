from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
   path('addevent/',views.addevent,name='addevent'),
   path('events/',views.events,name='events'),
   path('display/',views.event_display,name='event_display',),
   path('<int:id>/', views.addevent, name='event_update'),
    path('<int:id>/edit/', views.edit_event, name='edit_event'),
    path('<int:id>/delete/', views.delete_event, name='delete_event'),
#    path('<int:id>/',views.addevent,name="event_update")
]
