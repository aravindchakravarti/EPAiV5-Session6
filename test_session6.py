import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import time
from session5 import squared_power_list
from session5 import polygon_area
from session5 import temp_converter
from session5 import speed_converter

README_CONTENT_CHECK_FOR = [
    'time_it(fn, *args, repetitions= 1, **kwargs)',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

def test_session5_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session5_readme_500_words():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session5_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session5_readme_file_for_more_than_10_hashes():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_session5_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 


def test_session5_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


############################## Assignment Validations###########################

def test_session5_time_it_print():
    ''''
    Test if time_it function can handle python print function also
    '''
    # Define arguments for the print function
    message = "Hello, World!"
    # Call time_it with the built-in print function and arguments
    exec_time = session5.time_it(print, message, repetitions=5)   
    # assert that exec_time is a greater than 1millisecond
    assert exec_time < 0.001, "Execution time is very slow for print function"

def test_session5_time_it_squared_power_list():
    '''
    Test time_it with squared_power_list with arguments.  
    '''
    exec_time = session5.time_it(session5.squared_power_list, number=5, start=0, end=5, repetitions=5)   
    # assert that exec_time is a greater than 100 microsecond
    assert exec_time < 0.0001, "Execution time is very slow for squared_power_list function"


def test_session5_time_it_polygon_area():
    '''
    Test time_it with polygon_area with arguments.  
    '''
    exec_time = session5.time_it(session5.polygon_area, length=10, sides=3, repetitions=10) 
    # assert that exec_time is a greater than 100 microsecond
    assert exec_time < 0.0001, "Execution time is very slow for squared_power_list function"


def test_session5_time_it_temp_converter():
    '''
    Test time_it with temp_converter with arguments.  
    '''
    exec_time = session5.time_it(session5.temp_converter, temp=32, temp_given_in='f', repetitions=100)
    # assert that exec_time is a greater than 200 microsecond
    assert exec_time < 0.0002, "Execution time is very slow for temp_converter function"


def test_session5_time_it_speed_converter():
    '''
    Test time_it with speed_converter with arguments.  
    '''
    exec_time = session5.time_it(session5.speed_converter, speed=3600, dist='m', time='s', repetitions=200)
    # assert that exec_time is a greater than 500 microsecond
    assert exec_time < 0.0005, "Execution time is very slow for speed_converter function"



####################### Validations for time_it#################################

def test_session5_time_it_no_args():
    """ DON'T TOUCH THIS FUNCTION \
        Test time_it with no arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'fn'*"):
        session5.time_it()


def test_session5_time_it_incorrect_pos_args():
    """ DON'T TOUCH THIS FUNCTION \
        Test time_it with non existing positional arguments"""
    with pytest.raises(NameError, match=r".*is not defined*"):
        session5.time_it(unknown_fn,repetitions=1)


def test_session5_time_it_zero_rep():
    """ DON'T TOUCH THIS FUNCTION \
        Test time_it with zero repetation. Should return 0 avg time"""
    assert session5.time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=0) == 0, "time_it should retun 0 for no function call"
    assert session5.time_it(squared_power_list, 2, start=0, end=5, repetitions=0) == 0, "time_it should retun 0 for no function call"
    assert session5.time_it(polygon_area, 15, sides=3, repetitions=0) == 0, "time_it should retun 0 for no function call"
    assert session5.time_it(speed_converter, 100, dist='km', time='min', repetitions=0) == 0, "time_it should retun 0 for no function call"
    assert session5.time_it(temp_converter, 100, temp_given_in = 'f', repetitions=0) == 0, "time_it should retun 0 for no function call"


####################### Validations for squared_power_list()####################

def test_session5_squared_power_list_no_args():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'number'*"):
        session5.squared_power_list()

def test_session5_squared_power_list_incorrect_pos_args():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for incorrect values for positional arguments"""
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        session5.squared_power_list('sac')
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        session5.squared_power_list(1+2j)

def test_session5_squared_power_list_incorrect_start__end():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for incorrect value to start keyword arguments"""
    with pytest.raises(ValueError, match=r".*Value of start or end can't be negative*"):
        session5.squared_power_list(2,start=-1)
    with pytest.raises(ValueError, match=r".*Value of start or end can't be negative*"):
        session5.squared_power_list(2,end=-1)

