"""
Author: Camilla Montonen
Description: Tests for lib/commuter.py
"""

import unittest2
import sys
from src.lib.commuter import Commuter
from mock import MagicMock

class TestCommuterProperties(unittest2.TestCase):
    def test_commuter_initialisation(self):
        mockSource = MagicMock()
        mockDest = MagicMock()
        id_number = 1
        commuter = Commuter(id_number,mockSource,mockDest)
        self.assertEquals(commuter.id_number,id_number)


