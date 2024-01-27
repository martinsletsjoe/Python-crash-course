favourite_languages = {
    "jen": {"python", "ruby"},
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favourite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favourite language is:")
    else:
        print(f"\n{name.title()}'s favourite languages are:")
    for languages in languages:
        print(f"\t{languages.title()}")