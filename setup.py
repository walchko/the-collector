##############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import print_function
from setuptools import setup
# from the_collector import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution
from build_utils import SetGitTag
from build_utils import get_pkg_version

VERSION = get_pkg_version('the_collector/__init__.py')
PACKAGE_NAME = 'the_collector'
BuildCommand.pkg = PACKAGE_NAME
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION
SetGitTag.version = VERSION


setup(
    author='Kevin Walchko',
    author_email='walchko@users.noreply.github.com',
    name=PACKAGE_NAME,
    version=VERSION,
    description='A library to store robot data in a json file',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/MomsFriendlyRobotCompany/{}'.format(PACKAGE_NAME),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
    license='MIT',
    keywords=['library', 'robotics', 'robot'],
    packages=[PACKAGE_NAME],
    install_requires=[
        'build_utils',
        'msgpack'
    ],
    extras_require={
        'numpy': ["numpy"],
        'simplejson': ["simplejson"]
    },
    cmdclass={
        'publish': PublishCommand,
        'make': BuildCommand,
        'tag': SetGitTag
    },
    # scripts=[
    #     'bin/set_id.py',
    #     'bin/servo_ping.py',
    #     'bin/set_angle.py',
    #     'bin/set_baud_rate.py',
    #     'bin/servo_reboot.py',
    #     'bin/servo_reset.py',
    #     'bin/get_angle.py'
    # ]
)
