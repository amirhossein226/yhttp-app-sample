import re
from os.path import join, dirname

from setuptools import setup, find_namespace_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'yhttp/bee/__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S).\
        match(v_file.read()).group(1)


dependencies = [
    'yhttp >= 6.3.1, < 7',
    'yhttp-pony',
]


setup(
    name='bee',
    version=package_version,
    install_requires=dependencies,
    license='',
    url='https://github.com/yhttp/yhttp-boilerplate',
    author='amirhossein226',
    packages=find_namespace_packages(
        where='.',
        include=['yhttp.bee'],
        exclude=['tests']
    ),
    entry_points={
        'console_scripts': [
            'bee = yhttp.bee:app.climain'
        ]
    },
)
