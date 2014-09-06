#!/usr/bin/env python2.7
# pySCLikeSync.py by GameplayJDK,
# Copyright 2014 (c) GameplayJDK.de,
# All rights reserved until further notice
import sys
import time
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
    print pre+"Loading tracks..."
    tracks = client.get('/users/'+tr_user+'/favorites', limit=tr_limit)
    url_cache = []
    id_cache = []
    name_cache = []
    t_sf_c = 0
    t_ff_c = 0
    print pre+"Fetching tracks..."
    for track in tracks:
        try:
            t_url = client.get(track.stream_url, allow_redirects=False).location
            t_id = track.id
            t_name = track.title
            url_cache.append(t_url)
            id_cache.append(str(t_id))
            name_cache.append(t_name)
            t_sf_c = t_sf_c+1
            print pre+"Added track '"+str(t_sf_c)+"' stream from '"+t_url+"' named '"+t_name+"' with id '"+str(t_id)+"'."
        except Exception, ex:
            t_sf_c = t_sf_c+1
            t_ff_c = t_ff_c+1
            print pre+"Skipped track '"+str(t_sf_c)+"' due to an error."
    print pre+"Fetched tracks. There were '"+str(t_sf_c)+"' fetchable tracks, '"+str(t_ff_c)+"' of them have been skipped!"
    existing = []
    if (os.path.isfile("track_id_store")):
        lines = open("track_id_store", 'r')
        for line in lines.readlines():
            existing.append(line.strip("\n"))
        lines.close()
    track_id_store = open("track_id_store", 'w')
    t_sd_c = 0
    t_fd_c = 0
    print pre+"Downloading previously fetched tracks..."
    for c in range(len(url_cache)):
        t_sd_c = t_sd_c+1
        try:
            t_url = url_cache[c]
            t_id = int(id_cache[c])
            t_name = name_cache[c]
            if (str(t_id) not in existing):
                print pre+"Downloading new track named '"+t_name+".mp3' with id '"+str(t_id)+"' from '"+t_url+"'."
                urllib.urlretrieve(t_url, t_name+".mp3")
                track_id_store.write(str(t_id)+"\n")
            else:
                print pre+"Track does already exist. Skipped."
                t_fd_c = t_fd_c+1
        except:
            print pre+"Skipped track due to an error."
            t_fd_c = t_fd_c+1
    print pre+"Downloaded previously fetched tracks. There were '"+str(t_sd_c)+"' downloadable tracks, '"+str(t_fd_c)+"' of them have been skipped!"
    print pre+"All files have been saved to '"+os.getcwd()+"' ('"+str(len(glob.glob("*.mp3")))+"' mp3 files):"
    f_c = 0
    for mp3f in glob.glob("*.mp3"):
        f_c = f_c+1
        print pre+"("+str(f_c)+") - "+mp3f
    # *** -Python code ***
except:
    print pre+"An error occurred while running the program!"
