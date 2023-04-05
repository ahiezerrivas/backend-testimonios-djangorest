from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Testimonios
from .serializers import TestimonioSerializer

@api_view(['GET'])
def getTestimonios(request):
    testimonio = Testimonios.objects.all()
    serializer = TestimonioSerializer(testimonio, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def posTestimonios(request):
   data = request.data
   testimonio = Testimonios.objects.create(
       nombre=data['nombre'],
       pais=data['pais'],
       cargo=data['cargo'],
       empresa=data['empresa'],
       testimonio=data['testimonio'],
   )
   serialzer = TestimonioSerializer(testimonio, many=False)
   return Response(serialzer.data)