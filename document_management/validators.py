import magic
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class FileValidator:
    def __init__(self, allowed_formats=None, max_size=None):
        self.allowed_formats = allowed_formats
        self.max_size = max_size

    def __call__(self, value):
        if self.allowed_formats:
            file_type = magic.from_buffer(value.read(), mime=True)
            if file_type not in self.allowed_formats:
                raise ValidationError(f"Invalid file format. Allowed formats are {', '.join(self.allowed_formats)}.")

        if self.max_size and value.size > self.max_size:
            raise ValidationError(f"File size exceeds the maximum limit of {self.max_size} bytes.")
