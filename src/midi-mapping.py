import rtmidi
import utils


scene_config = {
    1 : [0, 1, 0],
    2 : [2, 0, 2],
    3 : [2, 3, 1, 3]
}

synth_note = 68
scene_note = 57

volume_note = 7
lowpass_note = 10
reverb_note = 11

start_note = 66
stop_note = 65

MIDI_CHAN = 176
NOTE_ON = 127
NOTE_OFF = 0

#Offset the the desired CC messages so they dont trigger other stuff (like start and stop)
#Also, ensure the possibility of having a larger number of scenes and synths
synth_numb, synth_note, scene_note = utils.note_offset(scene_config, 120)
scene_numb = len(scene_config)

scene_count = 1
synth_count = 1
config_count = 0

midi_out = rtmidi.MidiOut()
print('Available MIDI ports:')
for port, name in enumerate(midi_out.get_ports()):
    print(port, ': ', name)
output_port = int(input('which port should I send the MIDI to?: '))
#midiout = midi_out.open_port(output_port)
print('\n')

with midi_out.open_port(output_port) as midiout:
    while scene_count <= scene_numb:
        inn = input(f"Toggle scene {scene_count}, THEN press y to continue: ")
        if inn == "y":
            midiout.send_message([MIDI_CHAN, scene_note, NOTE_ON])
            scene_note += 1
            scene_count += 1
        else:
            print("Scene config halted")
            break
    print('\n')

    while synth_count <= synth_numb: 
        inn = input(f"Toggle synth {synth_count-1}, THEN press y to continue: ")
        if inn == "y":
            midiout.send_message([MIDI_CHAN, synth_note, NOTE_ON])
            synth_note += 1
            synth_count += 1
        else:
            print("Synth config halted")
            break
    print('\n')
    
    inn = input(f"Toggle main volume, THEN press y to continue: ")
    if inn == "y":
        midiout.send_message([MIDI_CHAN, volume_note, NOTE_ON])
        config_count += 1
    else:
        print("Volume config halted")

    inn = input(f"Toggle Low-pass filter, THEN press y to continue: ")
    if inn == "y":
        midiout.send_message([MIDI_CHAN, lowpass_note, NOTE_ON])
        config_count += 1
    else:
        print("Lowpass config halted")

    inn = input(f"Toggle reverb, THEN press y to continue: ")
    if inn == "y":
        midiout.send_message([MIDI_CHAN, reverb_note, NOTE_ON])
        config_count += 1
    else:
        print("Reverb config halted")
    
    inn = input(f"Toggle start, THEN press y to continue: ")
    if inn == "y":
        midiout.send_message([MIDI_CHAN, start_note, NOTE_ON])
        config_count += 1
    else:
        print("Reverb config halted")

    inn = input(f"Toggle stop, THEN press y to continue: ")
    if inn == "y":
        midiout.send_message([MIDI_CHAN, stop_note, NOTE_ON])
        config_count += 1
    else:
        print("Reverb config halted")
    print('\n')
    
    if synth_count-1 == synth_numb and scene_count-1 == scene_numb and config_count == 5:
        print("Config fully completed!")
