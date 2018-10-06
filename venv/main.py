# Program to imitate the computer scene in the matrix
#author: Cody

import sys
import os
from time import sleep




white_rabbit_1 = 'Wake up, Neo...'
white_rabbit_2 = 'The Matrix has you...'
white_rabbit_3 = 'Follow the white rabbit.'
white_rabbit_4 = 'Knock, knock neo...'
white_rabbit_5 = ['Wake up, Neo...','The Matrix has you...','Follow the white rabbit.','Knock, knock neo...']





def whiterabbit():

    os.system('cls')
    sleep(5)
    for i in range(len(white_rabbit_1)):

        if i != len(white_rabbit_1) - 1:

            print(white_rabbit_1[i], end = '')
            sys.stdout.flush()
            sleep(0.21)
        elif i == len(white_rabbit_1) - 1:
            print(white_rabbit_1[i])
            sleep(3)
            os.system('cls')
            sleep(1.5)


    for i in range(len(white_rabbit_2)):

        if i != len(white_rabbit_2) - 1:


            print(white_rabbit_2[i], end = '')
            sys.stdout.flush()
            sleep(0.21)
        elif i == len(white_rabbit_2) - 1:
            print(white_rabbit_2[i])
            sleep(3)
            os.system('cls')
            sleep(1.5)

    for i in range(len(white_rabbit_3)):

        if i != len(white_rabbit_3) - 1:

            print(white_rabbit_3[i], end = '')
            sys.stdout.flush()
            sleep(0.21)
        elif i == len(white_rabbit_3) - 1:
            print(white_rabbit_3[i])
            sleep(2)
            os.system('cls')


    print(white_rabbit_4)
    sleep(4)
    os.system('cls')
    sleep(1.5)
    exit(0)










whiterabbit()