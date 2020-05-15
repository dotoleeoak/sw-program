from unittest.case import TestCase
from subprocess import PIPE, run
from main import tokenize, build_index, main
import pytest

class MyTest(TestCase):
    def test1(self):
        tokenize("1342-0.txt")
        with open("word-count.txt", 'r') as f1:
            w1 = f1.readlines()
        with open("test/word-count.txt", 'r') as f2:
            w2 = f2.readlines()
        self.assertEqual(w1, w2)

    def test2(self):
        build_index(5)
        with open("index.txt", 'r') as f1:
            w1 = f1.readlines()
        with open("test/index.txt", 'r') as f2:
            w2 = f2.readlines()
        self.assertEqual(w1[1:], w2[1:])

    def test3(self):
        command = 'act fil ab'
        result = main(command)
        ans = [['actually', 'act', 'acted', 'actions', 'active'],
                ['file', 'files', 'filial', 'fill', 'filled'],
                ['about', 'able', 'absence', 'above', 'absolutely']]
        self.assertEqual(ans, result)
