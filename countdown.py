__author__ = 'chenliang'

class Countdown(object):
    def __init__(self, n):
        self.n = n;

    def __iter__(self):
        return self;

    def next(self):
        if(self.n < 0):
            raise StopIteration;

        r = self.n;
        self.n = self.n - 1;
        return r;

for x in Countdown(19):
    print x

