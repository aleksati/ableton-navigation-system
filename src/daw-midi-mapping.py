import utils
import config

#Offset the the desired CC messages so they dont trigger other stuff (like start and stop)
#Also, ensure the possibility of having a larger number of scenes and synths
synth_numb, synth_note_mod, scene_note_mod = utils.note_offset()
midi_in, midi_out = utils.initialize_midi()

scene_numb = len(config.SCENE_CONFIG)
scene_count = 1
synth_count = 1
config_count = 0

with midi_out:
    while scene_count <= scene_numb:
        inn = input(f"Toggle scene {scene_count}, THEN press y to continue: ")
        if inn == "y":
            midi_out.send_message([config.MIDI_CHAN, scene_note_mod, config.NOTE_ON])
            scene_note_mod += 1
            scene_count += 1
        else:
            print("Scene config halted")
            break
    print('\n')

    while synth_count <= synth_numb: 
        inn = input(f"Toggle synth {synth_count-1}, THEN press y to continue: ")
        if inn == "y":
            midi_out.send_message([config.MIDI_CHAN, synth_note_mod, config.NOTE_ON])
            synth_note_mod += 1
            synth_count += 1
        else:
            print("Synth config halted")
            break
    print('\n')
    
    inn = input(f"Toggle main volume, THEN press y to continue: ")
    if inn == "y":
        midi_out.send_message([config.MIDI_CHAN, config.VOLUME_NOTE, config.NOTE_ON])
        config_count += 1
    else:
        print("Volume config halted")

    inn = input(f"Toggle Low-pass filter, THEN press y to continue: ")
    if inn == "y":
        midi_out.send_message([config.MIDI_CHAN, config.LOWPASS_NOTE, config.NOTE_ON])
        config_count += 1
    else:
        print("Lowpass config halted")

    inn = input(f"Toggle reverb, THEN press y to continue: ")
    if inn == "y":
        midi_out.send_message([config.MIDI_CHAN, config.REVERB_NOTE, config.NOTE_ON])
        config_count += 1
    else:
        print("Reverb config halted")
    
    inn = input(f"Toggle start, THEN press y to continue: ")
    if inn == "y":
        midi_out.send_message([config.MIDI_CHAN, config.START_NOTE, config.NOTE_ON])
        config_count += 1
    else:
        print("Reverb config halted")

    inn = input(f"Toggle stop, THEN press y to continue: ")
    if inn == "y":
        midi_out.send_message([config.MIDI_CHAN, config.STOP_NOTE, config.NOTE_ON])
        config_count += 1
    else:
        print("Reverb config halted")
    print('\n')
    
    if synth_count-1 == synth_numb and scene_count-1 == scene_numb and config_count == 5:
        print("Config fully completed!")
