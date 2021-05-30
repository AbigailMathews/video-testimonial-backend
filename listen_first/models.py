from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator

import uuid

# Utility function for selecting media save path
def testimonial_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/media_type/media_id
    media_id = uuid.uuid4()
    return '{0}/{1}.webm'.format(instance.media_type, media_id)

# Create your models here.
class Testimonial(models.Model):

    MEDIA_TYPES = (
        ('A', 'Audio'),
        ('V', 'Video'),
    )

    participant_id = models.BigIntegerField(blank=False, null=False)
    terms_accepted = models.BooleanField(default=False)
    media_file = models.FileField(upload_to=testimonial_path, blank=False, null=False)
    media_type = models.CharField(max_length=1, choices=MEDIA_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    review = models.IntegerField(blank=False, null=True, validators=[MaxValueValidator(5), MinValueValidator(1)])

    review.short_description = 'Rate this testimonial (1-5)'

    # Custom action for django admin -- Show testimonial in the detail page
    def show_media_preview(self):
        if self.media_type == 'A':
            return mark_safe('<audio controls src="/media/{0}" />'.format(self.media_file))
        if self.media_type == 'V':
            return mark_safe('<video controls src="/media/{0}" />'.format(self.media_file))

    show_media_preview.short_description = 'Preview Testimonial'

    # Custom action for django admin -- Allow staff to download testimonials
    def media_download(self):
        return mark_safe('<a href="/media/{0}" download>Download</a>'.format(self.media_file))

    media_download.short_description = 'Download File'


    def __str__(self):

        if not self.review:
            review_status = 'Unreviewed'
        else:
            review_status = '%s star reviewed' % (self.review)

        if self.media_type == 'A':
            media = 'Audio'
        else:
            media = 'Video'

        return '%s %s from participant %s' % (review_status, media, self.participant_id)