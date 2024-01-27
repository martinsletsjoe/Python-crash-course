#Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

def sandwiches(*contents):
    '''summarize the sandwich we about to make.'''
    print("\nMaking a sandwich with the following contents:")
    for content in contents:
        print(f"- {content}")

sandwiches('cheese')
sandwiches('pickled onions', 'radish')
sandwiches('brunost', 'gulost', 'banos')