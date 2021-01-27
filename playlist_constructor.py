from itertools import count


def add_missing_tracks(sp, playlist_id, final_tracks):
    to_add_tracks = final_tracks

    current_tracks = []
    for i in count(0):
        current_tracks_call = sp.playlist_tracks(playlist_id, fields="items", offset=(100 * i))
        current_tracks.append(current_tracks_call)
        if len(current_tracks_call['items']) == 0:
            break

    for i in range(0, len(current_tracks)):
        for track in current_tracks[i]['items']:
            if track['track']['id'] in to_add_tracks:
                to_add_tracks.remove(track['track']['id'])

    for i in range(0, len(to_add_tracks), 100):
        sp.user_playlist_add_tracks(sp.current_user()['id'], playlist_id, to_add_tracks[i:i+100])


def remove_additional_tracks(sp, playlist_id, final_tracks):
    current_tracks = sp.playlist_tracks(playlist_id, fields="items")
    for track in current_tracks['items']:
        if track['track']['id'] not in final_tracks:
            sp.playlist_remove_all_occurrences_of_items(playlist_id, [track['track']['id']])


def get_playlist(sp, name):
    user_playlists = []

    for i in count(0):
        user_playlists_call = sp.current_user_playlists(limit=50, offset=(50 * i))
        user_playlists.append(user_playlists_call)
        if len(user_playlists_call['items']) == 0:
            break

    for i in range(0, len(user_playlists)):
        for playlist in user_playlists[i]['items']:
            if playlist['name'] == name:
                return playlist['id']

    return sp.user_playlist_create(sp.current_user()['id'], name)['id']


def playlist_constructor(sp, parsed_playlists):
    for i, create_playlist in enumerate(parsed_playlists):
        print("Creating playlist " + create_playlist['Name'])

        playlist_id = get_playlist(sp, create_playlist['Name'])

        remove_additional_tracks(sp, playlist_id, create_playlist['Tracks'])
        add_missing_tracks(sp, playlist_id, create_playlist['Tracks'])
