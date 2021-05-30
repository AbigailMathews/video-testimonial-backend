from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import generics
from rest_framework import permissions
#from rest_framework_api_key.permissions import HasAPIKey

from .serializers import TestimonialSerializer
from .models import Testimonial


# Create your views here.
class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAdminUser]


class TestimonialCreateView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = TestimonialSerializer
    #permission_classes = [HasAPIKey]


class TestimonialDetailView(generics.RetrieveUpdateAPIView):
    model = Testimonial
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAdminUser]



