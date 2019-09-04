#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:18:11 2019

@author: vijendertss
"""

import unittest
import checkout

RULES = {
  'A': {'price': 50, 'discount_threshold': 3, 'discount_price': 130},
  'B': {'price': 30, 'discount_threshold': 2, 'discount_price': 45},
  'C': {'price': 20},
  'D': {'price': 15}
}

class TestTotals(unittest.TestCase):
  def setUp(self):
    self.co = checkout.Checkout(RULES)


  def test_three_items_discount(self):
    self.co.add_or_scan('B')
    self.co.add_or_scan('A')
    self.co.add_or_scan('B')
    total = self.co.total()
    self.assertEqual(95, total)


if __name__ == "__main__":
  unittest.main()
