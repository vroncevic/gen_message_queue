#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2018 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_message_queue is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_message_queue is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines setup for tool gen_message_queue.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_message_queue'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_message_queue/blob/dev/LICENSE'
__version__: str = '1.1.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR = 'gen_message_queue/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11', '3.12']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS
setup(
    name='gen_message_queue',
    version='1.1.6',
    description='Generating Message Queue',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_message_queue',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, Message Queue, Modules',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_message_queue', 'gen_message_queue.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_message_queue': [
            'py.typed',
            f'{CONF}/gen_message_queue.logo',
            f'{CONF}/gen_message_queue.cfg',
            f'{CONF}/gen_message_queue_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/posix/mq_posix.template',
            f'{TEMPLATE}/posix/mq_posix_close.template',
            f'{TEMPLATE}/posix/mq_posix_fatal_error.template',
            f'{TEMPLATE}/posix/mq_posix_open.template',
            f'{TEMPLATE}/posix/mq_posix_open_mode.template',
            f'{TEMPLATE}/posix/mq_posix_receive.template',
            f'{TEMPLATE}/posix/mq_posix_send.template',
            f'{TEMPLATE}/posix/mq_posix_unlink.template',
            f'{TEMPLATE}/sysv/mq_sysv.template',
            f'{TEMPLATE}/sysv/mq_sysv_control.template',
            f'{TEMPLATE}/sysv/mq_sysv_file_to_key.template',
            f'{TEMPLATE}/sysv/mq_sysv_get_buffer.template',
            f'{TEMPLATE}/sysv/mq_sysv_get_buffer_type.template',
            f'{TEMPLATE}/sysv/mq_sysv_key_to_id.template',
            f'{TEMPLATE}/sysv/mq_sysv_receive.template',
            f'{TEMPLATE}/sysv/mq_sysv_send.template',
            f'{TEMPLATE}/sysv/mq_sysv_set_buffer.template',
            f'{TEMPLATE}/sysv/mq_sysv_set_buffer_type.template',
            f'{LOG}/gen_message_queue.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_message_queue_run.py'
        ]
    )]
)
