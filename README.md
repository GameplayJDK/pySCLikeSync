pySCLikeSync
============

A simple soundcloud downloader written in python (2.7).

It does require 2 moduels (install them via `pip install <module>`).

* [Soundcloud](https://github.com/soundcloud/soundcloud-python) e.g. `pip install soundcloud`
* [mutagen](https://bitbucket.org/lazka/mutagen) e.g. `pip install mutagen` (ignored < 1.3)

On linux the `pip` commands might require `sudo` access.

This script only works with python 2.7 due to the print-print()-changes and the urllib module, which is removed in python 3.X (until it's installed manually). Currently there are no plans to release a port to python 3.4, since python 2.7 is still the commonly preinstalled version on linux os.

If the download process of one track seems to take too long and there is no significant change to the filesize, use `CTRL + C` to interrupt the current download and skip it. This doesn't remove the t_id and the file, so you might need to remove those by hand.

Download it:
* v1.0 ( [direct](http://download1324.mediafire.com/m142bqeg5ikg/zt4x9ixu56rw4b5/pySCLikeSync-v1.0.py) ) ( [mirror](http://www.mediafire.com/download/zt4x9ixu56rw4b5/pySCLikeSync-v1.0.py) )
* v1.1 ( [direct](http://download944.mediafire.com/501ls0eo9pfg/7oryhqnbjzrn8ec/pySCLikeSync-v1.1.py) ) ( [mirror](http://www.mediafire.com/download/7oryhqnbjzrn8ec/pySCLikeSync-v1.1.py) )
* v1.2 ( [direct](http://download1585.mediafire.com/xpdssbdehpjg/2s3tbob9pzu27f3/pySCLikeSync-v1.2.py) ) ( [mirror](http://www.mediafire.com/download/2s3tbob9pzu27f3/pySCLikeSync-v1.2.py) )
* v1.3 ( [direct](http://download948.mediafire.com/t4y1n666z76g/npogv6z93z9v16f/pySCLikeSync-v1.3.py) ) ( [mirror](http://www.mediafire.com/download/npogv6z93z9v16f/pySCLikeSync-v1.3.py) )

The 'direct' mf download may need up to 3 seconds to (re)start.

__I recommend you [this tutorial](http://gameplayjdk.wordpress.com/2014/07/28/tutorial-how-to-use-pysclikesync-to-download-your-favourite-tracks-from-soundcloud-28-07-2014/) to get familiar with the use of pySCLikeSync on my wordpress blog.__

You can use Sublime Text 2 (or 3) to edit the files since the related `.sublime-project` file is contained. I don't recommend you to use the contained `.sublime-workspace` file tho', because it's optimized for my system (`eOS freya b1`) and will produce a few errors if you use it 'as-is' on your computer.

Currently it supports:
* Fetching urls from the soundcloud api
* Downloading the tracks (with automatic naming)
* Avoiding duplications (by caching every id in `track_id_store`)
* Error handling (in case of a fatal error the user get a recommendation to report the bug or to visit the wiki to read about common errors)

It will support:
* Proper fail detection (check for nulled size)
* Proper error handling (error reports)
* TUI (later it may also have basic GUI)
* Automated ID3-Tagging (creating and updating)
* Detailed track range configuration (settable track offset)
* Optional naming pattern for the files (id, title, etc.)
* Logging (output to file and console)
* Message type (long, short or detailed)
* Named argument (`--<ARGN> <ARGV> ...`)
* Support for url export to a file (to use a dlmgr/prg like `wget` for downloading)
* Functions and multithreading (`code impl-`)
* Keep old id's in list (`open("teack_id_store", 'a')`)

Known bugs are:
* Some downloads fail (the cause is unknwon, you might have to run the downloader twice, in different directories to get get all tracks; You might want to use the [manual browser-based method](http://gameplayjdk.wordpress.com/2014/01/10/how-to-download-any-track-from-soundcloud-com-10-01-2014/) if you only need one or two single tracks; in v1.0, v1.1, v1.2, v1.3)
* The `track_id_store` file is overwritten, so older downloads are removed from the list of existing tracks (the script uses `w`, which overwrites the old content, instead of `a`, which appends to the file; in v1.1, v1.2)
* Some downloads freeze (caused by outdated AWS-keys; in v1.1 only)
* Resource `track_id_store` never gets released, missing `<strm>.close()` (which suppresses saving any t_id to the file; in [this commit (initial/f)](https://github.com/GameplayJDK/pySCLikeSync/commit/1c780f01b4954aab4cad8a1dcedcb099041d2600) (1c780f0) of v1.1 only)
* Missing `<strm>.flush()` (which causes all t_id elements to be written as `<strm>.close()` is called; in [this commit](https://github.com/GameplayJDK/pySCLikeSync/commit/07178d83d5480b5ffafcc4ea612f21669262c188) (07178d8) of v1.2 only)
* Uncought exception for httpStatusCode-404 (which lets the program stop with a fatal tl-error; in [this commit](https://github.com/GameplayJDK/pySCLikeSync/commit/1dfbeeaa79edbb456cb2a54895f70fa8b4c2ca2b) (1dfbeea) of v1.2 only)

pySCLikeSync.py is Copyright 2014 of GameplayJDK and registered under GPLv3 which you can find [here](https://raw.githubusercontent.com/GameplayJDK/pySCLikeSync/master/LICENSE).
```python
[...]
# pySCLikeSync.py by GameplayJDK,
# Copyright 2014 (c) GameplayJDK.de,
# All rights reserved until further notice
[...]
```
pySCLikeSync is registered under GPLv3. Please read [LICENSE](LICENSE) for more information.

(Last updated `Mi Okt 22 \n 11:08`)
