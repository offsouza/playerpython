#!/usr/bin/python

import omxplayer.player
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import os
import sys



#video = "/home/pi/Downloads/"
#video = os.listdir("/home/pi/Downloads/")



p=0
while True:
   try:
    video = os.listdir("/home/pi/Googledrive/videointer/")
    print video
    for i in video:
        video = os.listdir("/home/pi/Googledrive/videointer/")
        
        if i.lower().endswith(".mp4"):

            
            
            try:
                
                #pygame.init()
                #tela = pygame.display.set_mode ((1024, 768), pygame.FULLSCREEN)
                player.quit()
            except:
                pass
            
            player = OMXPlayer("/home/pi/Googledrive/videointer/"+str(i))    

            sleep(1)

            
            
                        
            
            print i
            
            
            tempo = 0
            tempo = player.duration()
            print tempo
            #print player

            #       sleep(tempo-3)
            #player.pause()

            #player2 = player
            
            s = 0
            while s < tempo-3:
                
              try:
                  
                  s += 1
                  sleep(1)
                                    
              except KeyboardInterrupt:
                  player.quit()
                  sys.exit()
   except:
           pass
            
   p+=1
    
    
