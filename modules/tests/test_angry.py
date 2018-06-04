import modules

def test_angry():
    assert('angry' == modules.process_query('angry')[0])
    assert('angry' == modules.process_query('i am angry')[0])
    assert('angry' == modules.process_query('I can not control my anger.')[0])
