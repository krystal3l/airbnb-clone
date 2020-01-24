from django.urls import path
from rooms import views as room_views

app_name = "core"

# path(url, 함수, ...) as_view : view로 바꿔주는 메소드
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]

