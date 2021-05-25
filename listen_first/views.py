from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from .serializers import TestimonialSerializer
from .models import Testimonial


class AllowedRequestSourcePermission(permissions.BasePermission):
    """
    Permission check for allowed IPs
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        print(request.META)
        #allowed_source = Allowed.objects.filter(ip_addr=ip_addr).exists()
        allowed_source = True
        return allowed_source


# Create your views here.
class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAdminUser]


class TestimonialCreateView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = TestimonialSerializer
    permission_classes = [AllowedRequestSourcePermission]


class MetaTestView(APIView):
    def get(self, request, format=None):
        meta_info = str(request.META)
        return Response(meta_info, status=status.HTTP_200_OK)

# from rest_framework.decorators import api_view

# @api_view()
# def meta_test(request):
#     return Response({"meta": request.META})


# class TestimonialView(APIView):
#   parser_classes = (MultiPartParser, FormParser, JSONParser)

#   def post(self, request, *args, **kwargs):
#     testimonial_serializer = TestimonialSerializer(data=request.data)
#     if testimonial_serializer.is_valid():
#       testimonial_serializer.save()
#       return Response(testimonial_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(testimonial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

