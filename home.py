import pygame
import sys

def getdate():
    import datetime
    return datetime.datetime.now()
def water():
    f=open("water_detail.txt","w")
    f.write(str(getdate()),"you drank")
def eye():
    f=open("eye_detail","w")
    f.write("eye clear:")
def excercise():
    f=open("water_detail.txt","w")
    f.write("you done  your exercise at:")


from pygame import mixer 
  
# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("alan_walker.mp3") 

# Setting the volume 
mixer.music.set_volume(0.7) 
  
# Start playing the song 
#mixer.music.play() 
  
# infinite loop 
while True: 
      
    print("Press 'p' to pause, 'r' to resume") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
      
    if query == 'p': 
  
        # Pausing the music 
        #mixer.music.pause()
        mixer.music.play()
        water() 
        time.sleep(1800)
pass
    elif query == 'r': 
  
        # Resuming the music 
        mixer.music.unpause() 
    elif query == 'e': 
  
        # Stop the mixer 
        mixer.music.stop() 
        break