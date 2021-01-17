from . import views

urlpatterns = [
	
    path('', views.home, name="home"),
    path('home_view/',views.home_view,name="home_view")
]