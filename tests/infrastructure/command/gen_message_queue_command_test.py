# -*- coding: UTF-8 -*-

'''
Module
    gen_message_queue_command_test.py
Info
    Unit tests for GenMessageQueueCommandDefinition and GenMessageQueueCommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_message_queue.core.service.iservice import IService
from gen_message_queue.infrastructure.command.gen_message_queue_command_definition import GenMessageQueueCommandDefinition
from gen_message_queue.infrastructure.command.gen_message_queue_command_executor import GenMessageQueueCommandExecutor


class TestGenMessageQueueCommand(unittest.TestCase):

    def test_definition(self) -> None:
        definition = GenMessageQueueCommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertEqual(definition.help_text, 'Generate MessageQueue project skeleton')
        self.assertEqual(len(definition.options), 3)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = GenMessageQueueCommandDefinition()
        executor = GenMessageQueueCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}
        
        params = {'name': 'test', 'output': '.'}
        result = executor.execute(params=params, service=mock_service)
        
        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = GenMessageQueueCommandDefinition()
        executor = GenMessageQueueCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False
        
        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = GenMessageQueueCommandDefinition()
        executor = GenMessageQueueCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))
