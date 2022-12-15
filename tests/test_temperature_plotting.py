import pytest, os

import temperature_plotting as tpl

def test_compute_mean():
    calc = tpl.compute_mean([0,10,20])
    assert calc == 10
    assert type(calc) == float

    calc = tpl.compute_mean([-10, 10])
    assert calc == 0
    
    calc = tpl.compute_mean([-10, 10])
    assert calc == 15
    
    calc = tpl.compute_mean([0,10,0])
    assert round(calc,4) == 3.3333, "Check that the average is roughly correct"
    
    with pytest.raises(TypeError) as e:
        calc = tpl.compute_mean(["a", "b", "c"])
    assert not e == None, "We shuold not be able to have strings"    
        
    calc = tpl.compute_mean([])
    assert calc == None  
    
def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")





