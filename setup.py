try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'Project URL',
    'download_url': 'DL URL',
    'author_emal': 'me@domain.com',
    'version': '0.0.1',
    'install_requires': [ 'nose' ],
    'packages': [ 'NAME' ],
    'scripts': [],
    'name': 'projectname'
}

setup( **config )
