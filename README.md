# Matrix MIDI Navigation
Navigate ableton's session view as a 2D array using MIDI and assosiate individual tracks with designated scenes to enable super fast navigation (precise skipping). Perfect for live use. Also includes a script for doing MIDI-mapping between the controller and ableton.

<p align="center">
 <img src="img/main.gif" width=600>
</p>

# Config
<p align="center">
 <img src="img/overview.png" width=600>
</p>

### Virtual MIDI Port
You need to create a virtual MIDI port that sits between your MIDI-keyboard and Ableton Live's MIDI input. This is where the "awake" python script filters the incoming messages on their way to Ableton. On Mac, use the IAC Driver and setup a designated IAC bus. On Windows, I recommend using [Tobias Erichsen's loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) to setup a MIDI port.

### Ableton MIDI Preferences
**More info coming soon...**
Run the virtual MIDI port and set the following MIDI config in Ableton:
picture coming..

# How to Use
**More info coming soon...**
1. MIDI mapping
2. Go!

# Requirements
collections.deque and rtmidi
