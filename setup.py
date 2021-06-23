#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     setup.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_message_queue is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as published
     by the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_message_queue is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define setup for tool gen_message_queue.
"""

from __future__ import print_function
import sys
from os.path import abspath, dirname, join, exists
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, https://vroncevic.github.io/gen_message_queue'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_message_queue/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    '''
        Return the installation directory, or None.

        :return: path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(sys.version_info[0], sys.version_info[1])
    if '--github' in sys.argv:
        index = sys.argv.index('--github')
        sys.argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(sys.prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(sys.prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                sys.prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                sys.prefix, py_version
            )
        ))
    message = None
    for path in paths:
        message = '[setup] check path {0}'.format(path)
        print(message)
        if exists(path):
            message = '[setup] use path {0}'.format(path)
            print(message)
            return path
    message = '[setup] no installation path found, check {0}\n'.format(
        sys.prefix
    )
    print(message)
    return None

INSTALL_DIR = install_directory()
TOOL_DIR = 'gen_message_queue/'
if not bool(INSTALL_DIR):
    print('[setup] force exit from install process')
    sys.exit(127)
THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()
PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = ['2.7', '3', '3.2', '3.3', '3.4']
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]
LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0} {1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]
PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_message_queue',
    version='1.0.0',
    description='Generating Message Queue',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_message_queue',
    license='GPL 2018 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, Message Queue, Modules',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=[
        'gen_message_queue', 'gen_message_queue.pro',
        'gen_message_queue.pro.config'
    ],
    install_requires=['ats-utilities'],
    package_data = {
        'gen_message_queue': [
            'conf/gen_message_queue.cfg',
            'conf/gen_message_queue_util.cfg',
            'conf/project.yaml',
            'conf/template/mq_posix/mq_posix.template',
            'conf/template/mq_posix/mq_posix_close.template',
            'conf/template/mq_posix/mq_posix_fatal_error.template',
            'conf/template/mq_posix/mq_posix_open.template',
            'conf/template/mq_posix/mq_posix_open_mode.template',
            'conf/template/mq_posix/mq_posix_receive.template',
            'conf/template/mq_posix/mq_posix_send.template',
            'conf/template/mq_posix/mq_posix_unlink.template',
            'conf/template/mq_sysv/mq_sysv.template',
            'conf/template/mq_sysv/mq_sysv_control.template',
            'conf/template/mq_sysv/mq_sysv_file_to_key.template',
            'conf/template/mq_sysv/mq_sysv_get_buffer.template',
            'conf/template/mq_sysv/mq_sysv_get_buffer_type.template',
            'conf/template/mq_sysv/mq_sysv_key_to_id.template',
            'conf/template/mq_sysv/mq_sysv_receive.template',
            'conf/template/mq_sysv/mq_sysv_send.template',
            'conf/template/mq_sysv/mq_sysv_set_buffer.template',
            'conf/template/mq_sysv/mq_sysv_set_buffer_type.template',
            'log/gen_message_queue.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            '{0}{1}'.format(TOOL_DIR, 'run/gen_message_queue_run.py')
        ]
    )]
)