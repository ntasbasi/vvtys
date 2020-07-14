# -*- coding: utf-8 -*-
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import redirect
from vvtys.video import Video,AttType,Att,Event
from django.http import *
from django import template
from django.template import Context, loader
import os
import cv2
import matplotlib.pyplot as plt

import scenedetect
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.frame_timecode import FrameTimecode
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector


import numpy as np
liste=[1,2,3] #normal python listesi
numpyliste=np.array([1,2,3]) #numpy dizisi

from django.core.files.storage import FileSystemStorage

def anasayfa(request):
    sablon = loader.get_template('anasayfa.html')
    icerik = Context()
    context_dict = icerik.flatten()
    return HttpResponse(sablon.render(context_dict))
def hakkimizda(request):
    sablon = loader.get_template('hakkimizda.html')
    icerik = Context()
    context_dict = icerik.flatten()
    return HttpResponse(sablon.render(context_dict))
def iletisim(request):
    sablon = loader.get_template('iletisim.html')
    icerik = Context({'baslik': 'Cok guzel blog, cok da guzel iyi blog!','makaleler' : [{'baslik':'b1','makale':'m1'},{'baslik':'b2','makale':'m2'},{'baslik':'b3','makale':'m3'}]})
    """
    yanit = sablon.render(iletisim)
    """
    context_dict = icerik.flatten()
    return HttpResponse(sablon.render(context_dict))
    #return HttpResponse(yanit)
IMAGE_FILE_TYPES = ['mov', 'MOV', 'mp4', 'MP4' , 'avi','AVI']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = 'G:/dddddd/Django-2.1.15/django/bin/ilkProjem/ilkProjem/static/videolar/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'G:/dddddd/Django-2.1.15/django/bin/ilkProjem/ilkProjem/static/videolar/')
def ekle(request):
    if request.method == 'POST' and request.FILES['videoName']:
        myfile = request.FILES['videoName']
        fs = FileSystemStorage(location='G:/dddddd/Django-2.1.15/django/bin/ilkProjem/ilkProjem/static/videolar/')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
    if request.method == 'POST':
       v = Video(
           videoName=filename,
           oTarihi=request.POST.get("oTarihi"),
           keyValue=request.POST.get("keyValue"),
       )
       v.save()
       return redirect(listele)
    return render(request,'ekle.html',locals())
def sVideoEkle(request):
    result=[]
    STATS_FILE_PATH = 'G:/dddddd/Django-2.1.15/django/bin/ilkProjem/ilkProjem/static/denemevideolar/testvideo2.stats.csv'   
    if request.method == 'POST' and request.FILES['videoName']:
        myfile = request.FILES['videoName']
        fs = FileSystemStorage(location='G:/dddddd/Django-2.1.15/django/bin/ilkProjem/ilkProjem/static/denemevideolar/')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = "G:/dddddd/Django-2.1.15/django/bin/ilkProjem/ilkProjem/static/denemevideolar/"+filename
        result.append([uploaded_file_url])
        video_manager = VideoManager(uploaded_file_url)
        """
        
        stats_manager = StatsManager()
        scene_manager = SceneManager(stats_manager)
        # Add ContentDetector algorithm (constructor takes detector options like threshold).
        scene_manager.add_detector(ContentDetector())
        base_timecode = video_manager.get_base_timecode()
        start_time = base_timecode + 20     # 00:00:00.667
        end_time = base_timecode + 20.0     # 00:00:20.000
            # Set video_manager duration to read frames from 00:00:00 to 00:00:20.
        video_manager.set_duration(start_time=start_time, end_time=end_time)

            # Set downscale factor to improve processing speed (no args means default).
        video_manager.set_downscale_factor()

            # Start video_manager.
        video_manager.start()

            # Perform scene detection on video_manager.
        scene_manager.detect_scenes(frame_source=video_manager)

            # Obtain list of detected scenes.
        scene_list = scene_manager.get_scene_list(base_timecode)
            # Like FrameTimecodes, each scene in the scene_list can be sorted if the
            # list of scenes becomes unsorted.

        for i, scene in enumerate(scene_list):
            result.append('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
                i+1,
                scene[0].get_timecode(), scene[0].get_frames(),
                scene[1].get_timecode(), scene[1].get_frames(),))

            # We only write to the stats file if a save is required:
        if stats_manager.is_save_required():
            with open(STATS_FILE_PATH, 'w') as stats_file:
                stats_manager.save_to_csv(stats_file, base_timecode)
    """
    if request.method == 'POST':
       return render(request,'sVideoSonuc.html',locals())
    return render(request,'sVideoEkle.html',locals())
   
