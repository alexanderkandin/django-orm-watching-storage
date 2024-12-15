from datacenter.models import Passcard, is_visit_long
from datacenter.models import Visit, get_duration, format_duration
from django.shortcuts import render
import locale


def passcard_info_view(request, passcode):
    locale.setlocale(locale.LC_TIME, 'russian')

    try:
        passcard = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        print("Нет такого ID")
        passcard = None

    if passcard:
        visits = Visit.objects.filter(passcard=passcard)
        this_passcard_visits = []
        for visit in visits:
            duration = get_duration(visit)
            formatted_duration = format_duration(duration)
            is_strange = is_visit_long(duration.total_seconds())

            this_passcard_visits.append({
                'entered_at': visit.entered_at.strftime("%d %B %Yг %H:%M"),
                'duration': formatted_duration,
                'is_strange': is_strange
            })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
