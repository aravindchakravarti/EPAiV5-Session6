"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time
from timeit import default_timer as timer
#from timeit import default_timer as timer
import math

def time_it(fn, *args, repetitions= 1, **kwargs):
    '''
    This function takes function and that functions arguments as arguments
    and calculates the total time taken for the execution of test function
    '''

    if repetitions > 0:
        start_time = timer()

        # Repeat number of times
        for _ in range (repetitions):
            result = fn(*args, **kwargs)

        end_time = timer()

        # Return results
        return (end_time - start_time)
    else:
        return 0

def squared_power_list(number: int,*args: any, start: int=0, end: int=5,**kwargs: any) -> list:
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Checks if number is passed
    if not number:
        raise TypeError ("required positional argument: 'number'")

    # Checks if number is really int
    if type(number) != int:
        raise TypeError ("Only integer type arguments are allowed")

    # Checks if start and end are not negative
    if start < 0 or end < 0:
        raise ValueError ("Value of start or end can't be negative")

    # Checks if start is lesser than end
    if start > end:
        raise ValueError ("Value of start should be less than end")

    # Checks if number is less than 10, to prevent exploded retun value
    if number > 10:
        raise ValueError ("Value of number should be less than 10")

    # If user passes more than one positionl args than required, raise error
    if args:
        raise TypeError ("takes maximum 1 positional arguments")

    # If user passes any key, value pair (named entity) raise error
    if kwargs:
        raise TypeError ("maximum 2 keyword/named arguments")

    # Return the list of number to the power of numbers from start to end
    l = [number**i for i in range (start, end, 1)]

    return (l)

def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Check if lenght is provided correctly and is of int or float
    if not length:
        raise TypeError ("required positional argument: 'length'")

    if not (isinstance(length, float) or isinstance(length, int)):
        raise ValueError ("polygon_area accepts only int or float")

    # Number of sides will be always a whole number
    if not isinstance(sides, int):
        raise ValueError ("polygon_area accepts only int or float")

    # Lenght must exist for each vertix
    if length < 0:
        raise ValueError ("lenght must be greater than zero")

    # If user passes more than one positionl args than required, raise error
    if args:
        raise TypeError ("polygon_area function takes maximum 1 positional arguments, more provided")

    # If user passes any key, value pair (named entity) raise error
    if kwargs:
        raise TypeError ("polygon_area function take maximum 1 keyword/named arguments, more provided")

    # Need minimum 3 vertices to form surface
    if sides < 3:
        raise ValueError("sides must be greater than 2")
    else:
        return(sides * length**2) / (4 * math.tan(math.pi / sides))
    # Return area

def temp_converter(temp: float, *args: any, temp_given_in :str= 'f', **kwargs: any) -> float:
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""
    if not temp:
        raise TypeError ("There must be at least one positional argument 'temp'")

    if not (isinstance(temp, float) or isinstance(temp, int)):
        raise ValueError("Temperature should be in float") 

    # Check if temperature given in correct format
    if isinstance(temp_given_in, str) and temp_given_in not in ['c', 'C', 'f', 'F']:
        raise ValueError ("Only f or c is allowed")

    if not isinstance(temp_given_in, str):
        raise TypeError ("Charcater string expected")

    # Check if the temperature doesn't cross physical limits
    if temp_given_in in ['C', 'c'] and temp < -273.15:
        raise ValueError ("Temprature can't go below -273.15 celsius = 0 Kelvin")

    if temp_given_in in ['F', 'f'] and temp < -459.67:
        raise ValueError ("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")

    # If user passes more than one positionl args than required, raise error
    if args:
        raise TypeError ("temp_converter function takes maximum 1 positional arguments, more provided")

    # If user passes any key, value pair (named entity) raise error
    if kwargs:
        raise TypeError ("temp_converter function take maximum 1 keyword/named arguments, more provided")

    if temp_given_in in ['C', 'c']:
        return ((temp*(9/5))+32)
    elif temp_given_in in ['F', 'f']:
        return ((temp-32)*(5/9))

def speed_converter(speed: float, *args: any, dist: str='km', time: str='min', **kwargs: any) -> int:
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # If user passes more than one positionl args than required, raise error
    if args:
        raise TypeError ("speed_converter function takes maximum 1 positional arguments, more provided")

    # If user passes any key, value pair (named entity) raise error
    if kwargs:
        raise TypeError ("speed_converter function take maximum 2 keyword/named arguments, more provided")

    # Checks if given speed is either in float or int
    if not (isinstance(speed, float) or isinstance(speed, int)):
        raise TypeError("Speed can be int or float type only")

    # Checks if required distance conversion is given in string or not
    if not (isinstance(dist, str)):
        raise TypeError("Charcater string expected for distance unit")    

    # Checks if required time conversion is given in string or not
    if not (isinstance(time, str)):
        raise TypeError("Charcater string expected for time unit") 

    # Checks if speed is within the limits defined by PHYSICS :-D
    if speed < 0:
        raise ValueError("Speed can't be negative")

    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")

    # Checks time and dist for supported formats
    if time not in ['ms', 's', 'min', 'hr', 'day']:
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")

    if dist not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")

    '''
    We have input in kmph
    Ouput (time)        = ms, s, min, hr, day
    Output(distance)    = m, km, ft, yrd
    '''
    time_conv = {'ms':(3600000), 's':(3600), 'min':(60), 'hr':1, 'day':(1/24)}
    distance_conv = {'m':1000, 'km':1, 'ft':3280.84, 'yrd':1093.61}

    # speed = distance / time
    return(round(speed*(distance_conv[dist]/time_conv[time])))