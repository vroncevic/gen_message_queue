# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenMessageQueueBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_message_queue.setup.keys import GenMessageQueueBundleKeys


class TestGenMessageQueueBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenMessageQueueBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenMessageQueueBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenMessageQueueBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenMessageQueueBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenMessageQueueBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenMessageQueueBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenMessageQueueBundleKeys.OPTION_INFO_FILE, opts)
