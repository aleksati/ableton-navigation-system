SYNTHS = {
    "Brass": 0,
    "Bass": 1,
    "Laat5Intro": 2,
    "Sun": 3,
    "Sun2": 4,
    "Blade": 5,
    "OrgelBass": 6,
}

SCENES = {
    "Laat 1 - til bridge": 0,
    "Laat 1 - bridge ->out": 1,
    "Laat 2 - opptakt": 2,
    "Laat 2 - hele": 3,
    "Laat 3 - til bridge": 4,
    "Laat 3 - bridge->out": 5,
    "Laat 4 - intro": 6,
    "Laat 4 - vers->out": 7,
    "Laat 5 - intro": 8,
    "Laat 5 - ref->out": 9,
    "Laat 6 - til bridge": 10,
    "Laat 6 - bridge->out": 11,
    "Laat 7 - hele": 12,
    "Laat 8 - til vers2": 13,
    "Laat 8 - vers2->out": 14,
}

SCENE_CONFIG = {
    SCENES["Laat 1 - til bridge"]: [SYNTHS["Bass"]],
    SCENES["Laat 1 - bridge ->out"]: [SYNTHS["Bass"]],
    SCENES["Laat 2 - opptakt"]: [SYNTHS["Brass"]],
    SCENES["Laat 2 - hele"]: [SYNTHS["Brass"], SYNTHS["Bass"], SYNTHS["Brass"], SYNTHS["Bass"], SYNTHS["Brass"]],
    SCENES["Laat 3 - til bridge"]: [SYNTHS["Brass"], SYNTHS["Bass"]],
    SCENES["Laat 3 - bridge->out"]: [SYNTHS["Bass"]],
    SCENES["Laat 4 - intro"]: [SYNTHS["Brass"]],
    SCENES["Laat 4 - vers->out"]: [SYNTHS["Sun"], SYNTHS["Brass"]],
    SCENES["Laat 5 - intro"]: [SYNTHS["Laat5Intro"]],
    SCENES["Laat 5 - ref->out"]: [SYNTHS["Laat5Intro"], SYNTHS["Sun2"]],
    SCENES["Laat 6 - til bridge"]: [SYNTHS["Blade"], SYNTHS["OrgelBass"], SYNTHS["Blade"]],
    SCENES["Laat 6 - bridge->out"]: [SYNTHS["Blade"]],
    SCENES["Laat 7 - hele"]: [SYNTHS["OrgelBass"]],
    SCENES["Laat 8 - til vers2"]: [SYNTHS["OrgelBass"]],
    SCENES["Laat 8 - vers2->out"]: [SYNTHS["OrgelBass"]],
}

####### MIDI KEYBOARD INFO ########
####### RUN "keyboard-test.py" TO FIND CORRECT VALUES ########
# the note number of the button that triggers a new synthS.
NEXT_SYNTH_NOTE = 68
# the note number of the button that trigger the next scene.
NEXT_SCENE_NOTE = 64
PREV_SCENE_NOTE = 57

VOLUME_NOTE = 7  # the note number of the dial that control the volume
LOWPASS_NOTE = 10  # the note number of the dial that control the lowpass filtering
REVERB_NOTE = 11  # the note number of the dial that controls the reverb amount

START_NOTE = 66  # the note number of the button that toggles start
STOP_NOTE = 65  # the note number of the button that toggles stop

CTRL_MIDI_CHAN = 176  # the MIDI channel of the buttons of the MIDI-keyboard, not the keys
NOTE_ON = 127  # the note-on MIDI value
NOTE_OFF = 0  # the note-off MIDI value

# to avoid conflict with other MIDI events on the same channel, we offset all our filtered message to very high midi notes.
# this value defines the highest possible note we can use for triggering events. all our events will occur just below this value.
HIGH_NOTE = 120
