import mido

def choose_input_port():
    print("Please choose a input device:")
    inputs = mido.get_input_names()
    i = 1
    for name in inputs:
        print("{}. {}".format(i, name))
        i += 1
    
    choosed = int(input())
    port = mido.open_input(inputs[choosed - 1])
    print(port)
    return port

def note_name(midi_number):
    # MIDI 数字到音名的映射
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    # 计算音名
    note = notes[midi_number % 12]
    
    # 计算八度
    octave = (midi_number // 12) - 1
    
    # 返回音名和八度的组合
    return f"{note}{octave}"


def incr_or_default(map, key, default, step=1):
    if key in map:
        map[key] += step
    else:
        map[key] = default
