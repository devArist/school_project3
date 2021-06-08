from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    pictures = models.Photo.objects.filter(status=True).order_by('-date_update')[:12]
    paginator = Paginator(object_list=pictures, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/index.html', {'page_obj':page_obj})

def video(request):
    videos = models.Video.objects.filter(status=True).order_by('-date_update')
    return render(request, 'gallery/videos.html')

def photo_detail(request, pk):
    return render(request, 'gallery/photo-detail.html')

def video_detail(request, pk):
    pass