def resimEkle(request):
    return render(request,'resimEkleme.html',locals())
def resimEkleme(request):    
    result=[]
    if request.method == 'POST' and request.FILES['resimAdi']:
        myfile = request.FILES['resimAdi']
        fs = FileSystemStorage(location='G:/dddddd/Django-2.1.15/django/bin/ilkProjem/ilkProjem/static/resimler/')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = "G:/dddddd/Django-2.1.15/django/bin/ilkProjem/ilkProjem/static/resimler/"+fs.url(filename)
        img = cv2.imread(uploaded_file_url)
        face_cascade = cv2.CascadeClassifier('C:\\projects\\opencv-python\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('C:\\projects\\opencv-python\\opencv\\data\\haarcascades\\haarcascade_eye.xml')
        faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)
        result.append(len(faces))
        result.append(5)
        result.append(filename)
        result.append(uploaded_file_url)
        return render(request,'yuzTanimaSonuc.html',locals())
    return render(request,'ekle.html',locals())
def listele(request):
    result = []
    for v in Video.objects.all():
      result.append(v)
    return render(request,'listele.html',locals())
def videoSil(request,idisi):
    v = Video.objects.get(id=idisi)
    v.delete()
    return redirect(listele)
def ekleDevam(request,idisi):
    result = []
    a = Video.objects.get(id=idisi)
    a.videoName='videolar/'+a.videoName
    result.append(a)
    return render(request,'ekledevam.html',locals())
def videoAnahtarEkle(request):
    if request.method == 'POST':
        degerler = request.POST.get("degerler")
        degerler = degerler[0: len(degerler) - 1]
        diziDeger = degerler.split(';')
        a = Video.objects.get(id=request.POST.get("videoID"))
        aty=AttType.objects.get(id=3)
        for deger in diziDeger:
                digerDeger = deger.split('-')
                att = Att(
                    attTypeID = aty,
                    videoID = a,
                    sure = digerDeger[0],
                    att = digerDeger[1],
                )                
                att.save()
    result = []
    a.videoName='videolar/'+a.videoName
    result.append(a)
    return render(request,'ekledevamolay.html',locals())
def videoAnahtarOlayEkle(request):
    if request.method == 'POST':
        degerler = request.POST.get("degerler")
        degerler = degerler[0: len(degerler) - 1]
        diziDeger = degerler.split(';')
        a = Video.objects.get(id=request.POST.get("videoID"))
        aty=AttType.objects.get(id=5)
        for deger in diziDeger:
                digerDeger = deger.split(':')
                eatt = Att(
                    attTypeID = aty,
                    videoID = a,
                    sure = digerDeger[0],
                    att = digerDeger[1],
                )                
                eatt.save()
    result = []
    for at in Att.objects.all():
      result.append(at)
    return render(request,'ozelliklerListele.html',locals())
def ozelliklerListele(request):
    result = []
    for at in Att.objects.all():
      result.append(at)
    return render(request,'ozelliklerListele.html',locals())
def olayOzelliklerListele(request):
    result = []
    for at in Event.objects.all():
      result.append(at)
    return render(request,'ozelliklerListele.html',locals())
def videoAnahtarSil(request,idisi):
    va = Att.objects.get(id=idisi)
    va.delete()
    return redirect(ozelliklerListele)
def attTypePage(request):
    if request.method == 'POST':
       a = AttType(
           attTypeName=request.POST.get("attTypeName"),
       )
       a.save()
       return redirect(attTypeListele)
    return render(request,'attTypePage.html',locals())
def attTypeListele(request):
    result = []
    for a in AttType.objects.all():
      result.append(a)    
    return render(request,'attTypeListele.html',locals())
def attTypeSil(request,idisi):
    a = AttType.objects.get(id=idisi)
    a.delete()
    return redirect(attTypeListele)
def attTypeDuzenle(request,idisi):
    result = []
    a = AttType.objects.get(id=idisi)
    result.append(a)
    return render(request,'attTypeDuzenleme.html',locals())
def attTypeDuzenleme(request):
    if request.method == 'POST':
       a = AttType.objects.get(id=request.POST.get("attTypeId"))
       a.attTypeName = request.POST.get("attTypeName")
       a.save()
       return redirect(attTypeListele)
    return render(request,'attTypePage.html',locals())
def deneme(request):
    result = []
    result.append(numpyliste)
    return render(request,'deneme.html',locals())
