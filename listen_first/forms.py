from django.forms import ModelForm
from .models import Testimonial
from .widgets import RangeInput

class TestimonialForm(ModelForm):

    class Meta:
        model = Testimonial
        widgets = {
          'review': RangeInput(attrs={'step': '1', 'min': '1', 'max': '5'}),
        }
        fields = '__all__'
