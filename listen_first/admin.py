from django.contrib import admin
from .models import Testimonial
# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields = ["participant_id", "terms_accepted", "media_file", "media_type", "timestamp"]
