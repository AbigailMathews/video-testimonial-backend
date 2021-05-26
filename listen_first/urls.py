from django.urls import path

from .views import TestimonialListView, TestimonialCreateView, MediaView

urlpatterns = [
    #path('', TestimonialListView.as_view(), name='all'),
    path('create', TestimonialCreateView.as_view(), name='testimonial_create'),
    #path('media/<str:type>/<str:media_id>', MediaView.as_view(), name="media"),
]