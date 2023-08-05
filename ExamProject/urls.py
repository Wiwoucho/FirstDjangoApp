
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ExamProject.common.urls')),
    path('/', include('ExamProject.main.urls')),
]
