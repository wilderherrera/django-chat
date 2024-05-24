from django.core.cache import cache
from asgiref.sync import sync_to_async
import time
from django.conf import settings


class Throttle:
    @sync_to_async
    def check_message_limit(self, user_id):
        key = f"throttle_{user_id}"
        now = time.time()
        window = settings.SOCKET_THROTTLE["window"]
        limit = settings.SOCKET_THROTTLE["limit"]
        timestamps = cache.get(key, [])
        timestamps = [ts for ts in timestamps if now - ts < window]
        if len(timestamps) >= limit:
            return False
        timestamps.append(now)
        cache.set(key, timestamps, timeout=window)
        return True
