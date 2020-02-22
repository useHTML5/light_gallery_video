from setuptools import setup, find_packages

setup(
    name="light_gallery_video",
    version="0.5",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=2.2",
        'django-cms>=3.5',
        'django-filer>=1.6.0'
    ],
)
