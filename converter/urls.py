from django.urls import path
from .views import FileUploadConvertAPIView

urlpatterns = [
    path('upload-convert/', FileUploadConvertAPIView.as_view(), name='upload_convert'),
]
