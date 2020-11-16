
def get_client_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
    if isinstance(ip, list):
        ip = list(filter(lambda i: i, ip))[0]
    return ip
