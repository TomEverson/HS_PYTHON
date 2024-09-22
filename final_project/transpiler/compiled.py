

WELCOME_TEXT = """W         W    EEEEE    L        CCCCC     OOOO     M       M    EEEEE
W         W    E        L        C        O    O    MM     MM    E
W    W    W    EEEE     L        C        O    O    M M   M M    EEEE
 W  W  W  W    E        L        C        O    O    M   M   M    E 
  W     W      EEEEE    LLLLL    CCCCC     OOOO     M       M    EEEEE

FFFFF    RRRRR      OOOO     M     M
F        R    R    O    O    MM   MM
FFFFF    RRRRR     O    O    M M M M
F        R   R     O    O    M  M  M
F        R    R     OOOO     M     M

RRRRR     PPPPP     SSSSS
R    R    P    P    S
RRRRR     PPPPP     SSSSS
R   R     P             S
R    R    P         SSSSS


"""

PLAYER_POINT = 0
CPU_POINT = 0

print(WELCOME_TEXT)


def WHILE(COUNT):
    global PLAYER_POINT
    global CPU_POINT
    if COUNT < 3:
        PLAYER_DECISION = int(input("1.ROCK, 2.PAPER, 3.SCISSORS  "))
        import random
        CPU_DECISION = random.randint(1, 3)
        if PLAYER_DECISION == 1:
            if CPU_DECISION == 1:
                print("COMPUTER CHOSE ROCK")
                print("TIED")
                WHILE(COUNT + 1)
            elif CPU_DECISION == 2:
                print("COMPUTER CHOSE ROCK")
                print("CPU WINS")
                CPU_POINT = CPU_POINT + 1
                WHILE(COUNT + 1)
            elif CPU_DECISION == 3:
                print("COMPUTER CHOSE ROCK")
                print("PLAYER WINS")
                PLAYER_POINT = PLAYER_POINT + 1
                WHILE(COUNT + 1)

        elif PLAYER_DECISION == 2:
            if CPU_DECISION == 1:
                print("COMPUTER CHOSE PAPER")
                print("PLAYER WINS")
                PLAYER_POINT = PLAYER_POINT + 1
                WHILE(COUNT + 1)
            elif CPU_DECISION == 2:
                print("COMPUTER CHOSE PAPER")
                print("TIED")
                WHILE(COUNT + 1)
            elif CPU_DECISION == 3:
                print("COMPUTER CHOSE PAPER")
                print("PLAYER WINS")
                CPU_POINT = CPU_POINT + 1
                WHILE(COUNT + 1)

        elif PLAYER_DECISION == 3:
            if CPU_DECISION == 1:
                print("COMPUTER CHOSE SCISSORS")
                print("CPU WINS")
                CPU_POINT = CPU_POINT + 1
                WHILE(COUNT + 1)
            elif CPU_DECISION == 2:
                print("COMPUTER CHOSE SCISSORS")
                print("PLAYER WINS")
                PLAYER_POINT = PLAYER_POINT + 1
                WHILE(COUNT + 1)
            elif CPU_DECISION == 3:
                print("COMPUTER CHOSE SCISSORS")
                print("TIED")
                WHILE(COUNT + 1)


WHILE(0)

if PLAYER_POINT == CPU_POINT:
    print("TIEDDDD")
elif PLAYER_POINT > CPU_POINT:
    print("YOU WINN")
else:
    print("YOU LOSE")
