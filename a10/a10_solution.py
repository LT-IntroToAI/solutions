import re, string, calendar
from wikipedia import page
import wikipedia
from bs4 import BeautifulSoup
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree
from match import match
from typing import List, Callable, Tuple, Any, Match


def get_named_entities(text: List[str]) -> List[str]:
    """Finds named entities in the given text

    Args:
        text - the list of words in which to search for a named entity

    Returns:
        a continuous chunk of words representing the named entity if any
    """
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk: List[str] = []
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue
    return continuous_chunk


def get_page_html(title: str) -> str:
    """Gets html of a wikipedia page

    Args:
        title - title of the page

    Returns:
        html of the page
    """
    return page(title).html()


def get_first_infobox_text(html: str) -> str:
    """Gets first infobox html from a Wikipedia page (summary box)

    Args:
        html - the full html of the page

    Returns:
        html of just the first infobox
    """
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all(class_="infobox")

    if not results:
        raise LookupError("Page has no infobox")
    return results[0].text


def clean_text(text: str) -> str:
    """Cleans given text removing non-ASCII characters and duplicate spaces & newlines

    Args:
        text - text to clean

    Returns:
        cleaned text
    """
    only_ascii = "".join([char if char in string.printable else " " for char in text])
    no_dup_spaces = re.sub(" +", " ", only_ascii)
    no_dup_newlines = re.sub("\n+", "\n", no_dup_spaces)
    return no_dup_newlines


def get_match(
    text: str,
    pattern: str,
    error_text: str = "Page doesn't appear to have the property you're expecting",
) -> Match:
    """Finds regex matches for a pattern

    Args:
        text - text to search within
        pattern - pattern to attempt to find within text
        error_text - text to display if pattern fails to match

    Returns:
        text that matches
    """
    p = re.compile(pattern, re.DOTALL | re.IGNORECASE)
    match = p.search(text)

    if not match:
        raise AttributeError(error_text)
    return match


def get_polar_radius(planet_name: str) -> str:
    """Gets the radius of the given planet

    Args:
        planet_name - name of the planet to get radius of

    Returns:
        radius of the given planet
    """
    infobox_text = clean_text(get_first_infobox_text(get_page_html(planet_name)))
    pattern = r"(?:Polar radius.*?)(?: ?[\d]+ )?(?P<radius>[\d,.]+)(?:.*?)km"
    error_text = "Page infobox has no polar radius information"
    match = get_match(infobox_text, pattern, error_text)

    return match.group("radius")


def get_birth_date(name: str) -> str:
    """Gets birth date of the given person

    Args:
        name - name of the person

    Returns:
        birth date of the given person
    """
    infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))
    pattern = r"(?:Born\D*)(?P<birth>\d{4}-\d{2}-\d{2})"
    error_text = (
        "Page infobox has no birth information (to be more specific"
        " none in xxxx-xx-xx format)"
    )
    match = get_match(infobox_text, pattern, error_text)

    return match.group("birth")


def percent_match(pattern: List[str], source: List[str]) -> float:
    """Determines the percentage match between the pattern and source

    Args:
        pattern - strings with % and _ matching words in the source
        source - a phrase represented as a list of words (strings)

    Returns:
        the percent match between pattern and source
    """
    match_ct = 0
    for word in source:
        if word in pattern:
            match_ct += 1
    return float(match_ct) / len(pattern) * 100


def approximate_match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to find an approximate match between the pattern and source

    Args:
        pattern - strings with % and _ matching words in the source
        source - a phrase represented as a list of words (strings)

    Returns:
        the approximate match if any
    """
    if percent_match(pattern, source) > 0.50:
        sent = pos_tag(source)
        res = get_named_entities(source)
        print(f"Found an approximate match! {pattern}")
        print(f"I think you're asking about: {res}")
        return res
    else:
        return None


global planet
global person
global third_person_pronouns
third_person_pronouns = [
    "he",
    "she",
    "it",
    "its",
    "him",
    "her",
    "his",
    "hers",
    "they",
    "them",
    "their",
    "theirs",
]
planet = ""
person = ""

# below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns
# a list of the answer(s) and not just the answer itself.


def birth_date(matches: List[str]) -> List[str]:
    """Returns birth date of named person in matches

    Args:
        matches - match from pattern of person's name to find birth date of

    Returns:
        birth date of named person
    """
    global person
    if not matches[0].lower().strip() in third_person_pronouns:
        person = " ".join(matches)
    return [get_birth_date(person)]


def polar_radius(matches: List[str]) -> List[str]:
    """Returns polar radius of planet in matches

    Args:
        matches - match from pattern of planet to find polar radius of

    Returns:
        polar radius of planet
    """
    global planet
    if not matches[0].lower().strip() in third_person_pronouns:
        planet = matches[0]
    return [get_polar_radius(planet)]


# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


global last_query
# the comment `type: ignore` on the next line prevents mypy from complaining that
# last_query doesn't have a type annotation. this is especially needed here as this is a
# mypy bug since Python does not allow type annotations on globals
last_query = []  # type: ignore


def catch_all(matches: List[str]):
    # TODO: COME BACK TO THIS
    """Catches any failed patterns

    Args:
        the string in which to find named entities

    Returns:
        matching wiki summary
    """
    global person

    nes = get_named_entities(last_query)
    person = nes[0]
    return [wikipedia.summary(nes[0], sentences=1)]


# type aliases to make pa_list type more readable, could also have written:
# pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [...]
Pattern = List[str]
Action = Callable[[List[str]], List[Any]]

# The pattern-action list for the natural language query system.  It must be declared
# here, after all of the function definitions
pa_list: List[Tuple[Pattern, Action]] = [
    ("when was % born".split(), birth_date),
    ("what is the polar radius of %".split(), polar_radius),
    (["bye"], bye_action),
    (["%"], catch_all),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]

    return ["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully"""
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


# uncomment the next line once you've implemented everything ready to try it out
# query_loop()
