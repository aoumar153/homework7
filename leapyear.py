import unittest
import l
def test_leapyear():
    s = 2004
    assert l.leap(s) == 'This is a leap year'
def test_p():
    s = 20001
    assert l.leap(s) == 'not a leap year'

def test_p():
    s = '2340'
    assert l.leap(s) == 'error'

