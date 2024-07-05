[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/z8haBqsC)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15331559&assignment_repo_type=AssignmentRepo)
# epai5session5

# Function Documentation

## Overview
This document provides detailed information on the functions available in this module. Each function is designed to perform specific tasks and includes input validation to ensure correctness and reliability. Below are the functions included in this documentation:

1. `time_it(fn, *args, repetitions= 1, **kwargs)`
2. `squared_power_list (number, *args, start=0, end=5, **kwargs)`
3. `polygon_area (length, *args, sides=3, **kwargs)`
4. `temp_converter (temp, *args, temp_given_in='f', **kwargs)`
5. `speed_converter (speed, *args, dist='km', time='min', **kwargs)`

## Function Descriptions

### `time_it(fn, *args, repetitions=1, **kwargs)`

#### Purpose
The `time_it` function measures the execution time of a given function over a specified number of repetitions.

#### Parameters
- `fn`: The function to be timed.
- `*args`: Positional arguments to be passed to `fn`.
- `repetitions`: Number of times to repeat the function execution. Default is 1.
- `**kwargs`: Keyword arguments to be passed to `fn`.

#### Returns
- `result`: The result of the function `fn`.
- `execution_time`: The total time taken to execute `fn` over the specified number of repetitions.

## `squared_power_list`

Returns a list by raising `number` to powers from `start` to `end` (inclusive).

### Parameters
- `number`: The base number for exponentiation.
- `*args`: Additional positional arguments (not used in this function).
- `start`: The starting exponent (default is 0).
- `end`: The ending exponent (default is 5).
- `**kwargs`: Additional keyword arguments (not used in this function).

### Returns
- A list containing `number` raised to the power of each integer in the range `[start, end)`.

### Exceptions
- Raises `TypeError` if `number` is not provided or not an integer.
- Raises `ValueError` if `start` or `end` is negative, or if `start` is greater than `end`.
- Raises `ValueError` if `number` is greater than 10.
- Raises `TypeError` if more than one positional argument (`*args`) is provided.
- Raises `TypeError` if any keyword arguments (`**kwargs`) are provided.

## `polygon_area`

Returns the area of a regular polygon with a specified number of sides (3 to 6 inclusive).

### Parameters
- `length`: The length of each side of the polygon.
- `*args`: Additional positional arguments (not used in this function).
- `sides`: The number of sides of the polygon (default is 3).
- `**kwargs`: Additional keyword arguments (not used in this function).

### Returns
- The area of the regular polygon.

### Exceptions
- Raises `TypeError` if `length` is not provided or is not an integer or float.
- Raises `ValueError` if `sides` is not an integer or if it is less than 3.
- Raises `ValueError` if `length` is negative.
- Raises `TypeError` if more than one positional argument (`*args`) is provided.
- Raises `TypeError` if any keyword arguments (`**kwargs`) are provided.

## `temp_converter`

Converts temperature between Celsius ('C' or 'c') and Fahrenheit ('F' or 'f').

### Parameters
- `temp`: The temperature value to be converted.
- `*args`: Additional positional arguments (not used in this function).
- `temp_given_in`: The scale of the input temperature ('C' for Celsius, 'F' for Fahrenheit). Default is 'F'.
- `**kwargs`: Additional keyword arguments (not used in this function).

### Returns
- The converted temperature value.

### Exceptions
- Raises `TypeError` if `temp` is not provided or is not a float or integer.
- Raises `ValueError` if `temp_given_in` is not a string or if it is not one of ['C', 'c', 'F', 'f'].
- Raises `ValueError` if the temperature (`temp`) is below absolute zero for the given scale.
- Raises `TypeError` if more than one positional argument (`*args`) is provided.
- Raises `TypeError` if any keyword arguments (`**kwargs`) are provided.

## `speed_converter`

Converts speed from kilometers per hour (km/h) to various units of distance (`dist`) and time (`time`).

### Parameters
- `speed`: The speed value to be converted (in km/h).
- `*args`: Additional positional arguments (not used in this function).
- `dist`: The unit of distance to convert to (`km`, `m`, `ft`, `yrd`). Default is `km`.
- `time`: The unit of time to convert to (`ms`, `s`, `min`, `hr`, `day`). Default is `min`.
- `**kwargs`: Additional keyword arguments (not used in this function).

### Returns
- The converted speed value as an integer.

### Exceptions
- Raises `TypeError` if more than one positional argument (`*args`) is provided.
- Raises `TypeError` if more than two keyword arguments (`**kwargs`) are provided.
- Raises `TypeError` if `speed` is not a float or integer.
- Raises `TypeError` if `dist` or `time` are not strings.
- Raises `ValueError` if `speed` is negative or exceeds the speed of light (300,000 km/h).
- Raises `ValueError` if `dist` or `time` are not valid units ('km', 'm', 'ft', 'yrd' for `dist`; 'ms', 's', 'min', 'hr', 'day' for `time`).
