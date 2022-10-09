# Overview

Navigate Ableton Live's session view as a 2D matrix using as few MIDI control signals as possible (two buttons; one for scene skipping and one for synth skipping). The scripts work by associating individual MIDI tracks with specific scenes in Ableton, enabling very fast "skipping" between synths and scenes, making them ideal for live performance.

<p align="left">
 <img src="img/main.gif" width=auto>
</p>

# Config

### Virtual MIDI Port

You need to create a virtual MIDI port that will sit between the python rtMIDI and your DAW. On Mac, use the IAC Driver and setup a designated IAC bus. On Windows, I recommend using [Tobias Erichsen's loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html).

<p align="left">
 <img src="img/overview.png" width=auto>
</p>

### Config.py

Once the virtual MIDI port is configured, open _config.py_ and add the following information:

```
SYNTHS = {
    "ArpBass": 0,
    "Brass": 1,
    "Bass": 2,
    "Laat5Intro": 3,
    "Sun": 4,
    "Blade": 5,
    "OrgelBass": 6,
}

SCENES = {
    "Laat 1 - Scene 1" : 0,
    "Laat 2 - Scene 2" : 1,
    "Laat 3 - Scene 3" : 2,
    "Laat 4 - Scene 4" : 3,
    "Laat 4 - Scene 5" : 4,
    "Laat 4 - Scene 6" : 5,
    "Laat 4 - Scene 7" : 6,
    "Laat 5 - Scene 8" : 7,
    "Laat 5 - Scene 9" : 8,
    "Laat 5 - Scene 10" : 9,
    "Laat 6 - Scene 11" : 10,
    "Laat 7 - Scene 12" : 11,
    "Laat 8 - Scene 13" : 12,
}

SCENE_CONFIG = {
    SCENES["Laat 1 - Scene 1"] : [SYNTHS["Bass"], SYNTHS["ArpBass"]], # Laat 1
    SCENES["Laat 2 - Scene 2"] : [SYNTHS["Brass"], SYNTHS["Bass"], SYNTHS["Brass"], SYNTHS["Bass"]], # Laat 2
    SCENES["Laat 3 - Scene 3"] : [SYNTHS["Brass"], SYNTHS["Bass"], SYNTHS["ArpBass"], SYNTHS["Bass"]], # Laat 3
    SCENES["Laat 4 - Scene 4"] : [SYNTHS["Brass"]], # Laat 4 - Intro
    SCENES["Laat 4 - Scene 5"] : [SYNTHS["Sun"]], # Laat 4 - Vers med playback bass
    SCENES["Laat 4 - Scene 6"] : [SYNTHS["Brass"]], # Laat 4 - Solo Bridge med playback bass
    SCENES["Laat 4 - Scene 7"] : [SYNTHS["Brass"]], # Laat 4 - Outro med playback bass
    SCENES["Laat 5 - Scene 8"] : [SYNTHS["Laat5Intro"]], # Laat 5 - Intro
    SCENES["Laat 5 - Scene 9"] : [SYNTHS["Bass"]], # Laat 5 - Refreng
    SCENES["Laat 5 - Scene 10"] : [SYNTHS["Bass"], SYNTHS["Laat5Intro"], SYNTHS["Bass"], SYNTHS["Sun"]], # Laat 5 - Bridge and out
    SCENES["Laat 6 - Scene 11"] : [SYNTHS["Blade"], SYNTHS["OrgelBass"], SYNTHS["Blade"], SYNTHS["ArpBass"]], # Laat 6
    SCENES["Laat 7 - Scene 12"] : [SYNTHS["OrgelBass"]], # Laat 7
    SCENES["Laat 8 - Scene 13"] : [SYNTHS["OrgelBass"], SYNTHS["ArpBass"]], # Laat 8
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
```

To see the MIDI values from your own setup, run the _keyboard-test.py_, use your MIDI-keyboard and see the MIDI-values printed on the console.

The SCENE_CONFIG defines which synths are used in which scenes, and the order. For instance, in `SCENES["Laat1 - Scene 1"]`, we switch from bass to arpbass, and back again, if we continuously press the button associated with the NEXT_SYNTH_NOTE value.

### Ableton MIDI Settings

Run the virtual MIDI port and enable it to track and remote control your DAW. Disable your keybords native MIDI-port. If not, there will be conflicts.

<p align="left">
 <img src="img/ableton-midi-pref.jpg" width=400>
</p>
All midi will come from our virtual MIDI port.

# How to Use

### MIDI Mapping

To make the midi-mapping part easy, I made a small script that does it automatically based on the information in _config.py_. To do this, simply run your virtual MIDI port, open your DAW in MIDI-mapping-mode, set correct MIDI settings and run _daw-midi-mapping.py_. Then, follow the command-line instructions to correctly setup Ableton.

```
Available MIDI input ports:
0 :  X3mini 0
1 :  virtual_midi_port 1
which port should I get MIDI from?: 0
Receiving MIDI from port:  0


Available MIDI output ports:
0 :  Microsoft GS Wavetable Synth 0
1 :  X3mini 1
2 :  virtual_midi_port 2
which port should I send the MIDI to?: 2
Sending MIDI to port:  2


Toggle scene 1, THEN press y to continue: y
Toggle scene 2, THEN press y to continue: y
Toggle scene 3, THEN press y to continue: y


Toggle synth 0, THEN press y to continue: y
Toggle synth 1, THEN press y to continue: y
Toggle synth 2, THEN press y to continue: y
Toggle synth 3, THEN press y to continue: y


Toggle main volume, THEN press y to continue: y
Toggle Low-pass filter, THEN press y to continue: y
Toggle reverb, THEN press y to continue: y
Toggle start, THEN press y to continue: y
Toggle stop, THEN press y to continue: y


Config fully completed!
```

### Running the program

When everything above is set, run _lets_go.py_. Remember to turn off all the speaker buttons (big yellow) beforehand.

# Dependencies

- Python3, with:
  - collections from deque
  - rtmidi
- Virtual MIDI driver
- USB MIDI keyboard
- DAW (Ableton Live 11)
