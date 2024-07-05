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