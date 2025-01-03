from datacenter.helper_func import get_duration, format_duration
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    storage_visitors = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visitor in storage_visitors:
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
