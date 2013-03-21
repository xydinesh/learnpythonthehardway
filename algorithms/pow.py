"""
Dinesh Weerapurage
03/20/2012
Compute power n of a number.
"""
import cProfile as cp

class Power(object):
    """
    Naive power algorithm
    """
    def __init__(self):
        self.x = 501
        self.n = 100000
        
    def run(self):
        print "%s^%s" % (self.x, self.n)
        y = 1;
        for i in xrange(0, self.n):
            y = y * self.x
        # print "sol: %s" % y


class DC(object):
    """
    Divide and conqure algorithm
    """
    def _x(self, n):
        if n == 1:
            return self.x

        v = 1
        if n % 2 == 0:
            v = self._x(n/2)
            return v*v;
        else:
            v = self._x((n-1)/2)
            return self.x*v*v

    def run(self):
        print "%s^%s" % (self.x, self.n)
        y = self._x(self.n)
        # print "sol: %s" % y


if __name__ == "__main__":
    p = Power()
    cp.run('p.run()')
    
    d = DC()
    cp.run('d.run()')
