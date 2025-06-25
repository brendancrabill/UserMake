import itertools

# Paste your CEWL wordlist here
raw_words = """
Single Word Names John Jill Jack
"""

# Clean and split
words = list(set(word.strip() for word in raw_words.split() if word.strip().isalpha()))


# Assumes captialized words are names
names = [w for w in words if w[0].isupper() and len(w) > 1]
first_names = names  # for simplicity, treat all as usable for first/last
last_names = names

usernames = set()

for first, last in itertools.product(first_names, last_names):
    first_l = first.lower()
    last_l = last.lower()
    first_i = first_l[0]
    last_i = last_l[0]

    # Generate combinations
    usernames.update({
        f"{first_l}",                 # john
        f"{last_l}",                  # doe
        f"{first_i}{last_l}",         # jdoe
        f"{first_l}{last_i}",         # johnd
        f"{first_l}.{last_l}",        # john.doe
        f"{first_l}_{last_l}",        # john_doe
        f"{first_l}{last_l}",         # johndoe
        f"{last_l}{first_l}",         # doejohn
        f"{last_l}.{first_l}",        # doe.john
        f"{first_i}.{last_l}",        # j.doe
        f"{last_l}.{first_i}",        # doe.j
        f"{last_l}_{first_i}",        # doe_j
    })

# Print or write to file
for u in sorted(usernames):
    print(u)
