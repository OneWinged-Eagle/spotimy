# spotimy

Making some playlists of (loosely) alike tracks from your followed artists' albums and singles' tracks.

It's still a WIP, like maybe some better visualisation, but it looks like it works pretty well.

Don't forget to change the values in the `config.py`!

Since there is some sort of timeout with spotify's API, I divided the multiple API calls in different scripts, so you have to call them scripts by scripts (yeah, pretty lame, I will hopefully fix that later).

So, first, you wanna get the artists, then the albums, then the tracks, then the audio features.
With that, you can finally run the actual algorithm et get `config.max_cluster` sets of centroids.
You'll get the classical WCSS graph to help you choose how many playlists will be better for your tracks.
Change the `config.nb_playlists` with that in mind, get the indexes and finally make the playlists.

Welp, that's pretty much it, not very user friendly right now but, as I said, I'll look into that.
