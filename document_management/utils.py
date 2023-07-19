import os
from django.conf import settings
from django.core.exceptions import ValidationError
from docx import Document
from io import BytesIO
from django.core.files.base import ContentFile

def convert_docx_to_pdf(docx_file):
    try:
        doc = Document(docx_file)
        pdf_bytes = BytesIO()
        doc.save(pdf_bytes)
        pdf_bytes.seek(0)
        pdf_file_path = os.path.join(settings.MEDIA_ROOT, 'converted_documents', 'output.pdf')
        
        with open(pdf_file_path, 'wb') as pdf_file:
            pdf_file.write(pdf_bytes.read())

        return pdf_file_path

    except Exception as e:
        raise ValidationError("Failed to convert the document to PDF.")
