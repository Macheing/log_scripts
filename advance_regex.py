# advance regex
import re 


def long_words(text):
    # find words atleast 7 longer.
  pattern = r'[a-zA-Z]{7,}'
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  #print(result)
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)


def extract_pid(log_id):
    '''
    extract process id and process status.
    '''
    regex = r"\[(\d+)\]\: ([A-Z]+)"
    result = re.search(regex, log_id)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

log1 = "August 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
log2 = "689 elephants look mesirably in the [zoo]"
log3 = "A string that also has numbers [34567] but no uppercase message"
log4 = "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"
print(extract_pid(log1)) # 12345 (ERROR)
print(extract_pid(log2)) # None
print(extract_pid(log3)) # None
print(extract_pid(log4))# 67890 (RUNNING)



def transform_record(record):
  '''
  modify US phone number to international format.
  '''
  new_record = re.sub(r',(?=\d)',r',+1-',record)
  return new_record
 

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator
print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist
print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer
print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


def multi_vowel_words(text):
  '''
  check if word contain atleast 3 vowels in a sentence and
  return them, or otherwise none. 
  '''
  pattern = r'\w*[aeiou]{3,}\w*'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']
print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']
print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']
print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']
print(multi_vowel_words("Hello world!")) 
# []


def transform_comments(line_of_code):
  '''
  convert python line comments (#) to C line comments(//).
  '''
  result = re.sub(r'#+',r'//',line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"


def convert_phone_number(phone):
  '''
  checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 
  3 more digits followed by a dash, and 4 digits), and converts it to a more formal 
  format that looks like this: (XXX) XXX-XXXX
  '''
  result = re.sub(r'\s(\d{3})-', r' (\1) ',phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) 
# Phone number of Buckingham Palace is +44 303 123 7300
