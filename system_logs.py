
import re,sys

def show_time_of_pid(logfile):
    '''
    display the date, time, and process id that's inside the square brackets. 
    We can read each line of the syslog and pass the contents to the show_time_of_pid function
    '''
    with open(logfile,'r') as file:
        count = 0
        for line in file:
            pattern = r'^(\w+\s[0-9]+\s[0-9]+:[0-9]+:[0-9]+)\s[\w\.]+\s[\w=]+\[([0-9]+)\]'
            result = re.search(pattern, line)
            if result is None:
                print('Done!: all process pids have been extracted!')
                break
            else:
                print('{} pid:{}'.format(result[1],result[2]))
                count += 1

        return 'Total extracted process pids: {}'.format(count)
                
    
show_time_of_pid('fishy.log')
