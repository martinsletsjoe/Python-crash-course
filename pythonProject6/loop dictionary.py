# user_0 = {
#     "username": "efermi",
#     "first": "enrico",
#     "last": "fermi"
# }
#
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")
#

favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

# for name, language in favourite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

friends = ["phil", "sarah"]
for name in favourite_languages.keys():
    # print(name.title())

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

if "erin" not in favourite_languages.keys():
    print("Erin, please take our poll!")