"""
音程练习
接上你的midi键盘，我在纯一度到大十三度范围内随机出一个音程，你随便按下两个按键，对了就是对了，错了就是错了~~

python -m pip install mido
python -m pip install python-rtmidi
"""

import utils
import random

QUESTIONS = [
    "纯一度",
    "小二度",
    "大二度",
    "小三度",
    "大三度",
    "纯四度",
    "增四度",
    "减五度",
    "纯五度",
    "小六度",
    "大六度",
    "小七度",
    "大七度",
    "纯八度",
    # "小九度",
    "大九度",
    # "小十度",
    # "大十度",
    # "纯十一度",
    # "增十一度",
    # "减十二度",
    # "纯十二度",
    # "小十三度",
    "大十三度",
]

_intervals = {
    "纯一度": 0,
    "小二度": 1,
    "大二度": 2,
    "小三度": 3,
    "大三度": 4,
    "纯四度": 5,
    "增四度": 6,
    "减五度": 6,
    "纯五度": 7,
    "小六度": 8,
    "大六度": 9,
    "小七度": 10,
    "大七度": 11,
    "纯八度": 12,
    "小九度": 13,
    "大九度": 14,
    "小十度": 15,
    "大十度": 16,
    "纯十一度": 17,
    "增十一度": 18,
    "减十二度": 18,
    "纯十二度": 19,
    "小十三度": 20,
    "大十三度": 21,
}

def main():
    right_cnt = 0
    right_map = {}
    wrong_cnt = 0
    wrong_map = {}

    port = utils.choose_input_port()
    print("==================")

    while True:
        q = random.choice(QUESTIONS)
        print("QUESTION: {}", q)
        right_interval = _intervals[q]

        pressed_key = []

        while True:
            msg = port.receive()
            if msg.type == "note_on":
                pressed_key.append(msg.note)
            if len(pressed_key) == 2:
                break

        interval = abs(pressed_key[0] - pressed_key[1])
        small = min(pressed_key)
        big = max(pressed_key)

        print("Yours -> {} - {}".format(utils.note_name(small), utils.note_name(big)))
        print("Right -> {} - {}".format(utils.note_name(small), utils.note_name(small + interval)))

        print("your interval: {}, right interval: {}".format(interval, right_interval))

        if interval == right_interval:
            right_cnt += 1
            utils.incr_or_default(right_map, q, 1)
            print("RIGHT!!!!!")
        else:
            wrong_cnt += 1
            utils.incr_or_default(wrong_map, q, 1)
            print("WRONG~")

        print("right cnt: {}, wrong cnt {}".format(right_cnt, wrong_cnt))
if __name__ == "__main__": 
    main()