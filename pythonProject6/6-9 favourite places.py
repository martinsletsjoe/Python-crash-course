favourite_places = {
    "oskar": ["sandefjord", "larvik", "bø"],
    "lesh": ["skrim", "stord", "bø"],
    "daniel": ["oslo", "varden", "scotland"],
}

for username, userinfo in sorted(favourite_places.items()):
    print(f"\n{username.title()}'s favourite places are:")
    for userinf in userinfo:
        print(f"\t{userinf.title()}")
#         "place_one": "sandefjord",
#         "place_two": "larvik",
#         "place_three": "bø",
#     }
#     "lesh": {
#         "place_one": "skrim",
#         "place_two": "stord",
#         "place_three": "bø",
#     }
#     "daniel": {
#         "place_one": "oslo",
#         "place_two": "varden",
#         "place_three": "scotland",
#     }
# }
#
# for username, userinfo in favourite_places.items():
#     print(f"\nUsername: {username}")
#     place_one = userinfo['place_one']
#     place_two = userinfo['place_two']
#     place_three = userinfo['place_three']
#
#     print(f"\t{username}'s favourite places are,")
#




# favourite_places = {
#     friend1 = {"oskar": ["sandefjord", "oslo", "bærum",],}
#     "bigb": ["sandefjord",],
#     "nina": ["oslo", "bærum",],
# }
