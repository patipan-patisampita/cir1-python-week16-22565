from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('member.urls'))
    #path('index/',include('member.urls'))
]