def test_session5_squared_power_list_start_gt_end():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for start value greater than end"""
    with pytest.raises(ValueError, match=r".*Value of start should be less than end*"):
        session5.squared_power_list(2,start=9,end=1)

def test_session5_squared_power_list_number_gt_10():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for number value greater than 10"""
    with pytest.raises(ValueError, match=r".*Value of number should be less than 10*"):
        session5.squared_power_list(15)

def test_session5_squared_power_list_unwanted_args():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for unwanted positional/keyword arguments"""
    with pytest.raises(TypeError, match=r".*takes maximum 1 positional arguments*"):
        session5.squared_power_list(1,2,start=1, end=5)
    with pytest.raises(TypeError, match=r".*maximum 2 keyword/named arguments*"):
        session5.squared_power_list(1,start=1, end=5, test = 0)

def test_session5_squared_power_list_output():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for output with multiple inputs"""
    assert session5.squared_power_list(1,start=1, end=5) == [1,1,1,1], "squared_power_list is not working as expected"
    assert session5.squared_power_list(2,start=1, end=4) == [2,4,8], "squared_power_list is not working as expected"



####################### Validations for polygon_area()####################
def test_session5_polygon_area():
    """Test polygon_area function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'length'*"):
        session5.polygon_area()

def test_session5_polygon_area_length():
    """Test polygon_area function for incorrect values for positional argument length (check for string AND imaginary input)"""
    with pytest.raises(ValueError, match=r".*polygon_area accepts only int or float*"):
        session5.polygon_area(length='2.2')
    with pytest.raises(ValueError, match=r".*polygon_area accepts only int or float*"):
        session5.polygon_area(length=3.+4j)

def test_session5_polygon_area_sides():
    """Test polygon_area function for incorrect value to sides keyword argument (string "ten" AND img input)"""
    with pytest.raises(ValueError, match=r".*polygon_area accepts only int or float*"):
        session5.polygon_area(length=2, sides = 'ten')
    with pytest.raises(ValueError, match=r".*polygon_area accepts only int or float*"):
        session5.polygon_area(length=2, sides = 3+4j)

def test_session5_polygon_area_sides_values():
    """Test polygon_area function for permissible values for sides, check for 0, 1, 2, 7"""
    with pytest.raises(ValueError, match=r".*sides must be greater than 2*"):
        session5.polygon_area(length = 0.1, sides = 2)
    with pytest.raises(ValueError, match=r".*sides must be greater than 2*"):
        session5.polygon_area(length = 0.1, sides = -1)

def test_session5_polygon_area_length_values():
    """Test polygon_area function for permissible values for sides (len > 0)"""
    with pytest.raises(ValueError, match=r".*lenght must be greater than zero*"):
        session5.polygon_area(length = -0.1)

def test_session5_polygon_area_unwanted_args():
    """DON'T TOUCH THIS FUNCTION \
        Test polygon_area function for unwanted positional/keyword arguments"""
    with pytest.raises(TypeError, match=r".*polygon_area function takes maximum 1 positional arguments, more provided*"):
        session5.polygon_area(1, 2, sides=4)
    with pytest.raises(TypeError, match=r".*polygon_area function take maximum 1 keyword/named arguments, more provided*"):
        session5.polygon_area(1, sides=4, test = 0)

def test_session5_polygon_area_output():
    length = 10
    assert math.isclose(
        ((length ** 2) * math.sqrt(3)) / 4, session5.polygon_area(length, sides=3), rel_tol=1e-3
    ), "test_session5_polygon_area fails for 3 sides"
    assert math.isclose(
        length ** 2, session5.polygon_area(length, sides=4), rel_tol=1e-3
    ), "test_session5_polygon_area fails for 4 sides"
    assert math.isclose(
        172.05, session5.polygon_area(length, sides=5), rel_tol=1e-3
    ), "test_session5_polygon_area fails for 5 sides"
    assert math.isclose(
        (((3 * math.sqrt(3)) / 2) * (length ** 2)),
        session5.polygon_area(length, sides=6),
        rel_tol=1e-3,
    ), "test_session5_polygon_area fails for 6 sides"



