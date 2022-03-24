# -*- coding: utf-8 -*-

from .context import cro-geneea-client

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

class ProjectTestSuite(unittest.TestCase):
    """project test cases."""

    def test_hello(self):
        cro-geneea-client.hello()


if __name__ == '__main__':
    unittest.main()