import hashlib
import random
import string
from itertools import product
from datetime import datetime
import threading

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789;@_#'

def findHashes():
    lines = open('shadow_copy', 'r').readlines()
    hashes = []
    for line in lines:
        shadow_line_elements = line.replace('\n', '').split(':')
        if shadow_line_elements[0] != '':
            if shadow_line_elements[1][0] == '$':
                print('Utilisateur : ' + shadow_line_elements[0] + ' | Hash : ' + shadow_line_elements[1])
                hashes.append(shadow_line_elements[0])
                hashes.append(shadow_line_elements[1].replace('$1$', ''))
    return hashes

def bruteForce(threadNumber, start, end):
    date_start = datetime.now()
    for length in range(start, end):
        print('Thread numéro : ' + str(threadNumber) + ' longueur : ' + str(length))
        for attempt in product(chars, repeat=length):
            password = (''.join(attempt))
            if hashlib.md5(password.encode('utf-8')).hexdigest() in hashes:
                print('Mot de passe trouvé : ' + password)
                break
    print('Thread ' + str(threadNumber) + ' terminé en ' + str(datetime.now() - date_start))


hashes = findHashes()

thread1 = threading.Thread(target=bruteForce, args=(1, 1, 6))
thread2 = threading.Thread(target=bruteForce, args=(2, 6, 7))
thread3 = threading.Thread(target=bruteForce, args=(3, 7, 8))

thread1.start()
thread2.start()
thread3.start()
