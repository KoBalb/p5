from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from main.forms import TextForm
from main.models import Text

# Create your views here.
def index(request):
    form = TextForm()

    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            texts = form.save()

    texts = Text.objects.all()
    data = {
        'form' : form,
        'texts': texts,
    }
    return render(request, 'main/index.html', data)
