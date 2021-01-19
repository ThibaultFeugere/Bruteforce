import hashlib
from datetime import datetime

start = datetime.now()

dico = open('dico_mini_fr', 'r')
dico_lines = dico.readlines()

shadow = open('shadow_copy', 'r')
shadow_lines = shadow.readlines()

path = 'results_dico.txt'
results = open(path, 'w')

hashes = []

for line in shadow_lines:
    shadow_line_elements = line.replace('\n', '').split(':')
    if shadow_line_elements[0] != '':
        if shadow_line_elements[1][0] == '$':
            print('Utilisateur : ' + shadow_line_elements[0] + ' | Hash : ' + shadow_line_elements[1])
            hashes.append(shadow_line_elements[0])
            hashes.append(shadow_line_elements[1].replace('$1$', ''))

print('-------------------------------')

found = 0

for dico_line in dico_lines:
    generated_hash = hashlib.md5((dico_line.replace('\n', '')).encode('utf-8')).hexdigest()
    if generated_hash in hashes:
        found += 1
        i = hashes.index(generated_hash)
        results.write('User : ' + hashes[i-1] + ' Password : ' + dico_line)

shadow.close()
dico.close()
results.close()

if found >= 2:
    print(str(found) + ' mots de passe trouvés')
else:
    print(str(found) + ' mot de passe trouvé')

print('Résultats stockés dans : ' + path)

end = datetime.now()
print('------------')
print('Executés en : ' + str(end - start))
