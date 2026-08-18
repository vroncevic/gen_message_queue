# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenMessageQueueBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_message_queue.setup.opt_validator import GenMessageQueueBundleOptionsValidator


class TestGenMessageQueueBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenMessageQueueBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenMessageQueueBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenMessageQueueBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenMessageQueueBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenMessageQueueBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenMessageQueueBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenMessageQueueBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenMessageQueueBundleOptionsValidator.is_valid({'info_file': 123}))
