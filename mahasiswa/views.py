from django.shortcuts import render
from .models import MahasiswaModel

# Create your views here.
def index(req):
    return render(req, 'base.html', context={
        'mahasiswas': MahasiswaModel.objects.all()
    })