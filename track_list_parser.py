def track_list_parser(sp, parsed_playlists, duplicates=False):
    print()
    for i, create_playlist in enumerate(parsed_playlists):
        parsed_playlists[i]['Tracks'] = []
        for uri in create_playlist["Playlists"]:
            tracks = sp.playlist_tracks(uri.split(':')[2], fields="items")
            for track in tracks['items']:
                if track['track']['id'] in parsed_playlists[i]['Tracks']:
                    print("Creating " + create_playlist['Name'] + ": " + track['track']['name'] + " is a duplicate!")
                    if not duplicates:
                        continue
                parsed_playlists[i]['Tracks'].append(track['track']['id'])
    print()