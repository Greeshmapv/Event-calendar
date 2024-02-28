from django.urls import path
from.import views
urlpatterns = [
    path('',views.registration,name="registration"),
    path('login/',views.login_event,name="login_event"),
    path('logout/',views.logout_user,name="logout"),
]
