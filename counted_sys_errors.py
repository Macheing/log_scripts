import re

def count_error_types(logfile):
    usernames = {}
    with open(logfile,'r') as file:
        for line in file:
            # retrieves log errors containing CRON only.
            if 'CRON' not in line:
                continue
            #pattern = r'\W+\[([0-9]*)\]:\s([A-Z]*)\s\w+'
            pattern = r'^(\w+\s[0-9]+\s[0-9]+:[0-9]+:[0-9]+)\s[\w]+\s([\w=]+\[([0-9]+)\]):\s(\w+)'
            result = re.search(pattern,line)
            print( 'Date: {} process pid: {} type: {}'.format(result[1],result[2],result[4]))
            if result is None:
                continue
            name = result[4]
            #print(name)
            usernames[name] = usernames.get(name,0)+1
            
    return usernames

print(count_error_types('fishy.log'))
