import re

# Regex used to expand and capture syntaxes for sequences like #### or <UDIM> ...
MATCH_FILE_SEQUENCE = [
    re.compile(r"^.+\W(%d)\W.+$"),  # Matches %d format
]
