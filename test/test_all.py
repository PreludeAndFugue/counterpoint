"""
Run all tests.

All the module names are stored in a list. Then a TestSuite is create from all
tests in the modules. The test suite is run and the results from the TestResult
object are printed.
"""

import unittest

def print_problems(problems, error_header):
    """Print the details of all errors or failures in the list of problems.
    
    problems: TestResult.failures or TestResult.errors object
    error_header: header info (string)
    """
    print '%s: %s' % (error_header, len(problems))
    print '-'*len(error_header)
    for i, (test_name, traceback) in enumerate(problems):
        print i + 1
        print test_name
        print traceback
        print

def main():
    module_names = ['rest_test', 'note_test']

    suite = unittest.TestLoader().loadTestsFromNames(module_names)
    print 'Number of tests: %s' % suite.countTestCases()
    
    results = unittest.TestResult()
    suite.run(results)
    
    if not results.wasSuccessful():
        print_problems(results.errors, 'Errors')
        print_problems(results.failures, 'Failures')
    else:
        print 'All tests passed.'
    
    
if __name__ == '__main__':
    main()