'''metazettel

This tiny script takes as input a table and a yaml file containing 
metadata and other information in the form of key: value pairs. It serves
to quickly summarize a "Kapselzettel".

Requires Python 3.X, otherwise complains: SyntaxError: Non-ASCII character 
'\xc3' in file metazettel.py on line 38, but no encoding declared; 
see http://www.python.org/peps/pep-0263.html for details. 

Usage: metazettel.py -i <infile> -o <outfile> [-y <yaml>]

Options:
  -h --help     Show this screen.
  -v --version  Show version.
  -i --infile   /path/to/infile
  -o --outfile  /path/to/outfile
  -y --yaml     /path/to/yaml 

'''

# http://docopt.org/
from docopt import docopt
import yaml
import re
from collections import Counter

if __name__ == '__main__':
    arguments = docopt(__doc__, version='metazettel 0.1')
# access: arguments['<outfile>']

# organmap
# References an organcode from the UICC TNM staging classification
# for hematogenic metastases, although some of these codes do not exist
# in the original classification. In principle, the first three letters
# of an organ are used as key.
d = {'kid': 'Niere', 'hea': 'Herz, Papillarmuskel, Koronararterien', 
'pul': 'Lunge', 'oss': 'Knochen', 'hep': 'Leber', 'spl': 'Milz',
'mar': 'Knochenmark', 'lym': 'Lymphknoten', 'bra': 'Gehirn', 
'ple': 'Pleura', 'per': 'Peritoneum', 'adr': 'Nebenniere', 
'ski': 'Haut', 'gal': 'Gallenblase', 'val': 'Herzklappen', 
'thy': 'Schilddrüse', 'pan': 'Pankreas', 'ova': 'Ovar', 
'tes': 'Hoden', 'pro': 'Prostate', 'pericard': 'Perikard', 
'ute': 'Uterus', 'eso': 'Ösophagus', 'sto': 'Magen', 
'col': 'Dickdarm', 'ile': 'Dünndarm', 'rec': 'Rektum',
'ner': 'Nerv'
}

index = 0
organlist = []
with open(arguments['<infile>'], 'r') as infile, \
    open(arguments['<outfile>'], 'w+') as outfile:
    for line in infile:
        if '&n' in line:

            # Number the table lines.
            index += 1
            # print(index)
            l = [element.strip() for element in line.split('|')]
            l[0] = str(index)
            outfile.write(' | '.join(l) + '\n')

            # Count the organ tags.
            try:
                m = re.search(r'<!-- (.*?) -->', line, re.DOTALL)
            # stackoverflow, 756898
            # Python Cookbook, 3rd edition, p. 44, 'Discussion'
                o = [i.strip() for i in m.group(1).split(',')]
                for i in o:
                    organlist.append(i)
            except AttributeError:
                pass
                # print('Nothing here.') # for debugging

# print(organlist)
# print(Counter(organlist))

len(set(organlist)) # for code A6015 or something like that

# Convert letters to words via organmap.
count = Counter([d[key] for key in organlist])

# [' x '.join([str(value), key]) for key, value in count.items()]
countformat = ['{} x {}\n'.format(value, key) for key, value in count.items()]


with open(arguments['<outfile>'], 'a') as file:
    file.write('\n')
    [file.write('{} x {}\n'.format(value, key)) for key, value in count.items()]
    file.write('\n')
    file.write(str(len(set(organlist))))

# TODO: rewrite using pandas with sep=' | ' and group by organ and stain





