import sys

#
# Add two values and return the result. If either value is less than
# 0 then an assertion error will arise.
#
def sum(a, b):
    assert a >= 0
    assert b >= 0
    return a + b

if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print "Summing %d and %d" % (a, b),
    c = sum(a, b)
    print " to get %d\n" % c
