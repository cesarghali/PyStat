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
            Case([1.5, 4.7, 24, 8.5], 4)
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
            Case([1.5, 4.7, 24, 8.5], 9.675)
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
                self.assertEqual(runningStat.mean(), case.mean)


    def test_variance(self):
        Case = namedtuple("Case", "array variance")
        cases = [
            Case([], float("nan")),
            Case([1], float("nan")),
            Case([1, 1], 0),
            Case([1, 1, 1], 0),
            Case([1, 2, 3, 4, 5], 2.5),
            Case([1.5, 4.7, 24, 8.5], 99.38916666666665)
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
                self.assertEqual(runningStat.variance(), case.variance)


    def test_stdev(self):
        Case = namedtuple("Case", "array stdev")
        cases = [
            Case([], float("nan")),
            Case([1], float("nan")),
            Case([1, 1], 0),
            Case([1, 1, 1], 0),
            Case([1, 2, 3, 4, 5], 1.5811388300841898),
            Case([1.5, 4.7, 24, 8.5], 9.969411550671717)
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
                self.assertEqual(runningStat.stdev(), case.stdev)


    def test_sum(self):
        Case = namedtuple("Case", "array sum")
        cases = [
            Case([], 0),
            Case([1], 1),
            Case([1, 1], 2),
            Case([1, 1, 1], 3),
            Case([1, 2, 3, 4, 5], 15),
            Case([1.5, 4.7, 24, 8.5], 38.7)
        ]

        # Calculating the sum using the pystat module.
        for case in cases:
            runningStat = RunningStat()

            # Push all elements.
            for element in case.array:
                runningStat.push(element)

            # Ensure that the sum is as expected.
            self.assertEqual(runningStat.sum(), case.sum)


    def test_min(self):
        Case = namedtuple("Case", "array min")
        cases = [
            Case([], float("nan")),
            Case([1], 1),
            Case([1, 1], 1),
            Case([1, 1, 1], 1),
            Case([1, 2, 3, 4, 5], 1),
            Case([1.5, 4.7, 24, 8.5], 1.5)
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
            Case([1.5, 4.7, 24, 8.5], 24)
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
