import Lab2 as lab2

print("Test_Lab2")


def test_find_min_max():
    input = [5.0, 3.0, 2.0, 4.0, 1.0]
    result = lab2.find_min_max(input)

    assert (result == [1.0, 5.0])
    
def test_calc_average():
    input = [5.0, 3.0, 2.0, 4.0, 1.0]
    result = lab2.calc_average(input)

    assert (result == 3.0)

def test_calc_median_temperature():
    input = [5.0, 3.0, 2.0, 4.0, 1.0]
    result = lab2.sort_temperature(input)
    result = lab2.calc_median_temperature(result)

    assert (result == 3.0)