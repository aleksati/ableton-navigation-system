import rtmidi
import config

def initialize_midi():
    print('\n')

    print('Available MIDI input ports:')
    midi_in = rtmidi.MidiIn()
    for port, name in enumerate(midi_in.get_ports()):
        print(port, ': ', name)
    input_port = int(input('which port should I get MIDI from?: '))
    midi_in_opened = midi_in.open_port(input_port)
    print('Receiving MIDI from port: ', input_port)

    print('\n')

    print('Available MIDI output ports:')
    midi_out = rtmidi.MidiOut()
    for port, name in enumerate(midi_out.get_ports()):
        print(port, ': ', name)
    output_port = int(input('which port should I send the MIDI to?: '))
    midi_out_opened = midi_out.open_port(output_port)
    print('Sending MIDI to port: ', output_port)
    print('\n')

    return midi_in_opened, midi_out_opened

#FIXME: No need to overcomplicate this. Presume arm exclusive.
#skip to the next synth and turn off the last synth that was enabled
def synth_skip(gen1, gen2, message, curr_scene, midi_out):
    #Enable first synth in scene and create desired offset between on/off (gen_scene1 and gen_scene2).
    if message[2] == config.NOTE_OFF:
        if len(config.SCENE_CONFIG[curr_scene]) > 1:
            message[2], message[1] = config.NOTE_ON, next(gen2)
            midi_out.send_message(message)
        else:
            pass
    else:
        note = next(gen1)
        message[1] = note
        midi_out.send_message(message)

        return int(note)

#increment the synth value in the current scene
#and loop back to start when necessary. 
def synth_increment(synth_trigger_note, scene):
    this_scene = config.SCENE_CONFIG[scene]
    count = 0
    while True:
        yield synth_trigger_note + this_scene[count]
        if count < (len(this_scene)-1):
            count += 1
        else:
            count = 0


def scene_increment(curr_scene):
    if curr_scene < len(config.SCENE_CONFIG):
        return curr_scene+1
    else:
        return 1

#Offset the synth and scene trigger midi-values so we ensure support for large number of synths and scenes. 
#If not, then constantly incrementing the MIDI message might trigger other unwanted stuff. 
def note_offset():
    synth_count=[]
    for i in range(len(config.SCENE_CONFIG)):
        #remove duplicate synth from the config dict
        curr_key = list(dict.fromkeys(config.SCENE_CONFIG[i+1]))
        #add only new items (new synths) to synth_count
        for elem in curr_key:
            if elem in synth_count:
                pass
            else:
                synth_count.append(elem)

    synth_note_mod = config.HIGH_NOTE-(len(config.SCENE_CONFIG)+len(synth_count)) 
    scene_note_mod = synth_note_mod+len(synth_count)

    return len(synth_count), synth_note_mod, scene_note_mod