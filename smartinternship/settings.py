INSTALLED_APPS = [
    import os

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'accounts/templates')],
        ...
    },
]
]