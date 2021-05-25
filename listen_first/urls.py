from django.urls import path
from django.conf.urls import url

from .views import TestimonialListView, TestimonialCreateView, MetaTestView

urlpatterns = [
    #path('', TestimonialListView.as_view(), name='all'),
    path('create', TestimonialCreateView.as_view(), name='testimonial_create'),
    path('metatest', MetaTestView.as_view(), name="meta_test")
]