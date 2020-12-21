# author: Sakhar Alkhereyf

import subprocess

# put the full path between double quotes
path = '"/Users/name/file.pdf"'

output = !gs -o - -sDEVICE=inkcov $path

# delete extra lines
i = 0
for line in output:
    if line.startswith('Page 1'):
        break
    i += 1
text = '\n'.join(output[i:])

# process file

i = 0
last_p_n = None
diff = 17 # if pdf number is different than the document number
for line in text.split('\n'):
    if i%2 == 0:
        last_p_n = line.split()[1]
    else:
        down_page = int(last_p_n) - diff
        vals = line.split()[:3]
        vals = map(float,vals)
        if sum(vals) > 0:
            print(last_p_n,down_page)
    i += 1
