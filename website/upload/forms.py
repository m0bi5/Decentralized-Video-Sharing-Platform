from django import forms
from django.core.exceptions import ValidationError

def set_field_html_name(cls, new_name):
    """
    This creates wrapper around the normal widget rendering, 
    allowing for a custom field name (new_name).
    """
    old_render = cls.widget.render
    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)

    cls.widget.render = _widget_render_wrapper

class UploadForm(forms.Form):
    title = forms.CharField(max_length=100)
    file=forms.FileField()
    set_field_html_name(file, 'file')
    description = forms.CharField(max_length=1000000,widget=forms.Textarea)
    tags = forms.CharField(max_length=1000000,widget=forms.Textarea)


