from os import path
from os.path import join, abspath, dirname
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    readme = f.read()

with open(join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(join(abspath(dirname(__file__)), "VERSION"), "r") as v:
    VERSION = v.read().replace("\n", "")

setup(
    name='crawlino-core',
    version=VERSION,
    packages=find_packages(),
    long_description=readme,
    install_requires=required,
    include_package_data=True,
    url='https://github.com/crawlino/crawlino-core',
    license='BSD3',
    author='Daniel Garcia (cr0hn)',
    author_email='hello[-at-]crawlino.org',
    description='Core module for Crawlino',
    classifiers=[
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
    ],
)

