from nim import train, play

ai = train(10000)

while True:
    select = input("Press '1' to play or '0' to exit: ")

    if select not in ['0', '1']: raise Exception('Selection is out of range :)')

    if select == '1':
        play(ai)
    else:
        break
