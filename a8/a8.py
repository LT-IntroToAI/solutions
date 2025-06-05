import re

# From Google python regular expressions examples with Nick Parlante

# . (dot) any char
# \w word char
# \d digit
# \s whitespace \S non whitespace
# + 1 or more
# * 0 or more


string = "called piiig"
pat = re.compile("iig")
result = pat.search(string)
print(result)
print(result.group())

pat = re.compile("iig")
result = pat.match(string)
print(result)

pat = re.compile("igs")
result = pat.search(string)
print(result)

pat = re.compile("ig")
result = pat.search(string)
print(result.group())

pat = re.compile("...g")
result = pat.search(string)
print(result.group())

pat = re.compile("x...g")
result = pat.search(string)
print(result)

pat = re.compile("..gs")
result = pat.search(string)
print(result)

string = "called piiig  much better: xyzg"
pat = re.compile("..g")
result = pat.search(string)
print(result.group())

pat = re.compile("..g")
result = pat.match(string)
# print(result.group())

string = "c.lled piiig  much better: xyzgs"
pat = re.compile("c\.l")
result = pat.search(string)
print(result.group())

string = 'blah :cat blah blah'
pat = re.compile(":\w\w\w")
result = pat.search(string)
print(result.group())

string = 'blah :123xxx '
pat = re.compile("\d\d\d")
result = pat.search(string)
print(result.group())

string = "1 2 3"
pat = re.compile("\d\s\d\s\d")
result = pat.search(string)
print(result.group())

string = "1      2       3"
pat = re.compile("\d\s+\d\s+\d")
result = pat.search(string)
print(result.group())

string = "blah blah :kitten blah blah"
pat = re.compile(":\w+")
result = pat.search(string)
print(result.group())

string = "blah blah :kitten123 blah blah"
pat = re.compile(":\w+")
result = pat.search(string)
print(result.group())

string = "blah blah :kitten123$ blah blah"
pat = re.compile(":\w+")
result = pat.search(string)
print(result.group())

string = "blah blah :kitten123$ blah blah"
pat = re.compile(":.+")
result = pat.search(string)
print(result.group())

string = "blah blah :kitten123$ blah blah"
pat = re.compile(":\S+")
result = pat.search(string)
print(result.group())

string = "blah blah rberg@cps.edu blah blah"
pat = re.compile("\w+@\w+")
result = pat.search(string)
print(result.group())

pat = re.compile("[\w.]+@[\w.]+")
result = pat.search(string)
print(result.group())

pat = re.compile("([\w.]+)@([\w.]+)")
result = pat.search(string)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.groups())

string = "blah blah rberg@cps.edu blah blah foo@bar.com"
pat = re.compile("([\w.]+)@([\w.]+)")
results = pat.findall(string)
print(results)

# Do as a class
cc_string = "Number: 1234123412341234 CVV: 123"
pat = re.compile("(Number:) (?P<number>\d{16}) (CVV:) (?P<cvv>\d{3})", re.IGNORECASE)
cc_match = pat.match(cc_string)
print(cc_match.group("number"))
print(cc_match.group("cvv"))