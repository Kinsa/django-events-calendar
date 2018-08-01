import os

from setuptools import setup, find_packages

description = "Simple Upcoming Events Calendar for Django"
long_description = description

if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name='django-events',
    version='1.0.5',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'Pillow>=3.1.1',
        'sorl-thumbnail>=3.2.5',
        'Django>=1.11'
    ],
    author='Joe Bergantine',
    author_email='joe.bergantine@gmail.com',
    description=description,
    long_description=long_description,
    url='https://github.com/jbergantine/django-events',
    download_url='https://github.com/jbergantine/django-events/tarball/1.0.4',
    license='New BSD License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite="runtests.runtests",
    include_package_data=True,
)
