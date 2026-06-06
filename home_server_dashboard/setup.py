"""
    This package represents is responsible
     for creating a dashboard web app used
     for my home server.
"""

from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'This is the home_server_dashboard module.'
LONG_DESCRIPTION = (
    'This is a web application that contains '
    'a dashboard web page for my home server.'
)
AUTHOR = 'Andrei Draghici'
AUTHOR_EMAIL = 'draghici.andrei12@yahoo.com'

setup(
    name='home_server_dashboard_draghici_andrei',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Andrei Draghici',
    author_email='draghici.andrei12@yahoo.com',
    url='https://github.com/draghiciandrei1307/home-server-dashboard',
    packages=find_packages(),
    install_requires=[
        'flask'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'run_server=home_server_dashboard.home_server_dashboard:main'
        ]
    }

)
