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
        'preorder':preorder,
      
    }
    return render(req,'admin-page.html',konteks)

def getpo(req):
    preorder = Preorder.objects.all()
    row_count = Preorder.objects.count()
    konteks={
        'preorder':preorder,
        'row_count':row_count
       
        
    }
    return render(req,'admin-po.html',konteks)

def addpreorder(req):
    if req.POST:
        form = FormPreorder(req.POST)
        if form.is_valid:
            form.save()
            form=FormPreorder()
            # pesan="data berhasil di tambahkan"
            konteks={
                'form':form,
                # 'pesan':pesan
            }
            return render(req,'tambah-po.html',konteks)
    else:
        form = FormPreorder(req.POST)
        konteks={
                'form':form,
                # 'pesan':pesan
            }
    return render(req,'tambah-po.html',konteks)


def suplier(req):
    sup = Suplier.objects.all()
    konteks={
        "sup":sup
    }
    return render(req,'supplier.html',konteks)