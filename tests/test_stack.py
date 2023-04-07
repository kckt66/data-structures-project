"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack

stack = Stack()


class TestStack(unittest.TestCase):
    def test_stack(self):
        self.assertEqual(stack.push('data'), None)
        stack.push('data')
        self.assertEqual(stack.pop(), 'data')
