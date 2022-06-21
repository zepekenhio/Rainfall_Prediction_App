
from django.shortcuts import render, redirect
from .models import Data
from .forms import DataForm

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')
    else:
        form = DataForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/index.html', context)

def predictions(request):
    predicted_diabeties = Data.objects.all()
    context = {
        'predicted_diabeties': predicted_diabeties
    }
    return render(request, 'dashboard/predictions.html', context)