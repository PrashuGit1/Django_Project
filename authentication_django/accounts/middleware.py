# myapp/middleware.py
from django.http import HttpResponseForbidden

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = ['192.168.1.100']  # Add more IPs if needed

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')  # Get user's IP address
        if ip in self.blocked_ips:
            return HttpResponseForbidden("Access Denied: Your IP is blocked.")

        # Call the next middleware or view
        response = self.get_response(request)

        # ✅ Add a custom header to indicate middleware was used
        response["X-Processed-By"] = "BlockIPMiddleware"

        # ✅ Optionally, modify response content for testing (only if it's text-based)
        if response.get("Content-Type", "").startswith("text/html"):
            response.content += b"\n<!-- Processed by BlockIPMiddleware -->"

        return response