####################### Validations for temp_converter()########################

def test_session5_temp_converter():
    """Test temp_converter function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'temp'*"):
        session5.temp_converter()

def test_session5_temp_converter_temp():
    """Test temp_converter function for incorrect values for positional argument temp (check for string AND imaginary input) """
    with pytest.raises(ValueError, match=r".*Temperature should be in float*"):
        session5.temp_converter('10')
    with pytest.raises(ValueError, match=r".*Temperature should be in float*"):
        session5.temp_converter(3+4j)

def test_session5_temp_converter_temp_given_in():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for incorrect value to temp_given_in keyword argument"""
    with pytest.raises(ValueError, match=r".*Only f or c is allowed*"):
        session5.temp_converter(10,temp_given_in='K')
    with pytest.raises(TypeError, match=r".*Charcater string expected*"):
        session5.temp_converter(10,temp_given_in=1+2j)

def test_session5_temp_converter_temp_values_in_celsius():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for permissible values for temprature in celsius"""
    with pytest.raises(ValueError, match=r".*Temprature can't go below -273.15 celsius = 0 Kelvin*"):
        session5.temp_converter(-280,temp_given_in='C')

def test_session5_temp_converter_temp_values_in_fahrenheit():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for permissible values for temprature in fahrenheit"""
    with pytest.raises(ValueError, match=r".*Temprature can't go below -459.67 fahrenheit = 0 Kelvin*"):
        session5.temp_converter(-500,temp_given_in='F')

def test_session5_temp_converter_unwanted_args():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for unwanted positional/keyword arguments"""
    with pytest.raises(TypeError, match=r".*temp_converter function takes maximum 1 positional arguments, more provided*"):
        session5.temp_converter(100,2,temp_given_in='F')
    with pytest.raises(TypeError, match=r".*temp_converter function take maximum 1 keyword/named arguments, more provided*"):
        session5.temp_converter(100,temp_given_in='C', test = 0)

def test_session5_temp_converter_output_in_fahrenheit():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for output with multiple inputs in fahrenheit"""
    assert session5.temp_converter(25,temp_given_in='c') == 77.0, "temp_converter is not working as expected"
    assert session5.temp_converter(-25,temp_given_in='C') == -13.0, "temp_converter is not working as expected"

def test_session5_temp_converter_output_in_celsius():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for output with multiple inputs in celsius"""
    assert session5.temp_converter(77,temp_given_in='f') == 25.0, "temp_converter is not working as expected"
    assert session5.temp_converter(-13,temp_given_in='F') == -25, "temp_converter is not working as expected"


####################### Validations for speed_converter()########################

def test_session5_speed_converter():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'speed''*"):
        session5.speed_converter()

def test_session5_speed_converter_speed():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for incorrect values for positional argument temp"""
    with pytest.raises(TypeError, match=r".*Speed can be int or float type only*"):
        session5.speed_converter('sac')
    with pytest.raises(TypeError, match=r".*Speed can be int or float type only*"):
        session5.speed_converter(1+2j)

def test_session5_speed_converter_dist():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for incorrect type of value for dist keyword argument"""
    with pytest.raises(TypeError, match=r".*Charcater string expected for distance unit*"):
        session5.speed_converter(10,dist=10)
    with pytest.raises(TypeError, match=r".*Charcater string expected for distance unit*"):
        session5.speed_converter(10,dist=1+2j)

def test_session5_speed_converter_time():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for incorrect type of value for time keyword argument"""
    with pytest.raises(TypeError, match=r".*Charcater string expected*"):
        session5.speed_converter(10,time=10)
    with pytest.raises(TypeError, match=r".*Charcater string expected*"):
        session5.speed_converter(10,time=1+2j)

