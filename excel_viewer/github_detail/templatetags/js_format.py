from django.utils.safestring import mark_safe
from django.template import Library

import json

register = Library()


@register.filter(is_safe=True)
def js_format(obj):
    return mark_safe(json.dumps(obj))
