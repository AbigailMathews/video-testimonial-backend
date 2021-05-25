from django.db import models
import uuid

# Utility function for selecting media save path
def testimonial_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/media_type/media_id
    media_id = uuid.uuid4()
    return '{0}/{1}'.format(instance.media_type, media_id)

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
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        review_status = 'Reviewed'
        if self.reviewed == False:
            review_status = 'Unreviewed'
        if self.media_type == 'A':
            media = 'Audio'
        else:
            media = 'Video'

        return '%s %s from participant %s' % (review_status, media, self.participant_id)