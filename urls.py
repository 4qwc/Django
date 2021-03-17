from django.urls import path
from . import views

urlpatterns = [
	# Path = converd
	# int: numbers
	# str: strings
	# path: whole urls
	# slug: hyphen-and_underscores_stuff
	# UUID: universarsally unique indentifier
	path('<int:year>/<str:month>/', views.index, name="index"),
	#path('<int:year>/<str:month>', views.home, name="home"),
]