pySCLikeSync
============

A simple soundcloud downloader written in python (2.7).

It does require 2 moduels (install them via `pip install <module>`).

* [Soundcloud](https://github.com/soundcloud/soundcloud-python) e.g. `pip install soundcloud`
* [mutagen](https://bitbucket.org/lazka/mutagen) e.g. `pip install mutagen` (ignored < 1.3)

On linux the `pip` commands might require `sudo` access. It only works with python 2.7 due to the print-print()-changes and the urllib module, which is removed in python 3.X (until it's installed manually). Currently there are no plans to release a port to python 3.4, since python 2.7 is still the commonly preinstalled version on linux os.

If the download of one track seems to take too long and there is no significant change to the filesize, use `CTRL + C` to interrupt the current download and skip it (this doesn't remove the t_id and the file!).

Download it:
* [v1.0](http://download1324.mediafire.com/m142bqeg5ikg/zt4x9ixu56rw4b5/pySCLikeSync-v1.0.py)
* [v1.1](http://download944.mediafire.com/501ls0eo9pfg/7oryhqnbjzrn8ec/pySCLikeSync-v1.1.py)
* [v1.2](http://download1512.mediafire.com/zsv071ksr6vg/2s3tbob9pzu27f3/pySCLikeSync-v1.2.py)

The mf download may need up 3 seconds to (re)start.

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
