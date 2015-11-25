'''yamlcalc

This script calculates some new keys given a yaml file.

Requires Python 3.X if used with non-ASCII characters in the yaml.

Usage: yamlcalc.py -y <yaml> -r <ref>

Options:
  -h --help         Show this screen.
  -v --version      Show version.
  -y --yaml         /path/to/yaml
  -r --reference    /path/to/heart_weight_reference.csv 

'''



# Avoid writing __pycache__ because this is a Github repo.
# http://stackoverflow.com/questions/154443/how-to-avoid-pyc-files 
import sys
sys.dont_write_bytecode = True

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

e = {} 

try: # in case no value is found for the "kg" and "cm" keys in .yaml
    bmi = round(d['kg'] / (d['cm'] * 0.01)**2, 1)

    e['bmi'] = str(bmi).replace('.', ',')
    e['broca'] = d['cm'] - 100

except TypeError:
    pass


# http://stackoverflow.com/questions/6288892/convert-datetime-format
try:
    dob = datetime.strptime(d['dob'], '%d.%m.%Y')
    e['alter'] = calculate_age(dob) 
except TypeError:
    pass


heartref = pd.read_csv(arguments['<ref>'])

try:
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
    e['gherz_soll'] = str(result[0]) + ' - ' + str(result[1])

except TypeError:
    pass

# print(e)

if e: # if e contains any key:value pairs
    # http://stackoverflow.com/questions/12470665/how-can-i-write-data-in-yaml-format-in-a-file
    with open(arguments['<yaml>'], 'a+') as outfile:
        # unordered:
        # outfile.write(yaml.dump(d, default_flow_style=False, allow_unicode=True))
        # ordered:
        ordered_dump(e, Dumper=yaml.SafeDumper, stream=outfile,
          default_flow_style=False, allow_unicode=True)




