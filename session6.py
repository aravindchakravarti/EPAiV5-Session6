'''
    There is no separate assignment link. You need to write the code + test code, test your actions, and then 
    submit the link on the assignment page. 

1.  Write a closure that takes a function and then check whether the function passed has a docstring with 
    more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200

2.  Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100

3.  We wrote a closure that counts how many times a function was called. Write a new one that can keep 
    track of how many times add/mul/div functions were called, and update a global dictionary variable with 
    the counts (+ 6 tests) - 250

4.  Modify above such that now we can pass in different dictionary variables to update different dictionaries 
    (+ 6 tests) - 250

5.  Once done, upload the code to Git Hub, run actions, and then proceed to answer S6 - Assignment QnA. 

6.  No readme or no docstring for each function, or no test cases (4, 2, 6, 6, >7 = 25 tests), then 0. 
    Write at least 7 test cases to check boundary conditions that might cause your code to fail. 
    Scores = Total Tests * 5 + Total Cleared Tests * 5

'''

"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

def doc_string_check(fn):
    '''
    This function takes any arbitry function and checks if the docstring
    of the function is atleast 50 words. Else, raises warning
    '''
    min_words_in_doc = 50
    def doc_checker(*args: any, **kwargs: any):
        '''
        This function doesn't do anything other than counting number of 
        charecters in fn.__doc__
        '''
        copy_doc_string = str(fn.__doc__)
        doc_string_len = len(str(copy_doc_string).split())
        alpha_characters = len([char for char in copy_doc_string if char.isalpha()])
        
        # Checks if docstring present or not
        if (fn.__doc__ == None):
            raise SyntaxError (f'{fn.__name__} contains no docstring')
        
        # Check if docstring contains sufficient words
        if (doc_string_len < min_words_in_doc):
            raise SyntaxError ("docstring must contain minimum 50 words")
        
        # Check if docstring contains only letters
        if (alpha_characters < 100):
             raise SyntaxError ("docstring must contain few charecter atleast")
        
    return doc_checker


def fibonacci_closure():
    '''
    This function returns the closure for for generating next fibonacci numbers. 
    Function take argument for which next fib number to be generated.
    inedex: 1 2 3 4 5 6 7  8  9 10 ....
    Series: 0 1 1 2 3 5 8 13 21 34 55 ....
    Basically Fn = Fn-1 + Fn-2
    '''
    fn_0 = 0
    fn_1 = 1
    
    def next_fib(n: int=0)->int:
        '''
        Generates the next fionacci number
        '''
        if not isinstance(n, int):
            raise ValueError("Fibonacci series is defined only for integers")
        
        if (n < 0):
            raise ValueError("Fibonacci series is defined only for positive integers")

        nonlocal fn_0
        nonlocal fn_1
        # Loop through the index+1 times for which fib to be 
        # generated
        for _ in range (n+1):
            temp_0 = fn_0
            temp_1 = fn_1
            fn_0 = temp_1
            fn_1 = temp_0 + temp_1
        # Reset the nonlocal variables, so that variables are not 
        # persistant across function calls
        fn_0 = 0
        fn_1 = 1
        return (temp_0)
    return next_fib

# Declare a global variable to keep track of function call count
fn_called = {}

def fun_cnt_closure(fn):
    '''
    This function keep counts of how many times a function gets called
    '''
    def fn_counter(*args, **kwargs):
        '''
        This function keeps count of how many times a function is called
        '''
        # Access the global variable
        global fn_called

        # Fetch the name of function and check if already exists in dictionary
        # if not create the key in the dictionary and initialize it to zero.
        if not (fn.__name__ in fn_called.keys()):
            fn_called[fn.__name__] = 0
        
        # Update the count
        fn_called[fn.__name__] =  fn_called[fn.__name__] + 1

        # Return value, which is not used
        _ = fn(*args, **kwargs)

        # Return the dictionary
        return (fn_called)
    return fn_counter