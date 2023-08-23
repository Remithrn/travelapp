from django.shortcuts import render,HttpResponse
from .models import PLace,Team
# Create your views here.
def home(request):
    obj=PLace.objects.all()
    obj2=Team.objects.all()
    return render(request,'index.html',{'result':obj,'Team_member':obj2})