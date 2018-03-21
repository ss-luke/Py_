###This covers Python strings split and any other string operations on a given object
###This also covers regular expressions in Python

import re

#####Regex####
# 1. Any character- like 1,2,q,a,A,> tells to just match itself
# 2. . -- matches any single character other than "\n"
# 3. \w - Matches a word-- [a-zA-Z0-9_]
# 4. \W - Matches any non-word character
# 5. ^- Match the start of the string
# 6. $-Match the end of the string 
# 7. \d - Match the decimal digit
# 8. \t, \n, \r -- tab, newline, return
# 9. \s- Matches any whitespace character 
# 10. \S- matches any non-whitespace character

#####Function to match: match , module: re

###Practically quite useful Regex operation: Grouping

##match- re.match(pattern, string, flags = 0)
## Flags are A|S|I|L|M|X, can be specified in the same maanner, delimited by | - pipe
## Escape character-- \


string_="m_ss_20180320_1816"
string_1="Word"

match_=re.match(r'(.*)_(.*)_(\d+)_(\d+)',string_,flags=0)

##Grouping index start from 1
##Explanation-- \d+ Match all decimal digits and group them 


# match()     Determine if the RE matches at the beginning of the string.
# search()     Scan through a string, looking for any location where this RE matches.
# findall()     Find all substrings where the RE matches, and returns them as a list.
# finditer()     Find all substrings where the RE matches, and returns them as an iterator.


print(match_) ####Print match object
if match_ :
    print(match_.group(1))
    print(match_.group(2))
    print(match_.group(3))
    print(match_.group(4))

print("Enter a digit: ")
word=input()
if re.match(r'\d+', word, flags=0):
    print("Ok, the input", word," is a digit!")
else:
    print("The input is not a digit!")
    
##Flags

# print("Enter a String: ")
# str_=input()