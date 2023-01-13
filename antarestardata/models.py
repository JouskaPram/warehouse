from django.db import models
from django.db.models import F , ExpressionWrapper, FloatField
# Create your models here.
class Suplier(models.Model):
    nama_suplier=models.CharField(max_length=40)
    datasup = models.TextField()
    def __str__(self):
        return self.nama_suplier

class Preorder(models.Model):
    produk = models.CharField(max_length=50)
    bahan = models.CharField(max_length=10)
    warna = models.CharField(max_length=30)
    ukuran = models.CharField(max_length=30)
    qty = models.IntegerField(null=True)
    harga = models.IntegerField(null=True)
    nama_penulis = models.CharField(max_length=40)
    suplier_id =models.ForeignKey(Suplier,on_delete=models.CASCADE,null=True)
   
    def jumlah(self):
        jumlah = self.qty * self.harga
        return jumlah
    def __str__(self):
        return self.nama_penulis
class AppPreorder(models.Model):
    nama_penyetuju = models.CharField(max_length=40)
    preorder_id = models.ForeignKey(Preorder,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nama_penyetuju

