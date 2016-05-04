import math


# RunningStat provides statistical computations on a running stream of values.
# The set of values is never stored.
class RunningStat:
    def __init__(self):
        self.__mean = float("nan")
        self.__count = 0.0
        self.__vsum = float("nan")
        self.__min = float("nan")
        self.__max = float("nan")

    # push adds a new elements to the set on which the statistical computation
    # is carried.
    def push(self, value):
        # Pushing the first element.
        if math.isnan(self.__mean):
            self.__mean = float(value)
            self.__count = 1
            self.__vsum = 0
            self.__min = float(value)
            self.__max = float(value)
        # Pushing the rest of the elements.
        else:
            # Update count.
            self.__count = self.__count + 1
            # Update mean and variance sum.
            tmp = self.__mean + (float(value) - self.__mean) / self.__count
            self.__vsum = self.__vsum + (float(value) -
                                       self.__mean) * (value - tmp)
            self.__mean = tmp
            # Update min and max.
            if value < self.__min:
                self.__min = float(value)
            if value > self.__max:
                self.__max = float(value)


    # count returns the number of elements.
    def count(self):
        return self.__count


    # mean returns the average of the pushed elements.
    def mean(self):
        if self.__count < 1:
            return float("nan")
        else:
            return self.__mean


    # variance returns the variance of the pushed elements.
    def variance(self):
        if self.__count < 2:
            return float("nan")
        else:
            return self.__vsum / (self.__count - 1)


    # stdev returns the standard deviation of the pushed elements.
    def stdev(self):
        return math.sqrt(self.variance())


    # sum returns the sum of the pushed elements.
    def sum(self):
        if math.isnan(self.mean()):
            return 0.0
        else:
            return self.mean() * self.__count


    # min returns the smallest of the pushed elements.
    def min(self):
        return self.__min


    # max returns the largest of the pushed elements.
    def max(self):
        return self.__max


    # all return all statistical data.
    def all(self):
        result = {}
        result["count"] = self.count()
        result["mean"] = self.mean()
        result["variance"] = self.variance()
        result["stdev"] = self.stdev()
        result["sum"] = self.sum()
        result["min"] = self.min()
        result["max"] = self.max()
        return result
