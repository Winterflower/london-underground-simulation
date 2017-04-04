"""
Author: Camilla Montonen
Description: Tests for lib/commuter.py
"""

import unittest2
import sys
from src.lib.commuter import Commuter
from mock import MagicMock

class TestCommuterProperties(unittest2.TestCase):
    def setUp(self):
        self.mock_source = MagicMock()
        self.mock_dest = MagicMock()
        self.env = MagicMock()
        self.id_number = 1
        self.mock_request = MagicMock(type='request')
        self.mock_train = MagicMock(space=MagicMock(req=lambda *args, **kwargs: self.mock_request))
        self.commuter = Commuter(self.id_number, self.mock_source, self.mock_dest, self.env)

    def test_commuter_initialisation(self):
        self.assertEquals(self.commuter.id_number,self.id_number)

    def test_request_train_space(self):
        gen_object = self.commuter.request_train_space(self.mock_train)
        self.assertTrue( gen_object.next().type, self.mock_request.type)


