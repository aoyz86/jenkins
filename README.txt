
Simple Python and nosetests Example
===================================

Prerequisites
=============

Python 2.4+
-----------

Check if it is installed already
$ python --version
Python 2.7.1+

If not, then see
http://wiki.python.org/moin/BeginnersGuide/Download

nosetests
---------

Check if it is installed already
$ nosetests
----------------------------------------------------------------------
Ran 0 tests in 0.006s

OK
 
If not, then see
http://nose.readthedocs.org
http://pypy.python.org/pypy/nose

Use
===

Run
$ python src/sum.py 1 2
Summing 1 and 2 to get 3

Run tests
$ nosetests --with-xunit
..
----------------------------------------------------------------------
Ran 2 tests in 0.009s

OK

View results
$ more nosetests.xml
<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="nosetests" tests="2" errors="0" failures="0" skip="0">
<testcase classname="test_sum.TestSum" name="test_sum01" time="0" />
<testcase classname="test_sum.TestSum" name="test_sum10" time="0" />
</testsuite>

Copyright and contact
=====================

Mike Jackson - info@software.ac.uk

Copyright (c) The University of Edinburgh, 2012.
