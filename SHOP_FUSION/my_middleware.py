from django.http import HttpResponse
from django.shortcuts import render


class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Custom-Header'] = 'This is a custom header'
        return response
    

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # You can use this to turn maintenance mode on or off.
        self.maintenance_mode = False

    def __call__(self, request):
        if self.maintenance_mode:
            return render(request, 'maintenance.html')
        return self.get_response(request)