'''yamlcalc

This script calculates some new keys given a yaml file.

Requires Python 3.X if used with non-ASCII characters in the yaml.

Usage: yamlcalc.py -y <yaml> -o <outfile> -r <ref>

Options:
  -h --help         Show this screen.
  -v --version      Show version.
  -y --yaml         /path/to/yaml
  -o --outfile      /path/to/outfile 
  -r --reference    /path/to/heart_weight_reference.csv 

'''

# http://docopt.org/
from docopt import docopt
from utils import ordered_load, ordered_dump, calculate_age
import yaml
import pandas as pd
from datetime import datetime



if __name__ == '__main__':
    arguments = docopt(__doc__, version='yamlcalc 0.1')
    # print(arguments)



# unordered:
# with open(arguments['<yaml>'], 'r') as stream:
#     d = yaml.load(stream)

# ordered:
with open(arguments['<yaml>'], 'r') as stream:
    d = ordered_load(stream, yaml.SafeLoader)



bmi = round(d['kg'] / (d['cm'] * 0.01)**2, 1)
d['bmi'] = str(bmi).replace('.', ',')

d['broca'] = d['cm'] - 100



# http://stackoverflow.com/questions/6288892/convert-datetime-format
dob = datetime.strptime(d['dob'], '%d.%m.%Y')
d['alter'] = calculate_age(dob) 



heartref = pd.read_csv(arguments['<ref>'])

# http://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
valuepick = min(heartref['kg'], key=lambda x:abs(x-d['kg']))
if d['geschlecht'] == 'f':
    a = heartref[heartref['kg'] == valuepick][['low female', 'high female']]
    
    # http://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-data-frame
    result = tuple(a.iloc[0])
if d['geschlecht'] == 'm':
    a = heartref[heartref['kg'] == valuepick][['low male', 'high male']]
    
    # http://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-data-frame
    result = tuple(a.iloc[0])
d['herz_range'] = str(result[0]) + ' - ' + str(result[1])



# http://stackoverflow.com/questions/12470665/how-can-i-write-data-in-yaml-format-in-a-file
with open(arguments['<outfile>'], 'w+') as outfile:
    # unordered:
    # outfile.write(yaml.dump(d, default_flow_style=False, allow_unicode=True))
    # ordered:
    ordered_dump(d, Dumper=yaml.SafeDumper, stream=outfile,
      default_flow_style=False, allow_unicode=True)




