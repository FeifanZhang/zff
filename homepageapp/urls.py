from django.urls import path
from homepageapp import views
urlpatterns = [
    # 子路由分发
    path('words/', views.WordView.as_view()),
    path('photos/', views.PhotoView.as_view()),
]
