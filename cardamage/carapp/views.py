from django.shortcuts import render, redirect
from carapp.forms import ImageForm
from carapp.models import PicUpload
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')

def list(request):
    image_path=''
    image_path1=''
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES) #Doubt in request.FILES

        if form.is_valid():
            newdoc = PicUpload(imagefile=request.FILES['imagefile']) #Doubts
            newdoc.save()

            #return HttpResponseRedirect(reverse('list')) #To load back the list again
            return redirect('list')
    else:
        form = ImageForm() 



    documents = PicUpload.objects.all()
    for document in documents:
        image_path = document.imagefile.name
        image_path1='/'+image_path
        document.delete()

    #To save image_path variable globally i.e. in different views as well we use sessions:
    request.session['image_path'] = image_path
    return render(request,'list.html',{'documents':documents,'image_path1':image_path1,'form':form})
