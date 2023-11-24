from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='post',
    manual_parameters=[openapi.Parameter(name="map", in_=openapi.IN_FORM, type=openapi.TYPE_FILE, required=True,
                                         description="map picture")],
    responses={
        201: "File uploaded successfully",
        400: "Bad Request, invalid data provided",
    },
    operation_summary="Upload a map picture",
    operation_description="Upload a map picture using this API endpoint.",
)
@api_view(['POST'])
@parser_classes([MultiPartParser])
def process_image(request):
    map_file = request.FILES.get('map')

    if not map_file:
        return Response({"error": "No file was provided."}, status=status.HTTP_400_BAD_REQUEST)

    file_name = map_file.name
    file_path = default_storage.save(file_name, ContentFile(map_file.read()))

    return Response({"message": "File uploaded successfully", "file_path": file_path}, status=status.HTTP_201_CREATED)
