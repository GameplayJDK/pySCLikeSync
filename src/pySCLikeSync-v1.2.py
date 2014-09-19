#!/usr/bin/env python2.7
# pySCLikeSync.py by GameplayJDK,
# Copyright 2014 (c) GameplayJDK.de,
# All rights reserved until further notice
import sys
import soundcloud
import urllib
import os
import glob
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
    print pre+"Loading liked tracks... ('http://www.soundcloud.com/"+tr_user+"/likes')"
    tracks = client.get('/users/'+tr_user+'/favorites', limit=tr_limit)
    print pre+"Loaded '"+str(len(tracks))+"' tracks."
    print pre+"Scanning for existing tracks..."
    count = 0
    toskip = []
    if os.path.isfile("track_id_store"):
        lines = open("track_id_store", 'r')
        for line in lines.readlines():
            toskip.append(line.strip("\n"))
            count = count+1
            print pre+"'"+str(count)+"': "+line.strip("\n")
        lines.close()
    track_id_store = open("track_id_store", 'w')
    print pre+"Scanned. Found '"+str(count)+"' existing tracks."
    count = 0
    print pre+"Downloading new tracks..."
    for track in tracks:
        t_name = track.title
        t_url = client.get(track.stream_url, allow_redirects=False).location
        t_id = track.id
        if str(t_id) not in toskip:
            try:
                urllib.urlretrieve(t_url, t_name+".mp3")
                cound = count+1
                track_id_store.write(str(t_id)+"\n")
                print pre+"Successfully downloaded '"+t_url+"' to '"+t_name+".mp3'."
            except:
                print pre+"Failed to download '"+t_url+"' to '"+t_name+".mp3'."
        else:
            print pre+"Skipped download of '"+t_url+"' to '"+t_name+".mp3'."
    track_id_store.close()
    print pre+"Downloaded '"+str(count)+"/"+str(len(tracks))+"'' tracks."
    count = 0
    globbed = glob.glob("*.mp3")
    print pre+"Tracks in '"+os.getcwd()+"': ("+str(len(globbed))+")"
    for mp3f in globbed:
        print pre+"- "+mp3f
    # *** -Python code ***
except Exception, ex:
    print pre+"Failed to run the program properly!"
    print pre+"Please report this error ('"+str(ex)+"') to the official issue tracker at 'https://github.com/GameplayJDK/pySCLikeSync/issues' or view the README.md at 'https://github.com/GameplayJDK/pySCLikeSync/blob/master/README.md' and visit the wiki at 'https://github.com/GameplayJDK/pySCLikeSync/wiki' to read about common errors."
