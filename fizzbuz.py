import unittest
import f
def test_fizz(capsys):
    f.fizz()
    
    # Capture stdout so that we can check for things in tests
    # We'll get an array that contains each line in the output (the -1 is to deal with the trailing newline)
    output = capsys.readouterr().out.split('\n')[:-1]
    for i in range(len(output)):
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
                
def test_buzz(capsys):
    f.fizz()
    output = capsys.readouterr().out.split('\n')[:-1]
    for i in range(len(output)):
        if((i+1) % 3 == 0) :
            if ((i+1) % 5 == 0 ):
                assert output[i] == 'FizzBuzz'
            else :
                assert output[i] == 'Fizz'
        else: 
            if((i+1) % 5 == 0):
                assert output[i] == 'Buzz'
            else:
                assert output[i] == i+1
