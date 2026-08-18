# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenMessageQueueBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_message_queue.setup.bundle import GenMessageQueueBundle
from gen_message_queue.setup.factory import GenMessageQueueBundleFactory


class TestGenMessageQueueBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenMessageQueueBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenMessageQueueBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_message_queue/infrastructure/config/gen_message_queue.cfg'}
        bundle = GenMessageQueueBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenMessageQueueBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenMessageQueueBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenMessageQueueBundleFactory.get_version(), '1.1.7')
