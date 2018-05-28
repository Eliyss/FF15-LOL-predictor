import re

fil = open('nameNumbers.txt').read()
output = re.sub('\D \n', '', fil)
open('champindex.txt', 'w').write(output)