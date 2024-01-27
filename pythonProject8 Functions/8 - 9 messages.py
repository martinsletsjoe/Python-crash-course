# def show_messages(messages):
#     '''make a list containing a series of short text messages.'''
#     for message in messages:
#         print(message)
#
# text_message = ["hi", "k", "hello", "yo"]
# show_messages(text_message)

def send_messages(messages, sent_messages):
    '''simulate printing each message until none are left.'''
    while messages:
        writing_message = messages.pop()
        print(f"sending message: {writing_message}")
        sent_messages.append(writing_message)

def show_messages(messages):
    '''make a list containing a series of short text messages.'''
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

messages = ["yo", "hi", "k", "hello", "sup"]
sent_messages = []

send_messages(messages[:], sent_messages)
show_messages(sent_messages)

print(messages)