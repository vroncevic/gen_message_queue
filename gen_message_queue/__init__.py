# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2018 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    GenMessageQueue is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    GenMessageQueue is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class GenMessageQueue with attribute(s) and method(s).
    Loads a base info, creates an CLI interface and runs operations.
'''

import sys
from typing import Any, List, Dict
from argparse import Namespace
from os.path import exists, dirname, realpath

try:
    from ats_utilities.splash import Splash
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_message_queue.pro import MessageQueue
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_message_queue'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_message_queue/blob/dev/LICENSE'
__version__ = '1.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenMessageQueue(CfgCLI):
    '''
        Defines class GenMessageQueue with attribute(s) and method(s).
        Loads a base info, creates an CLI interface and runs operations.

        It defines:

            :attributes:
                | __GEN_VERBOSE - Console text indicator for process-phase.
                | _CONFIG - Tool info file path.
                | _LOG - Tool log file path.
                | _LOGO - Logo for splash screen.
                | _OPS - List of tool options.
                | _logger - Logger object API.
            :methods:
                | __init__ - Initials GenMessageQueue constructor.
                | process - Processes and runs operations.
    '''

    _GEN_VERBOSE: str = 'GEN_MESSAGE_QUEUE'
    _CONFIG: str = '/conf/gen_message_queue.cfg'
    _LOG: str = '/log/gen_message_queue.log'
    _LOGO: str = '/conf/gen_message_queue.logo'
    _OPS: List[str] = [
        '-g', '--gen', '-t', '--type', '-v', '--verbose', '--version'
    ]

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir: str = dirname(realpath(__file__))
        gen_autoconf_property: Dict[str, str | bool] = {
            'ats_organization': 'vroncevic',
            'ats_repository': f'{self._GEN_VERBOSE.lower()}',
            'ats_name': f'{self._GEN_VERBOSE.lower()}',
            'ats_logo_path': f'{current_dir}{self._LOGO}',
            'ats_use_github_infrastructure': True
        }
        Splash(gen_autoconf_property, verbose)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(base_info, verbose)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} init tool info']
        )
        self._logger: ATSLogger = ATSLogger(
            self._GEN_VERBOSE.lower(), f'{current_dir}{self._LOG}', verbose
        )
        if self.tool_operational:
            self.add_new_option(
                self._OPS[0], self._OPS[1],
                dest='gen', help='generate driver (provide project name)'
            )
            self.add_new_option(
                self._OPS[2], self._OPS[3],
                dest='type', help='driver type (posix | sysv)'
            )
            self.add_new_option(
                self._OPS[4], self._OPS[5],
                action='store_true', default=False,
                help='activate verbose mode for generation'
            )
            self.add_new_option(
                self._OPS[6], action='version', version=__version__
            )

    def process(self, verbose: bool = False) -> bool:
        '''
            Process and run operation.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False
        if self.tool_operational:
            if len(sys.argv) >= 6:
                options: List[str] = [
                    arg for i, arg in enumerate(sys.argv) if i % 2 == 0
                ]
                if any(arg not in self._OPS for arg in options[1:]):
                    error_message(
                        [
                            f'{self._GEN_VERBOSE.lower()}',
                            'provide name (-g name) and',
                            'type (-t posix | sysv)'
                        ]
                    )
                    self._logger.write_log(
                        'missing model name or type', self._logger.ATS_ERROR
                    )
                    return status
            else:
                error_message(
                    [
                        f'{self._GEN_VERBOSE.lower()}',
                        'provide name (-g name) and',
                        'type (-t posix | sysv)'
                    ]
                )
                self._logger.write_log(
                    'missing model name or type', self._logger.ATS_ERROR
                )
                return status
            args: Any | Namespace = self.parse_args(sys.argv[2:])
            if not exists(getattr(args, 'gen')):
                print(
                    " ".join([
                        f'[{self._GEN_VERBOSE.lower()}]',
                        'gen MSG QUEUE skeleton',
                        str(getattr(args, 'gen'))
                    ])
                )
                generator: MessageQueue = MessageQueue(
                    getattr(args, 'verbose') or verbose
                )
                try:
                    status = generator.gen_setup(
                        f'{getattr(args, "gen")}',
                        f'{getattr(args, "type")}',
                        getattr(args, 'verbose') or verbose
                    )
                except (ATSTypeError, ATSValueError) as e:
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} {str(e)}']
                    )
                    self._logger.write_log(
                        f'{str(e)}', self._logger.ATS_ERROR
                    )
                if status:
                    success_message(
                        [f'{self._GEN_VERBOSE.lower()} done\n']
                    )
                    self._logger.write_log(
                        f'gen pro {getattr(args, "gen")} done',
                        self._logger.ATS_INFO
                    )
                else:
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} generation failed']
                    )
                    self._logger.write_log(
                        'generation failed', self._logger.ATS_ERROR
                    )
            else:
                error_message(
                    [
                        f'{self._GEN_VERBOSE.lower()}',
                        f'project with name [{getattr(args, "gen")}] exists'
                    ]
                )
                self._logger.write_log(
                    f'project with name [{getattr(args, "gen")}] exists',
                    self._logger.ATS_ERROR
                )
        else:
            error_message(
                [f'{self._GEN_VERBOSE.lower()} tool is not operational']
            )
            self._logger.write_log(
                'tool is not operational', self._logger.ATS_ERROR
            )
        return status
