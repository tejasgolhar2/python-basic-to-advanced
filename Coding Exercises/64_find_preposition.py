# Find Preposition
#       Implement a function which takes a quote as a parameter to find out which 
#   given prepositions have been used in the quote. The function should return 
#   the set of prepositions that are used in the quote.

def find_prep(v_quote):
    set1 = set(v_quote.split(" "))
    prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}
    new_set = set.intersection(set1,prep)
    return new_set


quote = """Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do."""

 
print(find_prep(quote))