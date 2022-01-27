import rtmidi
import config

#init the midi objects
def midi_INIT():
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

#init the program
def program_INIT():
    message = [[config.MIDI_CHAN, config.SCENE_NOTE, config.NOTE_ON], 127]
    curr_synth = 0
    curr_scene = 0
    init = True
    print("Ready!")
    print("\n")
    return message, init, curr_synth, curr_scene

#turn a synth on
def synth_ON(synth_val, midi_out):
    midi_out.send_message([config.MIDI_CHAN, synth_val, config.NOTE_ON])
    print("Synth", synth_val, "ON")

#turn a synth off
def synth_OFF(synth_val, midi_out):
    midi_out.send_message([config.MIDI_CHAN, synth_val, config.NOTE_OFF])
    print("Synth", synth_val, "OFF")

#create a generator object that loops through the synth values in a scene and loop back to start when necessary. 
def synth_INIT(synth_trigger_note, scene):
    this_scene = config.SCENE_CONFIG[scene]
    count = 0
    while True:
        yield synth_trigger_note + this_scene[count]
        if count < (len(this_scene)-1):
            count += 1
        else:
            count = 0

#jump to the next scene
def scene_NEXT(scene_trigger_note, curr_scene, midi_out):
    scene = scene_trigger_note+(curr_scene-1)
    midi_out.send_message([config.MIDI_CHAN, scene, config.NOTE_ON])
    print('Scene', curr_scene)

#increment the scene count and loop back to start when necessary
def scene_increment(curr_scene):
    if curr_scene < len(config.SCENE_CONFIG):
        return curr_scene+1
    else:
        return 1

#offset the synth and scene trigger values (defined in config) so we ensure support for large number of synths and scenes. 
#if not, then constantly incrementing the MIDI message might trigger other unwanted stuff. 
def gen_note_offset():
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

    synth_trigger_note = config.HIGH_NOTE-(len(config.SCENE_CONFIG)+len(synth_count)) 
    scene_trigger_note = synth_trigger_note+len(synth_count)

    return len(synth_count), synth_trigger_note, scene_trigger_note