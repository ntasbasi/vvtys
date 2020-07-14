from django.db import models
import django.utils.timezone

class Video (models.Model):
        videoName=models.CharField(max_length=200, verbose_name='Video Adı :',db_column='videoName', help_text='Lütfen Video ismini Boş Geçmeyiniz')
        oTarihi=models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma tarihi', db_column='oTarihi')
        keyValue = models.TextField(verbose_name='Anahtar Değerler :', max_length=500,db_column='keyValue',default="")
        
class AttType(models.Model):
        attTypeName=models.CharField(max_length=200)
    
class Att(models.Model):
        att=models.TextField(verbose_name='Anahtar Değerler :', max_length=500,db_column='att',default="")
        sure=models.TextField(verbose_name='Süre Değerler :', max_length=500,db_column='sure',default="")
        videoID= models.ForeignKey(Video,on_delete=models.CASCADE)
        attTypeID=models.ForeignKey(AttType,on_delete=models.CASCADE)
    
class Event(models.Model):
        att=models.TextField(verbose_name='Anahtar Değerler :', max_length=500,db_column='att',default="")
        baslangicSure=models.TextField(verbose_name='Süre Değerler :', max_length=500,db_column='baslangicSure',default="")
        bitisSure=models.TextField(verbose_name='Süre Değerler :', max_length=500,db_column='bitisSure',default="")
        videoID= models.ForeignKey(Video,on_delete=models.CASCADE)
        attTypeID=models.ForeignKey(AttType,on_delete=models.CASCADE)
