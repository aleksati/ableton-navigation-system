#This script dynamically arms MIDI-instruments (on a midi-event) based on their designated Ableton Scene (SCENE_CONFIG). 
#Also, we send out any other CC Midi from MIDI-keyboard to ableton for mapping.
from collections import deque
import utils
import config

_, synth_trigger_note, scene_trigger_note = utils.gen_note_offset()
midi_in, midi_out = utils.midi_INIT()
init = False

while True:
    if init:
        message = midi_in.get_message() 
    else: 
        message, init, curr_synth, curr_scene = utils.program_INIT()

    if not message: continue
    message = message[0]

    #key notes
    if message[0] is not config.MIDI_CHAN: midi_out.send_message(message)
    #volume, start & stop etc.
    if message[1] is not config.SCENE_NOTE and message[1] is not config.SYNTH_NOTE: midi_out.send_message(message) 

    if message[1] is config.SCENE_NOTE and message[2] is config.NOTE_ON:
        #turn off the synth
        utils.synth_OFF(curr_synth, midi_out)
        #increment the scene count
        curr_scene = utils.scene_increment(curr_scene)
        #change the scene in Ableton
        utils.scene_NEXT(scene_trigger_note, curr_scene, midi_out)

        #initialize a new synth and generator objects to turn them off and on.
        #enable first synth in scene and create desired offset between on/off.
        gen_curr_synth = utils.synth_INIT(synth_trigger_note, curr_scene)
        gen_prev_synth = utils.synth_INIT(synth_trigger_note, curr_scene)
        curr_synth = next(gen_curr_synth)

        utils.synth_ON(curr_synth, midi_out)

        #Keep track of synth on-off. Essential when only having one synth in a scene
        track_keeper = deque([curr_synth, curr_synth], maxlen=2)

    elif message[1] is config.SYNTH_NOTE and message[2] is config.NOTE_ON:
        #Generate a new synth and turn it on
        curr_synth = next(gen_curr_synth)
        utils.synth_ON(curr_synth, midi_out)
        #add curr_synth to tracker
        track_keeper.appendleft(curr_synth)
   
        # if the prev and current synth are different synths:
        if track_keeper[0] != track_keeper[1]:
            #generate the prev synth and turn it off.
            prev_synth = next(gen_prev_synth)
            utils.synth_OFF(prev_synth, midi_out)