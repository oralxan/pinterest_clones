from django.urls import path,include
from django.urls import path
from .views import SignupView
urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('signup/',SignupView.as_view(),name='signup')
]