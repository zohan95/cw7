from django.shortcuts import render
from django.views import View

from webapp.models import Poll, Choice, Answer


class StatView(View):
    def get(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        choices = Choice.objects.filter(poll=poll)
        list_stat = []
        list_each_stat = []
        avg = 0
        for i in choices:
            list_stat.append('{} (количество:{})'.format(i.variation, str(
                Answer.objects.filter(poll=poll).filter(variation=i).count())))
            avg += Answer.objects.filter(poll=poll).filter(variation=i).count()
            list_each_stat.append(Answer.objects.filter(poll=poll).filter(variation=i).count())
        for i in range(len(list_stat)):
            list_stat[i] += '({0:.2f}%)'.format((list_each_stat[i] / avg) * 100)
        return render(request, 'Stat/index.html', {'poll': poll, 'choices': choices, 'count_list': list_stat})
