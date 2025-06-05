import re

# Assignment 8 Part 1

# problem 1
date_string = "November 9, 1982"
pat = re.compile("([a-zA-Z]*) ([0-9]*), ([0-9]*)", re.IGNORECASE)
date_matches = pat.match(date_string)

# problem 2
address_string = "2501 Addison Street\nChicago, IL 60618"
pat = re.compile(
    "(?P<number>([0-9]*)) (?P<street>([a-zA-Z ]*))\s*\n\s*(?P<city>([a-zA-Z]*)), (?P<state>([A-Z]*)) (?P<zip>([0-9]*))",
    re.IGNORECASE,
)
address_matches = pat.match(address_string)

# problem 3
tweet_string = "hi everyone! #cs #python #LT #champions"
pat = re.compile("#([\w]*)", re.IGNORECASE)
hashtag_matches = pat.findall(tweet_string)

if __name__ == "__main__":
    print("<<<<< Date Problem >>>>>\n")
    print(f"month is: {date_matches.group(1)}!")  # should print "month is: November"
    print(f"day is: {date_matches.group(2)}!")  # should print "day is: 9"
    print(f"year is: {date_matches.group(3)}!")  # should print "year is: 1982"
    assert date_matches.group(1) == "November", "Incorrect month"
    assert date_matches.group(2) == "9", "Incorrect day"
    assert date_matches.group(3) == "1982", "Incorrect year"
    print("\n<<<< Date extraction tests passed >>>>\n")

    print("<<<<< Address Problem >>>>>\n")
    # should print "number is: 2501"
    print(f'number is: {address_matches.group("number")}!')
    # should print "street is: Addison Street"
    print(f'street is: {address_matches.group("street")}!')
    # should print "city is: Chicago"
    print(f'city is: {address_matches.group("city")}!')
    # should print "state is: IL"
    print(f'state is: {address_matches.group("state")}!')
    # should print "zip is: 60618"
    print(f'zip is: {address_matches.group("zip")}!')
    assert address_matches.group("number") == "2501", "Incorrect address number"
    assert address_matches.group("street") == "Addison Street", "Incorrect street"
    assert address_matches.group("city") == "Chicago", "Incorrect city"
    assert address_matches.group("state") == "IL", "Incorrect state"
    assert address_matches.group("zip") == "60618", "Incorrect zip"
    print("\n<<<< Address extraction tests passed >>>>\n")

    print("<<<<< Hashtag Problem >>>>>\n")
    # should print "hashtags are: ['cs', 'python', 'LT', 'champions']"
    print(f"hashtags are: {hashtag_matches}")
    assert hashtag_matches == ["cs", "python", "LT", "champions"], "Incorrect hashtags"
    print("\n<<<< Hashtag extraction tests passed >>>>\n")

    print("\n<<<< All tests passed! >>>>")
