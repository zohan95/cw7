from django.shortcuts import render, redirect
from django.views import View

from webapp.models import Poll, Choice, Answer


class AnswerView(View):
    def get(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        variab = Choice.objects.filter(poll=poll)
        return render(request, 'Answer/index.html', {'poll': poll, 'variab': variab})

    def post(self, request, pk):
        choice = Choice.objects.get(pk=request.POST.get('answer_radio'))
        poll = Poll.objects.get(pk=pk)
        Answer.objects.create(poll=poll, variation=choice).save()
        return redirect('poll_url')
