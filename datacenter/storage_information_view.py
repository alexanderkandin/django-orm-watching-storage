
from datacenter.models import Passcard, Visit, get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    all_visitors = Visit.objects.all()
    non_closed_visits = []

    for visitor in all_visitors:
        if visitor.leaved_at is None:
            duration = get_duration(visitor)
            format_time = format_duration(duration)
            visitor_info = {
            'who_entered': visitor.passcard,'entered_at': visitor.entered_at.strftime('%Y-%m-%d %H:%M:%S'), 'duration': format_time
            }
            non_closed_visits.append(visitor_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
