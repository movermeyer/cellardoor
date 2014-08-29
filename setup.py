import io
import os.path
from setuptools import setup, find_packages

execfile(os.path.join('hammock', 'version.py'))

setup(
	name='hammock',
	version=__version__,
	description='Create ReST APIs from mongoengine documents.',
	long_description=io.open('README.rst', 'r', 'utf-8'),
	classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='wsgi web api framework rest http cloud mongodb mongoengine',
    author='Elisha Fitch-Cook',
    author_email='elisha@cooper.com',
    url='http://github.com/cooper-software/hammock',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['falcon', 'mongoengine'],
    test_suite='nose.collector'
)