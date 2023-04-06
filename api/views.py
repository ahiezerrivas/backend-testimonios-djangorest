from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework import status,generics
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



class obtenerUno(generics.GenericAPIView):
    queryset = Testimonios.objects.all()
    serializer_class  = TestimonioSerializer

    def get_testimonio(self,id):
        try:
            return Testimonios.objects.get(id=id)
        except:
            return None
        
    def get(self,request,id):
        testimonio = self.get_testimonio(id=id)
        if testimonio == None:
            return Response({'status':'fail','message':f'Note with Id: {id} not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(testimonio)
        return Response({'status':'success', 'note':serializer.data})
    