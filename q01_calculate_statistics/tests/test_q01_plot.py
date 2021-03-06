import numpy
from inspect import getargspec
from unittest import TestCase
from ..build import calculate_statistics


class TestLoad_distplot(TestCase):
    def test_calculate_statistics(self):  # Input parameters tests
        args = getargspec(calculate_statistics)
        self.assertEqual(len(args[0]), 0, "Expected arguments %d, Given %d" % (0, len(args[0])))

    def test_calculate_statistics_default(self): # Input parameters defaults
        args = getargspec(calculate_statistics)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_calculate_statistics_mean_type(self):  # Return type tests
        mean, median, mode = calculate_statistics()
        self.assertIsInstance(mean, float, "Expected data type for mean is float you are returning %s" % (type(mean)))

    def test_calculate_statistics_median_type(self):
        mean, median, mode = calculate_statistics()
        self.assertIsInstance(median, float,
                              "Expected data type for median is float you are returning %s" % (type(median)))

    def test_calculate_statistics_mode_type(self):  # Return type tests
        mean, median, mode = calculate_statistics()
        self.assertIsInstance(mode, numpy.int64,
                              "Expected data type for mode is numpy.int64 you are returning %s" % (type(mode)))


    def test_calculate_statistics_mean_values(self):  # Return value tests
        mean, median, mode = calculate_statistics()
        self.assertAlmostEqual(mean, 185479.51124002901, 2, "Return `mean` value does not match expected value")

    def test_calculate_statistics_median_values(self):  # Return value tests
        mean, median, mode = calculate_statistics()
        self.assertAlmostEqual(median, 167500.0, 1, "Return `median` value does not match expected value")

    def test_calculate_statistics_mode_values(self):  # Return value tests
        mean, median, mode = calculate_statistics()
        self.assertAlmostEqual(mode, 140000, "Return `mode` value does not match expected value")
