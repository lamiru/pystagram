from os.path import splitext
from uuid import uuid4
from django.utils import timezone


def random_name_with_file_field(model_instance, filename):
   app_label = model_instance.__class__._meta.app_label
   model_cls_name = model_instance.__class__.__name__
   dirpath_format = app_label + '/' + model_cls_name + '/%Y/%m/%d'
   dirpath = timezone.now().strftime(dirpath_format)
   random_name = uuid4().hex
   extension = splitext(filename)[-1]
   return (dirpath + '/' + random_name + extension).lower()
