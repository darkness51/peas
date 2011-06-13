# edit to reflect your local environment and save as settings_local.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mutlugunumuz.db',
    }
}

DEFAULT_FROM_EMAIL = 'info@site.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25

FACEBOOK_APP_ID          = ''
FACEBOOK_API_SECRET      = ''

TWITTER_CONSUMER_KEY     = ''
TWITTER_CONSUMER_SECRET  = ''
