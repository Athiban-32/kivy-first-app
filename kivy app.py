#Import the modules
from kivy.app import App
from kivy.uix.label import Label

#define the base class of the kivy app
class firstapp(App):
    
    def build(self):
        
        #Initialize the label with any text
        
        return Label(text='Hii this is Xcode Emulators Welcome to my youtube channel')
    
if __name__=='__main__':
    #firstapp is initialized and its run() method is

   firstapp().run()    