from django.conf.urls import url

from .views import TestimonialView

urlpatterns = [
    url(r'testimonial', TestimonialView.as_view(), name='testimonial_upload'),
]