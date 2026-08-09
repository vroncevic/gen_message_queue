# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_message_queue is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_message_queue is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Encapsulates core gen_message_queue components for simplification of gen_message_queue bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_message_queue.core.service.iservice import IService
from gen_message_queue.core.service.isubprocessor import ISubProcessor
from gen_message_queue.infrastructure.cli.icli import ICLI
from gen_message_queue.setup.bundle import GenMessageQueueBundle
from gen_message_queue.setup.validator import GenMessageQueueBundleValidator
from gen_message_queue.setup.keys import GenMessageQueueBundleKeys
from gen_message_queue.setup.dependencies import GenMessageQueueBundleDependencies
from gen_message_queue.setup.dep_validator import GenMessageQueueBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_message_queue'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_message_queue/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenMessageQueueBundleRegistry:
    '''
        Encapsulates core gen_message_queue components for simplification of gen_message_queue bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_message_queue bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenMessageQueueBundleDependencies) -> GenMessageQueueBundle:
        '''
            Creates the gen_message_queue bundle.

            :param dependencies: The gen_message_queue bundle dependencies.
            :return: The gen_message_queue bundle.
            :exceptions:
                | ATSValueError: The gen_message_queue bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_message_queue bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_message_queue bundle must be provided and have proper values.
                | ATSTypeError:  The gen_message_queue bundle must be an instance of GenMessageQueueBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenMessageQueueBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenMessageQueueBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenMessageQueueBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenMessageQueueBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenMessageQueueBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenMessageQueueBundle = GenMessageQueueBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenMessageQueueBundleValidator.validate(bundle)

        return bundle
