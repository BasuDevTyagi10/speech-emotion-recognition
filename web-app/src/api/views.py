import os

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage

from django.conf import settings

from .models import AudioFileModel
from .predict import predict


@api_view(['GET'])
def get_data(request):
    return Response({'test': 'TEST DATA'})


@api_view(['POST'])
def upload_file(request):
    file = request.FILES.get('file')
    fss = FileSystemStorage()
    filename = fss.save(file.name, file)
    filepath = fss.url(filename)

    AudioFileModel.objects.create(filepath=filepath)
    full_filepath = os.path.join(settings.MEDIA_ROOT, filename)
    result = predict(full_filepath)

    response = {
        'filename': filename,
        'filepath': filepath,
        'emotion': result
    }
    
    return Response(response)