def test_session5_speed_converter_speed_allowed_values():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for permissible value for speed argument"""
    with pytest.raises(ValueError, match=r".*Speed can't be negative*"):
        session5.speed_converter(-100)
    with pytest.raises(ValueError, match=r".*Speed can't be greater than speed of light*"):
        session5.speed_converter(300001)

def test_session5_speed_converter_time_allowed_values():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for permissible value for time keyword argument"""
    with pytest.raises(ValueError, match=r".*Incorrect unit of Time. Only ms/s/min/hr/day allowed*"):
        session5.speed_converter(10,time='KM')
    with pytest.raises(ValueError, match=r".*Incorrect unit of Time. Only ms/s/min/hr/day allowed*"):
        session5.speed_converter(10,time='YRD')

def test_session5_speed_converter_dist_allowed_values():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for permissible value for dist keyword argument"""
    with pytest.raises(ValueError, match=r".*Incorrect unit of distance. Only km/m/ft/yrd allowed*"):
        session5.speed_converter(10,dist='MIN')
    with pytest.raises(ValueError, match=r".*Incorrect unit of distance. Only km/m/ft/yrd allowed*"):
        session5.speed_converter(10,dist='HR')

def test_session5_speed_converter_unwanted_args():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for unwanted positional/keyword arguments"""
    with pytest.raises(TypeError, match=r".*speed_converter function takes maximum 1 positional arguments, more provided*"):
        session5.speed_converter(100,2)
    with pytest.raises(TypeError, match=r".*speed_converter function take maximum 2 keyword/named arguments, more provided*"):
        session5.speed_converter(100,dist='M', time = 'HR', test = 'abc')

def test_session5_speed_converter_output_km_to():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for output with multiple inputs from km/(x), x can be ms/s/min/hr/day"""
    assert session5.speed_converter(36000,dist='km',time='ms') == 0, "speed_converter is not working as expected"
    assert session5.speed_converter(36000,dist='km',time='s') == 10, "speed_converter is not working as expected"
    assert session5.speed_converter(6000,dist='km',time='min') == 100, "speed_converter is not working as expected"
    assert session5.speed_converter(100,dist='km',time='hr') == 100, "speed_converter is not working as expected"
    assert session5.speed_converter(100,dist='km',time='day') == 2400, "speed_converter is not working as expected"

def test_session5_speed_converter_output_m_to():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for output with multiple inputs from m/(x), x can be ms/s/min/hr/day"""
    assert session5.speed_converter(36000,dist='m',time='ms') == 10, "speed_converter is not working as expected"
    assert session5.speed_converter(3600,dist='m',time='s') == 1000, "speed_converter is not working as expected"
    assert session5.speed_converter(60,dist='m',time='min') == 1000, "speed_converter is not working as expected"
    assert session5.speed_converter(60,dist='m',time='hr') == 60000, "speed_converter is not working as expected"
    assert session5.speed_converter(24,dist='m',time='day') == 576000, "speed_converter is not working as expected"

def test_session5_speed_converter_output_ft_to():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for output with multiple inputs from ft/(x), x can be ms/s/min/hr/day"""
    assert session5.speed_converter(36000,dist='ft',time='ms') == 33, "speed_converter is not working as expected"
    assert session5.speed_converter(36000,dist='ft',time='s') == 32808, "speed_converter is not working as expected"
    assert session5.speed_converter(6000,dist='ft',time='min') == 328084, "speed_converter is not working as expected"
    assert session5.speed_converter(100,dist='ft',time='hr') == 328084, "speed_converter is not working as expected"
    assert session5.speed_converter(100,dist='ft',time='day') == 7874016, "speed_converter is not working as expected"

def test_session5_speed_converter_output_yrd_to():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for output with multiple inputs from yrd/(x), x can be ms/s/min/hr/day"""
    assert session5.speed_converter(36000,dist='yrd',time='ms') == 11, "speed_converter is not working as expected"
    assert session5.speed_converter(3600,dist='yrd',time='s') == 1094, "speed_converter is not working as expected"
    assert session5.speed_converter(6000,dist='yrd',time='min') == 109361, "speed_converter is not working as expected"
    assert session5.speed_converter(100,dist='yrd',time='hr') == 109361, "speed_converter is not working as expected"
    assert session5.speed_converter(100,dist='yrd',time='day') == 2624664, "speed_converter is not working as expected"
