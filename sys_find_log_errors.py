#!/usr/bin/env python3
import sys
import os
import re

def error_search(log_file):
    '''
    search log file and ask user for an error type.
    '''
    error = input("What is the error? ") # enter: CRON ERROR Failed to start
    returned_errors = []
    #log_file = 'fishy.log'

    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()

    return returned_errors

  
def file_output(returned_errors):
    '''
    writes returned errors to a file
    '''
    with open('errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()
    print('Done!: identified Error(s) is already written to a file!')


if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)



    # Enter following commands on CLI to run this script and when system error is ask.
    # ./sys_find_log_errors.py fishy.log 
    # CRON ERROR Failed to start
    # cat error_found.log


