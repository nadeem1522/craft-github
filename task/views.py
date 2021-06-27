from task.models import Albumzone, Bannerchange, Navchang
from django.shortcuts import render

# Create your views here.
def index(request):

    navbar= Navchang.objects.all()

    banner=Bannerchange.objects.all()

    album=Albumzone.objects.all()

    data={
        'navbar':navbar,
        'banner':banner,
        'album':album,
    }
    return render(request,'index.html',data)