# Spotify Playlist Manager

Automatically create Spotify playlists by combining existing ones!

## Installation

1. Clone the repository using `git clone https://github.com/ShiromMakkad/SpotifyPlaylistManager.git`
2. Install [Python](https://www.python.org/)
3. Install [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/) with `pip install spotipy`

## Usage

### Importing folders

Unfortunately, Spotify doesn't allow you to get folder data from their web API. 
To get folder information, this uses [mikez/spotify-folders](https://github.com/mikez/spotify-folders). 

To get the folder structure, 
1. Download [mikez/spotify-folders](https://github.com/mikez/spotify-folders) with `curl -L https://git.io/folders > spotify-folders && chmod +x spotify-folders`
2. Copy your [Spotify cache folder](https://support.spotify.com/us/article/storage-and-data-information/) to the same directory as spotify-folders. 
3. Run `spotify-folders --cache ./Storage > folders.json`
4. Copy `folders.json` into the same directory as `main.py`


See [mikez/spotify-folders](https://github.com/mikez/spotify-folders) for more information. 

### Get your client id and secret

See [App Settings | Spotify for Developers](https://developer.spotify.com/documentation/general/guides/app-settings/). Once you have the `client_id` and `client_secret`, fill them into the playlist configuration below.  

### Playlist Configuration

You'll need to create a `configuration.json` file in the same directory as `main.py`. Here is an example `configuration.json`:

```
{
  "client_id": "",
  "client_secret": "",
  "playlists": [
    {
      "Name": "All",
      "Playlists": [
        "*"
      ]
    },
    {
      "Name": "Pop",
      "Playlists": [
        "Pop/*"
      ]
    },
    {
      "Name": "Modern Pop",
      "Playlists": [
        "Pop/Modern/*"
      ]
    },
    {
      "Name": "Chill",
      "Playlists": [
        "Rap/Mellow/*",
        "Electro/Chill/*"
      ]
    }
  ]
}
```

The example above creates four playlists named `All`, `Pop`, `Modern Pop`, and `Chill`. 
- All contains every saved playlist's songs. 
- Pop contains every playlist in the folder `Pop` including subfolders. 
- Modern Pop only contains the playlists in the `Pop/Modern` folder. All these playlists will be included in `Pop/*` but will exclude other folders (for example `Pop/80s` wouldn't be in `Pop/Modern/*` but would be in `Pop/*`).
- Chill contains every playlist in `Rap/Mellow/*` AND `Electro/Chill/*`

##### Configuration tips:

- You can create as many playlists as you want, not just 4, just add them to the list in the same format shown above
- `/*` includes every playlist including subfolders. 
- You can create a playlist out of as many subfolders/subplaylists you want. The largest example above was two, but you can add more.  
