from mypackage import myModule

def test_top_n():
    """
    make sure top n works correctly
    """
    
    assert myModule.top_n([8,3,6,2,5,3,9,0,4,1,7], 4) = [9,8,7,5], 'Incorrect'
    assert myModule.top_n([8,3,6,2,5,3,9,0,4,1], ) = [9,8,6], 'Incorrect'
    assert myModule.top_n([8,3,6,2,5,3,0,4,1,7], 5) = [8,7,6,5,4], 'Incorrect'