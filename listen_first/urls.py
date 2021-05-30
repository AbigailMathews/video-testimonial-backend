from django.urls import path

from .views import TestimonialCreateView

urlpatterns = [
    #path('', TestimonialListView.as_view(), name='all'),
    path('create', TestimonialCreateView.as_view(), name='testimonial_create'),
    #path('media/<str:type>/<str:media_file>', SendMediaView.as_view(), name="media"),

]