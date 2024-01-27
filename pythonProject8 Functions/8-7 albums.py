def make_album(artist, title, tracks=None):
    '''return a dictionary of information about an album.'''
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict



musician = make_album('leo', 'bangers', tracks=4)
print(musician)
musician = make_album('pål', 'slammers')
print(musician)