from django.contrib import admin
from django.urls import path, include
from todo_api import views
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()

#Register TodoViewset with router
router.register('todoapi',views.TodoViewSet,basename='todo')

#include router urls in urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]
