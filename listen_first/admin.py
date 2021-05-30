from django.contrib import admin
from .models import Testimonial
from .forms import TestimonialForm

# Register your models here.

admin.site.site_header = "America Talks Project"

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialForm
    list_display = ('__str__', 'review', 'media_type')
    list_filter = ('review', 'media_type' )
    readonly_fields = ["participant_id", "terms_accepted", "media_file", "show_media_preview", "media_type", "timestamp", "media_download"]
