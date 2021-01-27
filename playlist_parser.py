import json

def add_specific_playlist(sp, parent_folder, playlist_name, parsed_playlists):
    for child in parent_folder['children']:
        if child['type'] == 'playlist':
            # We have to get the name from the spotify api since the JSON only gives us folder names, not playlist names
            name = sp.playlist(child['uri'], fields="name")['name']
            if name == playlist_name:
                parsed_playlists.append(child['uri'])
                return

def add_all_playlists(parent_folder, parsed_playlists):
    for child in parent_folder['children']:
        if child['type'] == 'playlist':
            parsed_playlists.append(child['uri'])
        if child['type'] == 'folder':
            add_all_playlists(child, parsed_playlists)

def playlist_parser(sp, playlists):
    playlist_folder_data = json.load(open("folders.json"));
    parsed_playlists = playlists

    for i, create_playlist in enumerate(playlists):
        parsed_component_playlist = []
        for component_playlist in create_playlist["Playlists"]:
            # Go through each component playlist and find the parent folder of the final playlist
            directory = component_playlist.split("/")
            playlist_name = directory.pop()
            parent_folder = playlist_folder_data
            for item in directory:
                if parent_folder['type'] == "folder":
                    for child_folder in parent_folder["children"]:
                        if child_folder['type'] == 'folder' and child_folder['name'] == item:
                            parent_folder = child_folder
                            break
                elif parent_folder['type'] == "playlist":
                    raise Exception("folders.json must describe folder structure!")

            before_playlist_add = len(parsed_component_playlist)

            if playlist_name == "*":
                add_all_playlists(parent_folder, parsed_component_playlist)
            else:
                add_specific_playlist(sp, parent_folder, playlist_name, parsed_component_playlist)

            if len(parsed_component_playlist) - before_playlist_add == 0:
                raise Exception("No playlists found! Check your path!")

        parsed_playlists[i]["Playlists"] = parsed_component_playlist

    return parsed_playlists