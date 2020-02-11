from setuptools import setup, find_packages

setup(
    name="light_gallery_video",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "django>=2.2",
        'django-cms>=3.5',
        'django-filer>=1.6.0'
    ],
)
