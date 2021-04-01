#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 08:35:24 2021

@author: amyaporteons
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= '601b526255fa49e9b4197e6493f748a3',
                                                           client_secret= '5e6e840cc98d48ee8d72505d081d6b17'))



def get_categories():
    categories = []
    r = sp.categories(country= 'US', locale= 'en_US', limit=50, offset=0)
    for i in r.values():
        y = i['items']
        for z in y:
            categories.append(z['id'])
    return(categories)
              
    
#get_categories()


def get_playlist(categories):
    playlist = []
    for k in categories:
        
        art = sp.category_playlists(category_id=(k),limit=1)
        
        for i in art.values():
            t = i['items']
            for v in t:
                playlist.append(v['id'])
        print(playlist)
    
                
               
            
  

