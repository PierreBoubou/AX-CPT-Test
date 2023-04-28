from pynput import keyboard


class MyOVBox(OVBox):
    def __init__(self):
        OVBox.__init__(self)
        self.listener = None
        self.stimCode = 33035

    def initialize(self):
        self.output[0].append(OVStimulationHeader(0., 0.))
        self.listener = keyboard.Listener(on_press=self.on_press) #we start one at first
        self.listener.start()
        return
    
    def on_press(self,key):
        stimSet = OVStimulationSet(self.getCurrentTime(), self.getCurrentTime()+1./self.getClock()) #the set containing the stim
        stimSet.append(OVStimulation(self.stimCode, self.getCurrentTime(), 0)) #we add the stim
        self.output[0].append(stimSet) #append our set to the stimulations output
          
    def process(self):
        if not self.listener.running: #if there is one running we let him and dont launch other
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
        return

    def uninitialize(self):
        self.listener.stop() 
        self.output[0].append(OVStimulationHeader(self.getCurrentTime(),self.getCurrentTime()))
        return

box = MyOVBox()