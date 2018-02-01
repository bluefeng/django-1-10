from django import forms
from django.utils.translation import ugettext_lazy as _

from .widgets import BodyMdTextarea


class BlogPostForm(forms.ModelForm):
    body = forms.CharField(label=_('内容'), widget=BodyMdTextarea)

    class Meta:
        fields = ['status','title','excerpt','pub_date','cover','category','tags','author']