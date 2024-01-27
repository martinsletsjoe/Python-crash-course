def make_album(artist, title, tracks=None):
    '''return a dictionary of information about an album.'''
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

while True:
    print("\nWhat album would you like?")
    print("(enter 'q' at any time to quit")

    artist_name = input("enter artist name ")
    if artist_name == 'q':
        break
    album_name = input("enter the title ")
    if album_name == 'q':
        break
    album = make_album(artist_name, album_name)
    print(album)
print("\nThanks for responding!")