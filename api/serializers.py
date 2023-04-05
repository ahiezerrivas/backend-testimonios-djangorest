from rest_framework.serializers import ModelSerializer

from .models import Testimonios

class TestimonioSerializer(ModelSerializer):
    class Meta:
        model = Testimonios
        fields = ('nombre','pais','cargo','empresa','testimonio',)
