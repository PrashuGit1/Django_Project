import time

class TimerMiddleware:
    def __init__(self, get_responce):
        self.get_responce=get_responce
        print("TimerMiddleware __init__ called")

    def __call__(self, request):
        print(time.time())
        start=time.time()
        response=self.get_responce(request)
        print("TimerMiddleware __call__ called")
        print(time.time())
        duration=time.time()-start
        print(f"[Middleware] Request to {request.path} took {duration:.4f} seconds.")
        return response