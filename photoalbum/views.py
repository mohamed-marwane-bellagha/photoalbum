from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Image
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .functions import handle_uploaded_file
from django.utils import timezone
from .forms import UploadFileForm


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'photoalbum/index.html'
    context_object_name = 'latest_image_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Image.objects.order_by('-date_published')[:5]

class DetailView(generic.DetailView):
    model = Image
    template_name = 'photoalbum/detail.html'



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Image(image_name=request.FILES['file'],filename= request.FILES['file'].name ,date_published=timezone.now())
            instance.save()
            return HttpResponseRedirect('/photoalbum/')
    else:
        form = UploadFileForm()
    return render(request, 'photoalbum/upload.html', {'form': form})