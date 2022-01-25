# Matrix MIDI Navigation
Navigate ableton's session view as a 2D array using MIDI and assosiate individual tracks with designated scenes to enable super fast navigation (precise skipping). Perfect for live use. Also includes a script for doing MIDI-mapping between the controller and ableton.

<p align="center">
 <img src="img/main.gif" width=600>
</p>

# How To Use
### Overview
You need to create a virtual MIDI port that sits between your MIDI-keyboard and Ableton Live's MIDI input. This is where the python scripts will filter the incoming messages. On Mac, use the IAC Driver and setup a IAC bus. On Windows, I recommend using [Tobias Erichsen's loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html).

<p align="center">
 <img src="img/overview.png" width=600>
</p>

### Ableton Config
In Ableton Live 11, use the following MIDI config.

.. coming soon ..

### use
.. coming soon ..

# Requirements
collections.deque and rtmidi
