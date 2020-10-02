"""pyvesync setup script."""

from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyvesync',
    version='1.2.0',
    description='pyvesync is a library to manage Etekcity\
                 Devices and Levoit Air Purifier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/markperdue/pyvesync',
    author='Mark Perdue',
    author_email='markaperdue@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['iot', 'vesync'],
    packages=find_packages('src',exclude=['tests','tests.*']),
    package_dir={'': "src"},
    zip_safe=False,
    install_requires=['requests>=2.20.0'],
    python_requires='>=3.5',
)
