import re
from django import forms
from django.utils import six
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class PointWidget(forms.HiddenInput):
    def render(self, name, value, attrs=None):
        width = str(self.attrs.get('width', '100%'))
        height = str(self.attrs.get('height', 300))
        if width.isdigit():
            width += 'px'
        if height.isdigit():
            height += 'px'

        self.attrs['base_lat'] = '37.497921'
        self.attrs['base_lng'] = '127.027636'

        if value:
            if isinstance(value, six.text_type):
                try:
                    lng, lat = re.findall(r'[\d\.]+', value)
                except (IndexError, ValueError):
                    pass
            else:
                raise NotImplementedError('not support point type : {}'.format(value.__class__))

            self.attrs['base_lat'] = lat
            self.attrs['base_lng'] = lng

        html = render_to_string('point_widget.html', {
            'id': attrs['id'],
            'base_lat': self.attrs['base_lat'],
            'base_lng': self.attrs['base_lng'],
            'width': width,
            'height': height,
        })

        rendered = super(PointWidget, self).render(name, value, attrs)
        return rendered + mark_safe(html)
