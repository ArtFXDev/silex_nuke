import re

# Regex used to expand and capture syntaxes for sequences like #### or <UDIM> ...
MATCH_FILE_SEQUENCE = [
    re.compile(r"^.+\W(\%\d*d)\W.+$"),  # Matches %d syntax
    re.compile(r"^.+[^\w#](#+)\W.+$"),  # Matches ####  syntax
]
