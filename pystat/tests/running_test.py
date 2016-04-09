import unittest
import math
import statistics as stat

from collections import namedtuple

from pystat.running import RunningStat

class RunningStatTest(unittest.TestCase):
    def test_count(self):
        Case = namedtuple("Case", "array count")
        cases = [
            Case([], 0),
            Case([1], 1),
            Case([1, 1], 2),
            Case([1, 1, 1], 3),
            Case([1, 2, 3, 4, 5], 5),
            Case([1.5, 4.7, 24, 8.5], 4),
            Case([-34, 5, 3.6, -104.95, 67.4], 5)
        ]

        # Calculating the mean using the pystat module.
        for case in cases:
            runningStat = RunningStat()

            # Push all elements.
            for element in case.array:
                runningStat.push(element)

            # Ensure that the count is as expected.
            self.assertEqual(runningStat.count(), case.count)


    def test_mean(self):
        Case = namedtuple("Case", "array mean")
        cases = [
            Case([], float("nan")),
            Case([1], 1),
            Case([1, 1], 1),
            Case([1, 1, 1], 1),
            Case([1, 2, 3, 4, 5], 3),
            Case([1.5, 4.7, 24, 8.5], 9.675),
            Case([-34, 5, 3.6, -104.95, 67.4], -12.59)
        ]

        # Calculating the mean using the pystat module.
        for case in cases:
            runningStat = RunningStat()

            # Push all elements.
            for element in case.array:
                runningStat.push(element)

            # Ensures that both numbers are either NaNs or not NaNs.
            self.assertEqual(math.isnan(runningStat.mean()),
                             math.isnan(case.mean))
            # If the mean is not a NaN compare it to the expected mean.
            if not math.isnan(runningStat.mean()):
                precision = 0
                if "." in str(case.mean):
                    precision = len(str(case.mean).split(".")[1])
                self.assertEqual(round(runningStat.mean(), precision),
                                 round(case.mean, precision))


    def test_variance(self):
        Case = namedtuple("Case", "array variance")
        cases = [
            Case([], float("nan")),
            Case([1], float("nan")),
            Case([1, 1], 0),
            Case([1, 1, 1], 0),
            Case([1, 2, 3, 4, 5], 2.5),
            Case([1.5, 4.7, 24, 8.5], 99.38916666666665),
            Case([-34, 5, 3.6, -104.95, 67.4], 3989.6705)
        ]

        # Calculating the variance using the pystat module.
        for case in cases:
            runningStat = RunningStat()

            # Push all elements.
            for element in case.array:
                runningStat.push(element)

            # Ensures that both numbers are either NaNs or not NaNs.
            self.assertEqual(math.isnan(runningStat.variance()),
                             math.isnan(case.variance))
            # If the variance is not a NaN compare it to the expected variance.
            if not math.isnan(runningStat.variance()):
                precision = 0
                if "." in str(case.variance):
                    precision = len(str(case.variance).split(".")[1])
                self.assertEqual(round(runningStat.variance(), precision),
                                 round(case.variance, precision))


    def test_stdev(self):
        Case = namedtuple("Case", "array stdev")
        cases = [
            Case([], float("nan")),
            Case([1], float("nan")),
            Case([1, 1], 0),
            Case([1, 1, 1], 0),
            Case([1, 2, 3, 4, 5], 1.5811388300841898),
            Case([1.5, 4.7, 24, 8.5], 9.969411550671717),
            Case([-34, 5, 3.6, -104.95, 67.4], 63.16384)
        ]

        # Calculating the stdev using the pystat module.
        for case in cases:
            runningStat = RunningStat()

            # Push all elements.
            for element in case.array:
                runningStat.push(element)

            # Ensures that both numbers are either NaNs or not NaNs.
            self.assertEqual(math.isnan(runningStat.stdev()),
                             math.isnan(case.stdev))
            # If the stdev is not a NaN compare it to the expected stdev.
            if not math.isnan(runningStat.stdev()):
                precision = 0
                if "." in str(case.stdev):
                    precision = len(str(case.stdev).split(".")[1])
                self.assertEqual(round(runningStat.stdev(), precision),
                                 round(case.stdev, precision))


    def test_sum(self):
        Case = namedtuple("Case", "array sum")
        cases = [
            Case([], 0),
            Case([1], 1),
            Case([1, 1], 2),
            Case([1, 1, 1], 3),
            Case([1, 2, 3, 4, 5], 15),
            Case([1.5, 4.7, 24, 8.5], 38.7),
            Case([-34, 5, 3.6, -104.95, 67.4], -62.95)
        ]

        # Calculating the sum using the pystat module.
        for case in cases:
            runningStat = RunningStat()

            # Push all elements.
            for element in case.array:
                runningStat.push(element)

            # Ensure that the sum is as expected.
            precision = 0
            if "." in str(case.sum):
                precision = len(str(case.sum).split(".")[1])
            self.assertEqual(round(runningStat.sum(), precision),
                             round(case.sum, precision))


    def test_min(self):
        Case = namedtuple("Case", "array min")
        cases = [
            Case([], float("nan")),
            Case([1], 1),
            Case([1, 1], 1),
            Case([1, 1, 1], 1),
            Case([1, 2, 0], 0),
            Case([1, 2, 3, 4, 5], 1),
            Case([1.5, 4.7, 24, 8.5], 1.5),
            Case([-34, 5, 3.6, -104.95, 67.4], -104.95)
        ]

        # Calculating the min using the pystat module.
        for case in cases:
            runningStat = RunningStat()

            # Push all elements.
            for element in case.array:
                runningStat.push(element)

            # Ensures that both numbers are either NaNs or not NaNs.
            self.assertEqual(math.isnan(runningStat.min()),
                             math.isnan(case.min))
            # If the min is not a NaN compare it to the expected min.
            if not math.isnan(runningStat.min()):
                self.assertEqual(runningStat.min(), case.min)


    def test_max(self):
        Case = namedtuple("Case", "array max")
        cases = [
            Case([], float("nan")),
            Case([1], 1),
            Case([1, 1], 1),
            Case([1, 1, 1], 1),
            Case([1, 2, 3, 4, 5], 5),
            Case([1.5, 4.7, 24, 8.5], 24),
            Case([-34, 5, 3.6, -104.95, 67.4], 67.4)
        ]

        # Calculating the max using the pystat module.
        for case in cases:
            runningStat = RunningStat()

            # Push all elements.
            for element in case.array:
                runningStat.push(element)

            # Ensures that both numbers are either NaNs or not NaNs.
            self.assertEqual(math.isnan(runningStat.max()),
                             math.isnan(case.max))
            # If the max is not a NaN compare it to the expected max.
            if not math.isnan(runningStat.max()):
                self.assertEqual(runningStat.max(), case.max)


if __name__ == '__main__':
    unittest.main()
