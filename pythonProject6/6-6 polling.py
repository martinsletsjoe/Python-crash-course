favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    "harald": "",
    "lars": "",
    }


for key in favourite_languages.keys():
    if favourite_languages[key] != "":
        print(f"Thank you for taking the poll, {key}.")
    else:
        print(f"please take the poll, {key}.")
