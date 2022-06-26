from django.urls import path
from zarafshon.views import TagPageView, homePageView, AboutUsView, NewsView, ContactUsView, PostDetailPageView, Register, Login, logout_view

app_name = 'zarafshon'

urlpatterns = [
   path('', homePageView.as_view(), name='home'),
   path('aboutus', AboutUsView.as_view(), name='aboutus'),
   path('contactus', ContactUsView.as_view(), name='contactus'),
   path('news', NewsView.as_view(), name='news'),
   path('tags/<str:slug>/', TagPageView.as_view(), name='tag'),
   path('detail/<str:slug>/', PostDetailPageView.as_view(), name='detail'),

   path('register/', Register.as_view(), name='register'),
   path('login/', Login.as_view(), name='login'),
   path('logout/', logout_view, name='logout'),
]
