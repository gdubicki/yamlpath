"""
Defines a custom type for YAML Path segment attributes.

Copyright 2020 William W. Kimball, Jr. MBA MSIS
"""
from typing import Union

from yamlpath.path import CollectorTerms
import yamlpath.path.searchterms as searchterms


PathAttributes = Union[str, CollectorTerms, searchterms.SearchTerms]
