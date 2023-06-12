from StackAndQueue.stackqueuebrackets.brackets import validate_brackets


def test_1():
    expected = True
    actual = validate_brackets('{lEENA}')
    assert actual == expected

def test_2():
    expected = True
    actual = validate_brackets('{}(LeeNa){}')
    assert actual == expected

def test_3():
    expected = True
    actual = validate_brackets('()[[Extra Characters]]')
    assert actual == expected

def test_4():
    expected = True
    actual = validate_brackets('(){}[[Leena]]')
    assert actual == expected

def test_5():
    expected = True
    actual = validate_brackets('{}{Code}[LeeNa](())')
    assert actual == expected

def test_6():
    expected = False
    actual = validate_brackets('[({LeeNa}]')
    assert actual == expected

def test_7():
    expected = False
    actual = validate_brackets('(](')
    assert actual == expected

def test_8():    
    expected = False
    actual = validate_brackets('{(})')
    assert actual == expected
