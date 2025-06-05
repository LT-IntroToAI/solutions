# some python libraries we'll be using
import re, string, calendar
from wikipedia import page
from bs4 import BeautifulSoup

from typing import List, Match
from utilities import *


def get_planet_radius(planet_name: str) -> str:
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
        "Page infobox has no birth information (at least none in xxxx-xx-xx format)"
    )
    match = get_match(infobox_text, pattern, error_text)
    return match.group("birth")


if __name__ == "__main__":
    print("\n<<<<<<<<<<<<<< Testing Planet Radius >>>>>>>>>>>>>>")
    print(f'Mars has a polar radius of {get_planet_radius("Mars")}km')
    print(f'Earth has a polar radius of {get_planet_radius("Earth")}km')
    print(f'Jupiter has a polar radius of {get_planet_radius("Jupiter")}km')
    print(f'Saturn has a polar radius of {get_planet_radius("Saturn")}km')
    print("\n<<<< Running asserts, this might take a sec >>>>")
    assert get_planet_radius("Mars") == "3376.2", "Incorrect radius for Mars"
    assert get_planet_radius("Earth") == "6356.752", "Incorrect radius for Earth"
    assert get_planet_radius("Jupiter") == "66,854", "Incorrect radius for Jupiter"
    assert get_planet_radius("Saturn") == "54,364", "Incorrect radius for Saturn"

    print("\n<<<<<<<<<<<<<< Testing Birth Dates >>>>>>>>>>>>>>")
    print(format_birth(get_birth_date("Grace Hopper"), "Grace Hopper"))
    print(format_birth(get_birth_date("Alan Turing"), "Alan Turing"))
    print(format_birth(get_birth_date("Tim Berners-Lee"), "Tim Berners-Lee"))
    print(format_birth(get_birth_date("Anita Borg"), "Anita Borg"))
    print("\n<<<< Running asserts, this might take a sec >>>>")
    assert (
        get_birth_date("Grace Hopper") == "1906-12-09"
    ), "Incorrect birth date for Grace Hopper"
    assert (
        get_birth_date("Alan Turing") == "1912-06-23"
    ), "Incorrect birth date for Alan Turing"
    assert (
        get_birth_date("Tim Berners-Lee") == "1955-06-08"
    ), "Incorrect birth date for Tim Berners-Lee"
    assert (
        get_birth_date("Anita Borg") == "1949-01-17"
    ), "Incorrect birth date for Anita Borg"

    print("All tests passed!")
