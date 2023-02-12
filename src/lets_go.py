# This script dynamically arms MIDI-instruments (on a midi-event) based on their designated Ableton Scene (SCENE_CONFIG).
# Also, we send out any other CC Midi from MIDI-keyboard to ableton for mapping.
from collections import deque
import utils
import config

_, synth_trigger_note, scene_trigger_note = utils.gen_note_offsets()
midi_in, midi_out = utils.midi_INIT()
init = False

while True:
    if init:
        message = midi_in.get_message()
    else:
        message, init, curr_synth, curr_scene = utils.program_INIT()

    if not message:
        continue

    message = message[0]

    # Hitting keys/notes
    if message[0] is not config.CTRL_MIDI_CHAN:
        midi_out.send_message(message)

    # Hitting the scene buttons
    if message[1] is config.NEXT_SCENE_NOTE or message[1] is config.PREV_SCENE_NOTE:
        if message[2] is not config.NOTE_ON:
            continue
        # turn off the current synth
        utils.synth_OFF(synth_trigger_note, curr_synth, midi_out)

        # increment or decrement the scene count.
        curr_scene = utils.scene_CHANGE(curr_scene, message[1])
        # change the scene in Ableton
        utils.scene_ON(scene_trigger_note, curr_scene, midi_out)

        # initialize a new synth and generator objects to turn them off and on.
        gen_curr_synth = utils.synth_INIT(synth_trigger_note, curr_scene)
        gen_prev_synth = utils.synth_INIT(synth_trigger_note, curr_scene)
        # By calling next() here, I created the desired offsett between on/off
        curr_synth = next(gen_curr_synth)

        utils.synth_ON(synth_trigger_note, curr_synth, midi_out)

        # Keep track of synth on-off. Essential when only having one synth in a scene
        track_keeper = deque([curr_synth, curr_synth], maxlen=2)

    # Hitting next-synth button
    if message[1] is config.NEXT_SYNTH_NOTE:
        if message[2] is not config.NOTE_ON:
            continue
        # Generate a new synth and turn it on
        curr_synth = next(gen_curr_synth)
        utils.synth_ON(synth_trigger_note, curr_synth, midi_out)
        # add curr_synth to tracker
        track_keeper.appendleft(curr_synth)

        # if the prev and current synth are the same, we do NOT turn off the prev synth
        if track_keeper[0] == track_keeper[1]:
            continue

        # generate the prev synth and turn it off.
        prev_synth = next(gen_prev_synth)
        utils.synth_OFF(synth_trigger_note, prev_synth, midi_out)

    # Hitting volume, start & stop etc.
    if message[1] is not config.NEXT_SCENE_NOTE and message[1] is not config.PREV_SCENE_NOTE and message[1] is not config.NEXT_SYNTH_NOTE:
        midi_out.send_message(message)
