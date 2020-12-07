import rtmidi


def initialize_midi():
    midi_in = rtmidi.MidiIn()
    midi_out = rtmidi.MidiOut()

    print('Available MIDI ports:')
    for port, name in enumerate(midi_in.get_ports()):
        print(port, ': ', name)
    input_port = int(input('which port should I get MIDI from?: '))
    midi_in_opened = midi_in.open_port(input_port)
    print('Getting MIDI from port: ', input_port)

    #print('Available MIDI OUT ports:')
    #for port, name in enumerate(midi_out.get_ports()):
    #    print(port, ': ', name)
    output_port = int(input('which port should I send the MIDI to?: '))
    midi_out_opened = midi_out.open_port(output_port)
    print('Sending MIDI to port: ', output_port)
    print('\n')

    return midi_in_opened, midi_out_opened


def synth_increment(note, scene, scene_config):
    this_scene = scene_config[scene]
    count = 0
    while True:
        yield note + this_scene[count]
        if count < (len(this_scene)-1):
            count += 1
        else:
            count = 0


def scene_increment(scene, scene_config):
    if scene < len(scene_config):
        return scene+1
    else:
        return 1


def note_offset(scene_config, high_note):
    synth_count=[]
    for i in range(len(scene_config)):
        #remove duplicate synth from the config dict
        curr_key = list(dict.fromkeys(scene_config[i+1]))
        #add only new items (new synths) to synth_count
        for elem in curr_key:
            if elem in synth_count:
                pass
            else:
                synth_count.append(elem)

    synth_note_mod = high_note-(len(scene_config)+len(synth_count)) 
    scene_note_mod = synth_note_mod+len(synth_count)

    return len(synth_count), synth_note_mod, scene_note_mod