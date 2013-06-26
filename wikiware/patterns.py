import re

# match "( and (anything) here )" inclusive
parentheses_pattern = re.compile("\(([^()])+\)")

# match "[[ anything |" inclusive
right_angled_brackets_pattern = re.compile("\[\[[^\]]*?\|")

# match "<ref anything />" or "<ref> anything </ref>" inclusive
ref_pattern = re.compile("<\s*ref[^>]*?\/>|<\s*ref[^>*]*>.*?</ref>")

# match html comments "<!-- anything -->" inclusive
html_comment_pattern = re.compile("\<!--.*?--\>") 

# match "{{ anything }}" inclusive
curly_brackets_pattern = re.compile("\{\{.*?[^\}\}]\}\}")

# match any "[[" or "]]"
double_angled_brackets_pattern = re.compile("\[\[|\]\]")

# match space before comma " ," or "       ,"
comma_pattern = re.compile(" {1,}\,")

# match space before dot " ." or "       ."
dot_pattern = re.compile(" {1,}\.")



