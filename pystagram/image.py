import os
from optparse import OptionParser
from io import BytesIO
from PIL import Image, ImageOps
from django.core.files import File
from django.utils import six


def receiver_with_image_field(field_name, max_size):
    def receiver(sender, **kwargs):
        instance = kwargs['instance']
        field = getattr(instance, field_name)
        if field:
            if field.width > max_size or field.height > max_size:
                processed_file = thumbnail(field.file, max_size, max_size)
                field.save(field.name, File(processed_file))
    return receiver


def pil_image(input_f, quality=90):
    if isinstance(input_f, six.string_types):
        filename = input_f
    elif hasattr(input_f, 'name'):
        filename = input_f.name
    else:
        filename = 'noname.png'

    extension = os.path.splitext(filename)[-1].lower()
    try:
        format = {
            '.jpg': 'jpeg',
            '.jpeg': 'jpeg',
            '.png': 'png',
            '.gif': 'gif',
        }[extension]
    except KeyError:
        format = 'png'

    image = Image.open(input_f)
    return image, format


def image_to_file(image, format, quality):
    output_f = BytesIO()
    image.save(output_f, format=format, quality=quality)
    output_f.seek(0)
    return output_f


def thumbnail(input_f, width, height, quality=80):
    image, format = pil_image(input_f, quality)
    image.thumbnail((width, height), Image.ANTIALIAS)
    return image_to_file(image, format, quality)


def square_image(input_f, max_size, quality=80):
    image, format = pil_image(input_f, quality)
    max_size = min(image.size[0], image.size[1], max_size)
    image = ImageOps.fit(image, size=(max_size, max_size))
    return image_to_file(image, format, quality)
