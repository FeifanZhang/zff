from django.urls import path
from loginapp import views
urlpatterns = [
    # 子路由分发
    path('confirmAuth/', views.LoginView.as_view()),
]
