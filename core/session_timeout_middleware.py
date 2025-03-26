from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware

class SessionIdleTimeoutMiddleware(SessionMiddleware):
    def process_request(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the last activity time from the session
            last_activity = request.session.get('last_activity')
            current_time = datetime.now()

            # Check for session expiration
            if last_activity:
                last_activity_time = datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
                if current_time - last_activity_time > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                    # Log the user out if timeout is exceeded
                    from django.contrib.auth import logout
                    logout(request)
                    request.session.flush()  # Clear the session

            # Update the last activity timestamp
            request.session['last_activity'] = current_time.strftime('%Y-%m-%d %H:%M:%S')
