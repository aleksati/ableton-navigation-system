SYNTH = {
    "ArpBass": 1,
    "Brass": 2,
    "Bass": 3, 
    "Laat5Intro": 4,
    "Sun": 5,
    "Blade": 6,
    "OrgelBass": 7,
}

SCENE = {
    "Laat 1 - Scene 1" : 1,
    "Laat 2 - Scene 2" : 2,
    "Laat 3 - Scene 3" : 3,
    "Laat 4 - Scene 4" : 4,
    "Laat 4 - Scene 5" : 5, 
    "Laat 4 - Scene 6" : 6,
    "Laat 4 - Scene 7" : 7,
    "Laat 5 - Scene 8" : 8,
    "Laat 5 - Scene 9" : 9,
    "Laat 5 - Scene 10" : 10,
    "Laat 6 - Scene 11" : 11,
    "Laat 7 - Scene 12" : 12, 
    "Laat 8 - Scene 13" : 13, 
}

# scene : synths
SCENE_CONFIG = {
    SCENE["Laat 1 - Scene 1"] : [SYNTH["Bass"], SYNTH["ArpBass"]], # Laat 1
    SCENE["Laat 2 - Scene 2"] : [SYNTH["Brass"], SYNTH["Bass"], SYNTH["Brass"], SYNTH["Bass"]], # Laat 2
    SCENE["Laat 3 - Scene 3"] : [SYNTH["Brass"], SYNTH["Bass"], SYNTH["ArpBass"], SYNTH["Bass"]], # Laat 3
    SCENE["Laat 4 - Scene 4"] : [SYNTH["Brass"]], # Laat 4 - Intro
    SCENE["Laat 4 - Scene 5"] : [SYNTH["Sun"]], # Laat 4 - Vers med playback bass
    SCENE["Laat 4 - Scene 6"] : [SYNTH["Brass"]], # Laat 4 - Solo Bridge med playback bass
    SCENE["Laat 4 - Scene 7"] : [SYNTH["Brass"]], # Laat 4 - Outro med playback bass
    SCENE["Laat 5 - Scene 8"] : [SYNTH["Laat5Intro"]], # Laat 5 - Intro
    SCENE["Laat 5 - Scene 9"] : [SYNTH["Bass"]], # Laat 5 - Refreng 
    SCENE["Laat 5 - Scene 10"] : [SYNTH["Bass"], SYNTH["Laat5Intro"], SYNTH["Bass"], SYNTH["Sun"]], # Laat 5 - Bridge and out
    SCENE["Laat 6 - Scene 11"] : [SYNTH["Blade"], SYNTH["OrgelBass"], SYNTH["Blade"], SYNTH["ArpBass"]], # Laat 6
    SCENE["Laat 7 - Scene 12"] : [SYNTH["OrgelBass"]], # Laat 7
    SCENE["Laat 8 - Scene 13"] : [SYNTH["OrgelBass"], SYNTH["ArpBass"]], # Laat 8
}

####### MIDI KEYBOARD INFO ########
####### RUN "keyboard-test.py" TO FIND CORRECT VALUES ######## 
SYNTH_NOTE = 57 #the note number of the button that triggers a new synth.
SCENE_NOTE = 68 #the note number of the button that trigger the next scene.

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