import time
import datetime
import pygame

class alarm:
    
    def __init__(self,alarm_time):
        self.alarm_time=alarm_time
        print(f"Alarm is set for:{alarm_time}")
    
    def get_current_time(self):
      return datetime.datetime.now().strftime("%H:%M:%S") 
        
        
       
class Clock(alarm):
    def __init__(self,alarm_time):
        
        super().__init__(alarm_time)
        self.soundfile="alarm.mp3"
        self.is_running=True
        self.end = None
       
    def alarm_clock(self):
        while self.is_running:
            current_time=self.get_current_time()
            print(current_time)
            
            if current_time== self.alarm_time:
                 print("WAKE UP ! 🛌")
        
                 pygame.mixer.init()  # mixer is a module
                 pygame.mixer.music.load(self.soundfile) # ascessing the pygame and ascessing the mixer module and ascessing music of module mixer and loading the sound
                 pygame.mixer.music.play()
                 
                 self.end=input("Enter O to turn off the alarm:").lower()       
                 if self.end=="o":
                     pygame.mixer.music.stop()
                     self.is_running=False
            time.sleep(1)     
         

if __name__=="__main__" :
    user_time=input("enter you alarm time(HH:MM:SS) :")
    
    my_clock=Clock(user_time)  # my clock is the object of class clock
    my_clock.alarm_clock()  # ascessing the function inside the class clock
    
