import re

# More RegEx problems!! 
# This document has a ton of regex problems for you to practice with.  Complete as many of these as
# you desire to get a better understanding of regex.  There is a separate answer file attached
# so you can check your work.  Have Fun!!

# problem 1
# should extract a match where the first group is the username, the second group is the domain
# and the third group is the top-level domain (com, edu, org, etc.)
email_string = "student123@university.edu"
pat = re.compile("REPLACE ME", re.IGNORECASE)
email_matches = pat.match(email_string)

# problem 2
# should extract a match where the first group is the hour, the second group is the minutes,
# and the third group is AM or PM (if present)
time_string = "3:45 PM"
pat = re.compile("REPLACE ME", re.IGNORECASE)
time_matches = pat.match(time_string)

# problem 3
# should extract all words that are at least 5 characters long and contain at least one vowel
text_string = "Python programming is an excellent skill to learn quickly"
pat = re.compile("REPLACE ME", re.IGNORECASE)
word_matches = pat.findall(text_string)

# problem 4
# should extract a match where the first group is the protocol (http or https), 
# the second group is the domain, and the third group is the path (if present)
url_string = "https://github.com/user/repository"
pat = re.compile("REPLACE ME", re.IGNORECASE)
url_matches = pat.match(url_string)

# problem 5
# should extract all valid US phone numbers in various formats (e.g., 555-123-4567, (555) 123-4567, 5551234567)
contact_string = "Call me at 555-123-4567 or (312) 456-7890 or send a text to 8473216540"
pat = re.compile("REPLACE ME", re.IGNORECASE)
phone_matches = pat.findall(contact_string)

# Make sure to uncomment the code below for testing these new patterns
if __name__ == "__main__":
    print("<<<<< Email Problem >>>>>\n")
    # uncomment the following prints to see email results and asserts to test
    # print(f"username is: {email_matches.group(1)}!") # should print "username is: student123"
    # print(f"domain is: {email_matches.group(2)}!")   # should print "domain is: university"
    # print(f"tld is: {email_matches.group(3)}!")      # should print "tld is: edu"
    # assert email_matches.group(1) == 'student123', "Incorrect username"
    # assert email_matches.group(2) == 'university', "Incorrect domain"
    # assert email_matches.group(3) == 'edu', "Incorrect top-level domain"
    # print('\n<<<< Email extraction tests passed >>>>\n')

    print("<<<<< Time Problem >>>>>\n")
    # uncomment the following prints to see time results and asserts to test
    # print(f"hour is: {time_matches.group(1)}!")      # should print "hour is: 3"
    # print(f"minutes is: {time_matches.group(2)}!")   # should print "minutes is: 45"
    # print(f"period is: {time_matches.group(3)}!")    # should print "period is: PM"
    # assert time_matches.group(1) == '3', "Incorrect hour"
    # assert time_matches.group(2) == '45', "Incorrect minutes"
    # assert time_matches.group(3) == 'PM', "Incorrect period"
    # print('\n<<<< Time extraction tests passed >>>>\n')

    print("<<<<< Word Problem >>>>>\n")
    # uncomment the following prints to see results and asserts to test
    # print(f"long words are: {word_matches}")  # should be ['Python', 'programming', 'excellent', 'skill', 'learn', 'quickly']
    # assert word_matches == ['Python', 'programming', 'excellent', 'skill', 'learn', 'quickly'], "Incorrect words"
    # print('\n<<<< Word extraction tests passed >>>>\n')

    print("<<<<< URL Problem >>>>>\n")
    # uncomment the following prints to see results and asserts to test
    # print(f"protocol is: {url_matches.group(1)}!")  # should print "protocol is: https"
    # print(f"domain is: {url_matches.group(2)}!")    # should print "domain is: github.com"
    # print(f"path is: {url_matches.group(3)}!")      # should print "path is: /user/repository"
    # assert url_matches.group(1) == 'https', "Incorrect protocol"
    # assert url_matches.group(2) == 'github.com', "Incorrect domain"
    # assert url_matches.group(3) == '/user/repository', "Incorrect path"
    # print('\n<<<< URL extraction tests passed >>>>\n')

    print("<<<<< Phone Number Problem >>>>>\n")
    # uncomment the following prints to see results and asserts to test
    # print(f"phone numbers are: {phone_matches}")  # should be ['555-123-4567', '(312) 456-7890', '8473216540']
    # assert phone_matches == ['555-123-4567', '(312) 456-7890', '8473216540'], "Incorrect phone numbers"
    # print('\n<<<< Phone number extraction tests passed >>>>\n')

    # print('\n<<<< All tests passed! >>>>')