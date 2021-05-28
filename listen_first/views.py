from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import generics
from rest_framework import permissions
from django.http import HttpResponseForbidden
from django_sendfile import sendfile

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
    permission_classes = [AllowedRequestSourcePermission] # TODO: Switch to API Key


class TestimonialDetailView(generics.RetrieveUpdateAPIView):
    model = Testimonial
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAdminUser]


# TODO: Implement fully or delete...
class SendMediaView(APIView):

    def get(self, request, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden()

        path = kwargs['type'] + '/' + kwargs['media_file']

        return sendfile(request, path)


def download(request, resource):
    filename = '/media' + resource
    if request.user.is_staff:
        return sendfile(request, filename)
    else:
        return HttpResponseForbidden()


