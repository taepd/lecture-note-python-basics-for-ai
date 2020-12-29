# -*- coding: utf8 -*-

import unittest
import basic_math as bm


class TestBasicMath(unittest.TestCase):
    def test_get_greatest(self):
        for _ in range(10):
            random_number_list = random.sample(range(1, 100), 10)
            pred = bm.get_greatest(random_number_list)
            real = self.get_greatest(random_number_list)
            self.assertEqual(pred, real)

    def get_greatest(self, number_list):
        return sorted(number_list)[-1]
