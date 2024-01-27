favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

# for name in sorted(favourite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll")

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

languages = {"python", "ruby", "python", "c"}
print(languages)