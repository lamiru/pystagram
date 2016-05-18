from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

def owner_required(model_cls, field_name='pk'):
    def wrap_fn(view_fn):
        def wrap(request, *args, **kwargs):
            field_value = kwargs[field_name]
            params = { field_name: field_value }
            obj = get_object_or_404(model_cls, **params)
            if (not request.user.is_staff) and obj.author != request.user:
                return HttpResponseForbidden('invalid user')
            return view_fn(request, *args, **kwargs)
        return wrap
    return wrap_fn
