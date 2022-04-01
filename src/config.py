# synth 0 = OpenBass
# synth 1 = ArpBass
# synth 2 = Brass
# synth 3 = LongBass
# synth 4 = Laat5Intro
# synth 5 = SunLead
# synth 6 = BladeLead
# synth 7 = OrganBass

SCENE_CONFIG = {
    1 : [0, 1], # Laat 1
    2 : [2, 3, 2, 3], # Laat 2
    3 : [2, 3, 1, 3], # Laat 3
    4 : [2, 5], # Laat 4 - Intro og solo
    5 : [2], # Laat 4 - Outro 
    6 : [4], # Laat 5 - Intro
    7 : [3], # Laat 5 - Refreng 
    8 : [3, 4, 3, 5], # Laat 5 - Bridge and out
    9 : [6, 7, 6, 1], # Laat 6
    10: [7, 1], # Laat 8
}

####### MIDI KEYBOARD INFO ########
####### RUN "keyboard-test.py" TO FIND CORRECT VALUES ######## 
SYNTH_NOTE = 68 #the note number of the button that triggers a new synth.
SCENE_NOTE = 57 #the note number of the button that trigger the next scene.

VOLUME_NOTE = 7 #the note number of the dial that control the volume
LOWPASS_NOTE = 10 #the note number of the dial that control the lowpass filtering
REVERB_NOTE = 11 #the note number of the dial that controls the reverb amount 

START_NOTE = 66 #the note number of the button that toggles start
STOP_NOTE = 65 #the note number of the button that toggles stop

MIDI_CHAN = 176 #the MIDI channel of the buttons of the MIDI-keyboard, not the keys
NOTE_ON = 127 #the note-on MIDI value
NOTE_OFF = 0 #the note-off MIDI value

#to avoid conflict with other MIDI events on the same channel, we offset all our filtered message to very high midi notes.
#this value defines the highest possible note we can use for triggering events. all our events will occur just below this value.
HIGH_NOTE = 120