from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoiceForm
from webapp.models import Poll, Choice


class ChoiceCreate(View):
    def get(self, request, pk):
        form = ChoiceForm()
        return render(request, 'Choice/create.html', {'form': form,'pk':pk})

    def post(self, request, pk):
        bound_from = ChoiceForm(request.POST)
        if bound_from.is_valid():
            choice = Choice()
            choice.variation = bound_from.cleaned_data['variation']
            choice.poll = Poll.objects.get(pk=pk)
            choice.save()
            return redirect('poll_url')
        return render(request, 'Choice/create.html', context={'form': bound_from})


class ChoiceEdit(UpdateView):
    model = Choice
    template_name = 'Choice/edit.html'
    fields = ['variation']
    success_url = reverse_lazy('poll_url')


class ChoiceDelete(DeleteView):
    model = Choice
    template_name = "Choice/delete.html"
    success_url = reverse_lazy('poll_url')

