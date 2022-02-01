from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.


def newType(request):
    form = TypeForm()
    if request.method == 'POST':
        form = TypeForm(request.POST)
        form.save()
        return redirect('expense_history:expanse')
    return render(request, 'type_add.html', context={'form': form})


def expanse(request):
    forms = expanseForm()
    if request.method == "POST":
        forms = expanseForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('expense_history:history')
    context = {
        "Eforms": forms,
    }
    return render(request, "expanse.html", context=context)


def history(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        print(fromdate, todate)
        searchresult = Expanse.objects.filter(Date__range=[fromdate, todate])
        return render(request, "expanse_history.html", context={'Fhistory': searchresult})
    else:

        history = Expanse.objects.all()

        # context = {
        #     "Fhistory": history,
        # }

        return render(request, "expanse_history.html", context={"Fhistory": history})


def edit(request, id):
    history = Expanse.objects.get(id=id)
    forms = expanseEditForm(instance=history)
    if request.method == 'POST':
        forms = expanseEditForm(request.POST, instance=history)
        forms.save()
        return redirect('expense_history:history')
    # return render(request, "edit_expense_history.html", context={'forms': forms, 'name': history.Type})
    return render(request, "edit_expense_history.html", context={'forms': forms, 'name': history.Type})


def delete(request, id):
    history = Expanse.objects.get(id=id)
    history.delete()
    return HttpResponseRedirect(reverse('expense_history:history'))
