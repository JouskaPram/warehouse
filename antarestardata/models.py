from django.db import models

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
    qty = models.IntegerField(max_length=20)
    harga = models.IntegerField(max_length=50)
    # jumlah = models.IntegerField(max_length=100)
    nama_penulis = models.CharField(max_length=40)
    suplier_id =models.ForeignKey(Suplier,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nama_penulis
class AppPreorder(models.Model):
    nama_penyetuju = models.CharField(max_length=40)
    preorder_id = models.ForeignKey(Preorder,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nama_penyetuju

