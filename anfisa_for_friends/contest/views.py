from django.shortcuts import render

from .forms import ContestForm


def proposal(request):
    template = 'contest/form.html'
    form = ContestForm(request.GET or None)
    context = {'form': form}
    return render(request, template, context)
