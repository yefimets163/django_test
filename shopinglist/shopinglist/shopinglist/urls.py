from django.contrib import admin
from django.urls import path, include
import polls.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('polls.urls')),
]
