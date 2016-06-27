'''
Usage:
  snip.py (-o | --origin) <origin> (-f | --format) <format>

Options:
  -h --help     Show this screen.
  --version     Show version.
  -o --origin   Path to snippet directory.
  -f --format   Path to Sublime Text snippet directory.
'''

from docopt import docopt
import yaml

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    # print(arguments)


with open(arguments['<origin>'], 'r') as stream:
    snippets = yaml.safe_load(stream)


def snip_format(key, value, scope):
    a = '<snippet>\n\t<content><![CDATA[\n'
    b = '\n]]></content>\n<tabTrigger>'
    c = '</tabTrigger>\n<scope>'
    d = '</scope>\n</snippet>'
    return(a + value + b + key + c + scope + d)


# Now for each snippet, we need to create a separate .sublime-snippet
# file in the corresponding Sublime Text 3 folder, which we created
# as a symbolic link (see README in original snippet directory). The
# separate files are necessary for the text expansion to work right.
# The symlinking is just for convenience: That way we get to store
# all the important bits in ~/config, which can be easily version
# controlled.
prefix = arguments['<format>']
for i in snippets.keys():
    k = i
    v = snippets[k]
    s = 'text'

    # Note that a+ creates a file if it does not exist and, crucially,
    # seeks the file to the end. So if you do a read immediately after
    # opening this way, you'll get nothing. You need to seek back to the
    # beginning first: f.seek(0)
    # stackoverflow, 2967194
    with open(prefix + i + '.sublime-snippet', mode='w+') as textfile:
        textfile.write(
            snip_format(k, v, s)
            )
