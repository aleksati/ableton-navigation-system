SYNTHS = {
    "ArpBass": 0,
    "Brass": 1,
    "Bass": 2, 
    "Laat5Intro": 3,
    "Sun": 4,
    "Sun2": 5,
    "Blade": 6,
    "OrgelBass": 7,
}

SCENES = {
    "Laat 1 - Scene 1" : 0,
    "Laat 1 - Scene 2" : 1,
    "Laat 2 - Scene 3" : 2,
    "Laat 3 - Scene 4" : 3,
    "Laat 4 - Scene 5" : 4,
    "Laat 4 - Scene 6" : 5, 
    "Laat 4 - Scene 7" : 6,
    "Laat 4 - Scene 8" : 7,
    "Laat 5 - Scene 9" : 8,
    "Laat 5 - Scene 10" : 9,
    "Laat 5 - Scene 11" : 10,
    "Laat 6 - Scene 12" : 11,
    "Laat 7 - Scene 13" : 12, 
    "Laat 8 - Scene 14" : 13, 
}

SCENE_CONFIG = {
    SCENES["Laat 1 - Scene 1"] : [SYNTHS["Bass"]], # Laat 1
    SCENES["Laat 1 - Scene 2"] : [SYNTHS["Bass"]], # Laat 1 bridge og ut
    SCENES["Laat 2 - Scene 3"] : [SYNTHS["Brass"], SYNTHS["Bass"], SYNTHS["Brass"], SYNTHS["Bass"]], # Laat 2
    SCENES["Laat 3 - Scene 4"] : [SYNTHS["Brass"], SYNTHS["Bass"], SYNTHS["Laat5Intro"], SYNTHS["Bass"]], # Laat 3
    SCENES["Laat 4 - Scene 5"] : [SYNTHS["Brass"]], # Laat 4 - Intro
    SCENES["Laat 4 - Scene 6"] : [SYNTHS["Sun"]], # Laat 4 - Vers med playback bass
    SCENES["Laat 4 - Scene 7"] : [SYNTHS["Brass"]], # Laat 4 - Solo Bridge med playback bass
    SCENES["Laat 4 - Scene 8"] : [SYNTHS["Brass"]], # Laat 4 - Outro med playback bass
    SCENES["Laat 5 - Scene 9"] : [SYNTHS["Laat5Intro"]], # Laat 5 - Intro
    SCENES["Laat 5 - Scene 10"] : [SYNTHS["Laat5Intro"]], # Laat 5 - Refreng 
    SCENES["Laat 5 - Scene 11"] : [SYNTHS["Laat5Intro"], SYNTHS["Sun2"]], # Laat 5 - Bridge and out
    SCENES["Laat 6 - Scene 12"] : [SYNTHS["Blade"], SYNTHS["OrgelBass"], SYNTHS["Blade"], SYNTHS["ArpBass"]], # Laat 6
    SCENES["Laat 7 - Scene 13"] : [SYNTHS["OrgelBass"]], # Laat 7
    SCENES["Laat 8 - Scene 14"] : [SYNTHS["OrgelBass"], SYNTHS["ArpBass"]], # Laat 8
}

####### MIDI KEYBOARD INFO ########
####### RUN "keyboard-test.py" TO FIND CORRECT VALUES ######## 
NEXT_SYNTH_NOTE = 68 #the note number of the button that triggers a new synthS.
NEXT_SCENE_NOTE = 64 #the note number of the button that trigger the next scene.
PREV_SCENE_NOTE = 57

VOLUME_NOTE = 7 #the note number of the dial that control the volume
LOWPASS_NOTE = 10 #the note number of the dial that control the lowpass filtering
REVERB_NOTE = 11 #the note number of the dial that controls the reverb amount 

START_NOTE = 66 #the note number of the button that toggles start
STOP_NOTE = 65 #the note number of the button that toggles stop

CTRL_MIDI_CHAN = 176 #the MIDI channel of the buttons of the MIDI-keyboard, not the keys
NOTE_ON = 127 #the note-on MIDI value
NOTE_OFF = 0 #the note-off MIDI value

#to avoid conflict with other MIDI events on the same channel, we offset all our filtered message to very high midi notes.
#this value defines the highest possible note we can use for triggering events. all our events will occur just below this value.
HIGH_NOTE = 120