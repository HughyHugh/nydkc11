from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Video
from .models import Newsletter, Minutes
def videos(request):
	video_list = Video.objects.order_by('-post')
	context = {
		'video_list':video_list,	
	}
	return render(request,'resources/videos.html',context)
def minutes(request):
	minutes_list = Minutes.objects.order_by('-pk').reverse()
	return render(request,'resources/minutes.html',{'minutes_list':minutes_list})
# Create your views here.
