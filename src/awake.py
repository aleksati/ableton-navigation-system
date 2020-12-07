#This program is designed to dynamically arm different MIDI-instruments
#based on their designated Ableton Scene. Also, we send out any other CC Midi from 
#the MIDI-keyboard to ableton for mapping.
import rtmidi
from collections import deque
import utils
import time


scene_config = {
    1 : [0, 1, 0],
    2 : [2, 0, 2],
    3 : [2, 3, 1, 3]
}

synth_note = 68 #record button
scene_note = 57 #backward skip button

MIDI_CHAN = 176
NOTE_ON = 127
NOTE_OFF = 0

#Offset the synth and scene mapping notes so we ensure support for large number of synths and scenes. 
#If not, then constantly incrementing the MIDI message might trigger other unwanted stuff. 
_, synth_note_mod, scene_note_mod = utils.note_offset(scene_config, 120)

message = [[MIDI_CHAN, scene_note, NOTE_ON], 127]
init_count = 0
curr_synth = 0
curr_scene = 0
synth = False


midi_in, midi_out = utils.initialize_midi()

def synth_skip(gen1, gen2, message, curr_scene):
    if message[2] == NOTE_OFF:
        if len(scene_config[curr_scene]) > 1:
            message[2], message[1] = NOTE_ON, next(gen2)
            midi_out.send_message(message)
        else:
            pass
    else:
        note = next(gen1)
        message[1] = note
        midi_out.send_message(message)

        return int(note)

print('Ready!')
while True:
    if init_count != 0:
        message = midi_in.get_message()

    if message:
        message = message[0]
        if message[0] == MIDI_CHAN:
            #Scene skipping with only one MIDI trigger
            if message[1] == scene_note and message[2] == NOTE_ON:
                if synth: #Then we turn it off before switching scenes
                    midi_out.send_message([MIDI_CHAN, curr_synth, NOTE_ON])
                    synth = not synth

                #Increment scene
                curr_scene = utils.scene_increment(curr_scene, scene_config)
                midi_out.send_message([MIDI_CHAN, scene_note_mod+(curr_scene-1), NOTE_ON])
                print('Changing to scene: ', curr_scene)

                #Initialize the scene
                gen_scene1 = utils.synth_increment(synth_note_mod, curr_scene, scene_config)
                gen_scene2 = utils.synth_increment(synth_note_mod, curr_scene, scene_config)

                #Enable first synth in scene and create desired offset between on/off (gen_scene1 and gen_scene2).
                curr_synth = synth_skip(gen_scene1, gen_scene2, [MIDI_CHAN, synth_note_mod, NOTE_ON], curr_scene)
                #Keep track of synth on-off. Essential when only having one synth in a scene
                track_keeper = deque([curr_synth, curr_synth], maxlen=2)
                synth = not synth

            #Synth skipping with only one MIDI trigger
            elif message[1] == synth_note:
                if message[2] == NOTE_ON:
                    curr_synth = synth_skip(gen_scene1, gen_scene2, message, curr_scene)
                    track_keeper.appendleft(curr_synth)
                    if track_keeper[0] == track_keeper[1]:
                        synth = not synth
                    else:
                        synth = True
                elif message[2] == NOTE_OFF:
                    synth_skip(gen_scene1, gen_scene2, message, curr_scene)

            else:
                #Send out any other info from the correct channel. So to control volume, start/stop etc.
                 midi_out.send_message(message)

    init_count = 1         
    #time.sleep(.1)