from django.db import models

# Utility function for selecting media save path
def testimonial_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/media_type/filename
    return '{0}/{1}'.format(instance.media_type, filename)

# Create your models here.
class Testimonial(models.Model):

    MEDIA_TYPES = (
        ('A', 'Audio'),
        ('V', 'Video'),
    )

    participant_id = models.BigIntegerField(blank=False, null=False)
    media_file = models.FileField(upload_to=testimonial_path, blank=False, null=False)
    media_type = models.CharField(max_length=1, choices=MEDIA_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)