from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
  class Meta():
    model = Testimonial
    fields = ('participant_id', 'terms_accepted', 'media_type', 'timestamp', 'media_file', 'review')

