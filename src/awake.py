#This script dynamically arms MIDI-instruments (on a midi-event) based on their designated Ableton Scene (SCENE_CONFIG). 
#Also, we send out any other CC Midi from MIDI-keyboard to ableton for mapping.
from collections import deque
import utils
import config

_, synth_note_mod, scene_note_mod = utils.note_offset()
midi_in, midi_out = utils.initialize_midi()

message = [[config.MIDI_CHAN, config.SCENE_NOTE, config.NOTE_ON], 127]
init_count = 0
curr_synth = 0
curr_scene = 0
synth = False

while True:
    if init_count != 0:
        message = midi_in.get_message()

    if message:
        message = message[0]
        if message[0] == config.MIDI_CHAN:
            #Scene skipping with only one MIDI trigger
            if message[1] == config.SCENE_NOTE and message[2] == config.NOTE_ON:
                if synth: #Then we turn it off before switching scenes
                    midi_out.send_message([config.MIDI_CHAN, curr_synth, config.NOTE_ON])
                    synth = not synth

                #Increment scene
                curr_scene = utils.scene_increment(curr_scene)
                midi_out.send_message([config.MIDI_CHAN, scene_note_mod+(curr_scene-1), config.NOTE_ON])
                print('Changing to scene: ', curr_scene)

                #Initialize the scene
                gen_scene1 = utils.synth_increment(synth_note_mod, curr_scene)
                gen_scene2 = utils.synth_increment(synth_note_mod, curr_scene)

                #Enable first synth in scene and create desired offset between on/off (gen_scene1 and gen_scene2).
                curr_synth = utils.synth_skip(gen_scene1, gen_scene2, [config.MIDI_CHAN, synth_note_mod, config.NOTE_ON], curr_scene, midi_out)
                
                #Keep track of synth on-off. Essential when only having one synth in a scene
                track_keeper = deque([curr_synth, curr_synth], maxlen=2)
                synth = not synth

            #Synth skipping with only one MIDI trigger
            elif message[1] == config.SYNTH_NOTE:
                if message[2] == config.NOTE_ON:
                    curr_synth = utils.synth_skip(gen_scene1, gen_scene2, message, curr_scene, midi_out)
                    track_keeper.appendleft(curr_synth)
                    if track_keeper[0] == track_keeper[1]:
                        synth = not synth
                    else:
                        synth = True
                elif message[2] == config.NOTE_OFF:
                    utils.synth_skip(gen_scene1, gen_scene2, message, curr_scene, midi_out)

            else:
                #Send out any other info from the correct channel. So to control volume, start/stop etc.
                 midi_out.send_message(message)
        else:
            midi_out.send_message(message)

    init_count = 1   