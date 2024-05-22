from django import forms
from .models import Candidate

class CertificateUploadForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['candidate_id', 'certificate_file']
        