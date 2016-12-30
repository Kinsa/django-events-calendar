from setuptools import setup, find_packages


setup(
    name='django-events',
    version='1.0.3',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'Pillow>=3.1.1',
        'sorl-thumbnail>=3.2.5',
        'Django>=1.8'
    ],
    author='Joe Bergantine',
    author_email='jbergantine@gmail.com',
    description="Simple Upcoming Events Calendar for Django",
    url='https://github.com/jbergantine/django-events',
    download_url='https://github.com/jbergantine/django-events/tarball/1.0.3',
    license='New BSD License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
    test_suite="runtests.runtests",
    include_package_data=True,
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='readme.md',
)
