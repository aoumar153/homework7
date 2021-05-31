import unittest

def test_fizz(capsys):
    fizzbuzz()
    
    # Capture stdout so that we can check for things in tests
    # We'll get an array that contains each line in the output (the -1 is to deal with the trailing newline)
    output = capsys.readouterr().out.split('\n')[:-1]
    for i in output.len():
        if((i+1) % 3 == 0) :
            if ((i+1) % 5 == 0 ):
                assert output[i] == 'FizzBuzz'
            else :
                assert output[i] == 'Fizz'
        else: 
            if((i+1) % 5 == 0):
                assert output[i] == 'Buzz'
            else:
                s = str(i+1)
                assert output[i] == s
                

