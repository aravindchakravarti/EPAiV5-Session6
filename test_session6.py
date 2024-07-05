import pytest
import random
import string
import os
import inspect
import re
import math
import time
from session6 import doc_string_check


def test_readme_exists():
    '''
    Checks if readme exists
    '''
    assert os.path.isfile("README.md"), "README.md file doesn't exists"

def test_doc_strings_without_docstring():
    '''
    Checks if function caches if no docstring present
    '''
    with pytest.raises(SyntaxError, match=r".*no docstring*"):
        def add_with_num_no_doc(a, b):
            return(a+b)
        fn_test = doc_string_check(add_with_num_no_doc)
        fn_test(2,3)

def test_doc_string_check():
    '''
    Check if number of words in docstring is less than 50
    '''
    with pytest.raises(SyntaxError, match=r".*minimum 50*"):
        def add(a, b):
            '''
            This function adds two numbers and returns sum
            '''
            return (a+b)
        fn_test = doc_string_check(add)
        fn_test(4, 5)


def test_doc_string_no_exception():
    '''
    Check if number of words in docstring is less than 50
    '''
    def add_with_long_doc(a, b):
        '''
        This function adds two numbers and returns the sum. The purpose of this function
        is to demonstrate the addition of two integers or floats. The result of the 
        addition will be returned as the output of this function. This docstring is 
        deliberately made long to satisfy the requirement of having at least fifty words.
        '''
        return (a+b)
    fn_test = doc_string_check(add_with_long_doc)
    try:
        fn_test(1, 2)
    except:
        pytest.fail("test_doc_string_check raised exception unexpectedly")


def test_doc_strings_without_letter():
    '''
    Check docstring contains only numbers
    '''
    with pytest.raises(SyntaxError, match=r".*few charecter*"):
        def add_with_num_only_doc(a, b):
            '''
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            0 1 2 3 4 5 6 7 8 9
            '''
            return(a+b)
        fn_test = doc_string_check(add_with_num_only_doc)
        fn_test(2,3)
    
