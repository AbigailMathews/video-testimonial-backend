from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import TestimonialSerializer

# Create your views here.
def index(request):
    return HttpResponse("Index of ListenFirst video testimonial app")


class TestimonialView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    testimonial_serializer = TestimonialSerializer(data=request.data)
    if testimonial_serializer.is_valid():
      testimonial_serializer.save()
      return Response(testimonial_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(testimonial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

