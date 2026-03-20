This is for the music guessing game we sometimes play on stream.

If you want to add a song that we have to guess (try to pick stuff that is somewhat popular, otherwise most people can't guess it) go to https://tkap1.github.io/guess_music/
and click on any song. A python line of code will be copied to your clipboard (look at the `data` array in `main.py`). Then add it to `main.py` and make a pull request, or paste it in my chat and I will add it.

If the song comes from a show/movie/anime/whatever and that thing is not in the name of the song, you can add `tags` property to allow the song to be guessed by using extra keywords (look at `main.py` for examples)
You can also change where the song starts (default is at 5000 milliseconds) by using the `start` property
