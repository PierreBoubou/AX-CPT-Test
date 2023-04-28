import tkinter as tk

class MyOVBox(OVBox):
   def __init__(self):
        OVBox.__init__(self) 
        self.root = None
        self.label = None

   def initialize(self):
        # Parameters fetch
        self.width = int(self.setting['Window_width'])
        self.length = int(self.setting['Window_length'])
        self.fontsize = int(self.setting['Font_size'])
        self.lettercolor = str(self.setting['Font_color'])
        # Parameters initialisation
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.geometry("{}x{}".format(self.width, self.length))
        self.centerX = self.width//2
        self.centerY = self.length//2
        self.label = tk.Label(self.root, font=("Arial", self.fontsize), bg="black", fg=self.lettercolor)
        self.label.place(x=self.centerX, y=self.centerY, anchor="center")
        self.label.configure(text="")
        self.root.update()
        return

   def process(self):
      for chunkIndex in range( len(self.input[0]) ):
         chunk = self.input[0].pop() #getting the first chunk in queue
         if(type(chunk) == OVStimulationSet):
            # We move through all the stimulation received in the StimulationSet and
            for stimIdx in range(len(chunk)):
                stim=chunk.pop();
                if(stim.identifier == 33028): #nettoyage
                    self.label.configure(text="")
                    self.root.update()
                elif(stim.identifier == 33024): #image
                    self.label.configure(text="A")
                    self.root.update()
                elif(stim.identifier == 33026): #image
                    self.label.configure(text="X")
                    self.root.update()
                elif(stim.identifier == 33025): #image
                    self.label.configure(text="B")
                    self.root.update()
                elif(stim.identifier == 33027): #image
                    self.label.configure(text="Y")
                    self.root.update()
                elif(stim.identifier == 33031): #image
                    self.label.configure(text="1")
                    self.root.update()
                elif(stim.identifier == 33032): #image
                    self.label.configure(text="2")
                    self.root.update()
                elif(stim.identifier == 33033): #image
                    self.label.configure(text="3")
                    self.root.update()
                elif(stim.identifier == 33034): #image
                    self.label.configure(text="4")
                    self.root.update()
                elif(stim.identifier == 33035): #image
                    self.label.configure(text="5")
                    self.root.update()
                elif(stim.identifier == 33036): #image
                    self.label.configure(text="END")
                    self.root.update()
                
         else:
            print('Received chunk of type ', type(chunk), " looking for StimulationSet")

      return

   def uninitialize(self):
      self.root.destroy()
      return

box = MyOVBox()