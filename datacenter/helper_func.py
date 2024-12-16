from django.utils.timezone import now, utc


def get_duration(visitor):
    entered_at = visitor.entered_at
    leaved_at = visitor.leaved_at or now().astimezone(utc)
    duration = leaved_at - entered_at
    return duration

def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours}ч {minutes}мин"

def is_visit_long(visit, minutes=60):
    is_strange = visit > minutes*60
    return is_strange