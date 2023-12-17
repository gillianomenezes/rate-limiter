from django.http import HttpResponse
from django.core.cache import cache

RATE_LIMIT_TIME_PERIOD = 60  # Em segundos
RATE_LIMIT_REQUESTS = 5  # Número máximo de solicitações permitidas no período

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    ip_address = get_client_ip(request)
    key = f'rate_limit:{ip_address}'
    count = cache.get(key, 0)

    if count >= RATE_LIMIT_REQUESTS:
        return HttpResponse("Rate limit exceeded", status=429)

    cache.set(key, count + 1, RATE_LIMIT_TIME_PERIOD)
    return HttpResponse("Hello, rate-limited world!")