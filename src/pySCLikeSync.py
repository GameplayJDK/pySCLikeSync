#!/usr/bin/env python2.7
# pySCLikeSync.py by GameplayJDK,
# Copyright 2014 (c) GameplayJDK.de,
# All rights reserved until further notice
import sys
import time
import soundcloud
import urllib
# Prefix for all console output
pre = "[pySCLikeSync] "
# INFO: never show your account information to others!
try:
    # The ClientID
    cli_id = sys.argv[1]
    # The ClientSecret
    cli_se = sys.argv[2]
    # Your email address:
    usr_nm = sys.argv[3]
    # Your password:
    usr_pw = sys.argv[4]
    # The name of the target user
    tr_user = sys.argv[5]
    # The limit of tracks to load
    tr_limit = sys.argv[6]
    # *** +Python code ***
    print pre+"Signing in as client..."
    client = soundcloud.Client(client_id=cli_id,client_secret=cli_se,username=usr_nm,password=usr_pw)
    print pre+"Signed in."
    print pre+"Loading tracks..."
    tracks = client.get('/users/'+tr_user+'/favorites', limit=tr_limit)
    n = 1
    cache = "url_cache_t."+str(int(round(time.time() * 1000)))+".txt"
    txtfile = open(cache, 'w')
    for track in tracks:
        try:
            track_title = track.title
            track_stream_url = client.get(track.stream_url, allow_redirects=False).location
            print pre+"(n"+str(n)+") found '"+track_title+"' at '"+track_stream_url+"'."
            txtfile.write(track_stream_url+'\n');
            try:
                urllib.urlretrieve(track_stream_url, track_title+".mp3")
                print "Downloaded '"+track_stream_url+"' to '"+track_title+".mp3'."
            except:
                print "Couldn't download '"+track_stream_url+"' to '"+track_title+"'!"
        except:
            print pre+"(n"+str(n)+") found 'NULL' at 'NULL'. (Error)"
        n = n+1
    txtfile.close()
    print pre+"Done."
    # *** -Python code ***
except:
    print pre+"An error occurred while running the program!"
