from setuptools import setup, find_packages


setup(
    name='django-events',
    version='1.0.0',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'Pillow>=3.1.1',
        'sorl-thumbnail>=3.2.5',
        'Django>=1.4'
    ],
    author='Joe Bergantine',
    author_email='jbergantine@gmail.com',
    description="Simple Upcoming Events Calendar for Django",
    url='https://github.com/jbergantine/django-events',
    download_url='https://github.com/jbergantine/django-events/tarball/develop',
    license='New BSD License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    test_suite="runtests.runtests",
    include_package_data=True,
)
