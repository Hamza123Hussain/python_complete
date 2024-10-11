from string_functions import Hello
def test_name():    
    
    assert Hello(name='Hamza')==f'Hi, Hamza'

def test_withoutname():
    assert Hello()=='Hi, hamza'   