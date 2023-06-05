from StackAndQueue.stackqueuebrackets.brackets import validate_brackets


def test_1():
    first = validate_brackets('{lEENA}')
    actual = first
    assert actual == first

def test_2():
    second = validate_brackets('{}(LeeNa){}')
    actual = second
    assert actual == second

def test_3():
    third = validate_brackets('()[[Extra Characters]]')
    actual = third
    assert actual == third

def test_4():
    fourth = validate_brackets('(){}[[Leena]]')
    actual = fourth
    assert actual == fourth

def test_5():
    fifth = validate_brackets('{}{Code}[LeeNa](())')
    actual = fifth
    assert actual == fifth

def test_6():
    sixth = validate_brackets('[({LeeNa}]')
    actual = sixth
    assert actual == sixth

def test_7():
    seventh = validate_brackets('(](')
    actual = seventh
    assert actual == seventh

def test_8():    
    eighth = validate_brackets('{(})')
    actual = eighth
    assert actual == eighth







