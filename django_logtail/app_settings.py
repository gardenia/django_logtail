from django.conf import settings

LOGTAIL_FILES = getattr(settings, 'LOGTAIL_FILES', {})
LOGTAIL_UPDATE_INTERVAL = getattr(settings, 'LOGTAIL_UPDATE_INTERVAL', '3000')
LOGTAIL_MAX_TAIL_BYTES = getattr(settings, 'LOGTAIL_MAX_TAIL_BYTES', -1)
