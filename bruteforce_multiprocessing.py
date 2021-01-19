import hashlib
import random
import string
from itertools import product
from datetime import datetime
import time
import multiprocessing 

def findHashes():
    lines = open('shadow', 'r').readlines()
    hashes = []
    for line in lines:
        shadow_line_elements = line.replace('\n', '').split(':')
        if shadow_line_elements[0] != '':
            if shadow_line_elements[1][0] == '$':
                print('Utilisateur : ' + shadow_line_elements[0] + ' | Hash : ' + shadow_line_elements[1])
                hashes.append(shadow_line_elements[0])
                hashes.append(shadow_line_elements[1].replace('$1$', ''))
    return hashes

def multiproc_func(chars, hashes, x):
    for length in range(x, x+1):
        print('Longueur : ' + str(length))
        for attempt in product(chars, repeat=length):
            password = (''.join(attempt))
            if hashlib.md5(password.encode('utf-8')).hexdigest() in hashes:
                print('Mot de passe trouvé : ' + password)
                break
    print('Longueur ' + str(x) + ' terminé.')
    
if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789;@_#'
    hashes = findHashes()
    starttime = time.time()
    processes = []
    for i in range(6,9):
        p = multiprocessing.Process(target=multiproc_func, args=(chars,hashes,i))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print('Cela a pris ' + str(time.time() - starttime) + ' secondes')
