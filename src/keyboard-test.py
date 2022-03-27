import utils

# just prints out the midi messages from your device to the console.
# Use this to setup config.py
midi_in, midi_out = utils.initialize_midi()
with midi_in:
    prev_message = []
    while True:
        message = midi_in.get_message()
        if message and message is not prev_message:
            print(message)
            prev_message = message