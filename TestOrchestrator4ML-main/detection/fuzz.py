
import random
#from py_parser import *
from main import *
import os 

FILEPATH = os.path.join(
    os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'blns.txt')
"""Path to the file"""
'''
def simpleCalculator(v1, v2, operation):
    print('The operation is: ', operation)
    valid_ops = ['+', '-', '*', '/', '%']
    res = 0 
    if operation in valid_ops:
        if operation=='+':
            res = v1 + v2 
        elif operation=='-':
            res = v1 - v2 
        elif operation=='*':
            res = v1 * v2 
        elif operation=='/':                
            res = v1 / v2 
        elif operation=='%':                
            res = v1 % v2 
        print('After the calculation the result is: ', res)
    else: 
        print('Operation not allowed. Allowable operations are: +, -, *, /, %')
        print('No calculation was done')  
    return res 
'''
def fuzzValues(filepath=FILEPATH):
     """Get the list of naughty_strings.
    By default this will get the strings from the blns.txt file
    Code is a simple port of what is already in the /scripts directory
    :param filepath: Optional filepath the the blns.txt file
    :returns: The list of naughty strings
    """

     strings = []
     with open(filepath, 'r') as f:

        # put all lines in the file into a Python list
        strings = f.readlines()
        
        # above line leaves trailing newline characters; strip them out
        strings = [x.strip(u'\n') for x in strings]
        
        # remove empty-lines and comments
        strings = [x for x in strings if x and not x.startswith(u'#')]
        
        # insert empty string since all are being removed
        strings.insert(0, u"")

     return strings


def checkNonPermissiveOerations():
    #operation_ = '='
    #op_list = [x for x in range(100) ]
    #for operation_ in op_list:
    string = fuzzValues()
    for i in range(100, 120): 
        test_script = string[i]
        #"../../../../../../../../../../../etc/passwd%00"
        checkAccuracyTest(test_script)
        print('System: Method 1 Test')
        print('System: Fuzz value checked against: ', string[i])
        print('='*100)

    for i in range(100, 120): 
        test_script = string[i]
        #"../../../../../../../../../../../etc/passwd%00"
        get_test_details(test_script)
        print('System: Method 2 Test')
        print('System: Fuzz value checked against: ', string[i])
        print('='*100)


def simpleFuzzer(): 
    # Complete the following methods 
    # fuzzValues()
    checkNonPermissiveOerations() 



if __name__=='__main__':
    #val1, val2, op = 100, 1, '+'

    #data = simpleCalculator(val1, val2, op)
    #print('Operation:{}\nResult:{}'.format(  op, data  ) )
    simpleFuzzer()