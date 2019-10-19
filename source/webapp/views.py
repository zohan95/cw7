from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Poll


class PollView(ListView):
    template_name = 'Poll/index.html'
    model = Poll
    paginate_by = 5
    paginate_orphans = 1
    ordering = ['-created_at']


class PollDetails(DetailView):
    template_name = 'Poll/details.html'
    model = Poll


class PollEdit(UpdateView):
    template_name = 'Poll/edit.html'
    model = Poll
    fields = ['question']
    success_url = reverse_lazy('poll_url')


class PollDelete(DeleteView):
    template_name = 'Poll/delete.html'
    success_url = reverse_lazy('poll_url')
    model = Poll


class PollCreate(CreateView):
    template_name = 'Poll/create.html'
    model = Poll
    fields = ['question']
    success_url = reverse_lazy('poll_url')