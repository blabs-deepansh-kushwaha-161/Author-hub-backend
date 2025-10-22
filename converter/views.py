import os
import pypandoc
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from .models import UploadedFile

class FileUploadConvertAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        # Save the uploaded file
        uploaded_file = UploadedFile.objects.create(file=file_obj)

        # Convert to EPUB
        input_path = uploaded_file.file.path
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}.epub"

        pypandoc.convert_file(input_path, 'epub', outputfile=output_path)

        # Return EPUB as downloadable response
        return FileResponse(open(output_path, 'rb'), as_attachment=True, filename=os.path.basename(output_path))
