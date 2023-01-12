from django.shortcuts import render, redirect
from antarestardata.models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def base(req):
    return render(req,'home.html')
# template admin page
def adminpage(req):
    preorder = Preorder.objects.all()
    konteks={
        'preorder':preorder
    }
    return render(req,'admin-page.html',konteks)

def getpo(req):
    preorder = Preorder.objects.all()
    konteks={
        'preorder':preorder
    }
    return render(req,'admin-po.html',konteks)

def addpreorder(req):
    if req.POST:
        form = FormPreorder(req.POST)
        if form.is_valid:
            form.save()
            pesan="data berhasil di tambahkan"
            konteks={
                'form':form,
                'pesan':pesan
            }
            return render(req,'tambah-po.html',konteks)
    else:
        form = FormPreorder(req.POST)
        konteks={
                'form':form,
                'pesan':pesan
            }
    return render(req,'tambah-po.html',konteks)