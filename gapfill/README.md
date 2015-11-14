## gapfill

Use this script as a hacky text expander, which replaces the keys in a document (markdown, rtf, txt) with the values specified in a yaml file. The key format is the one employed by the Jinja2 template engine, i.e. 

> On the {{ date }} we met {{ name }} wearing a {{ color }} coat.

is transformed into

> On the 2015-01-01 we met Mr. White wearing a black coat.

where the yaml file specifies

    name: Mr. White
    date: 2015-01-01
    color: black
    pina: colada
    foo: bar
    price: 200

Usage pattern:

    python gapfill.py -h
    python gapfill.py -t example.md -o examplemod.md -y example.yaml

If keys are specified in the template which have no corresponding entry in the yaml, the script will complain: `missing key(s) in yaml: variable`. The yaml on the other hand can contain keys which the template does not.

Some ways to specify a field (which can contain valid python code, see below):

* {{ variable }}
* {{ variable[0] }} # in yaml "variable: [a, b, c]", returns "a"
* {{ variable|default('place value here') }}

## Templating

[start here](https://wiki.python.org/moin/Templating)

[some more background](http://www.simple-is-better.org/template/)

a [crude alternative](https://docs.python.org/3.4/library/string.html#template-strings) from the standard library

[Jinja2](http://jinja.pocoo.org/) and the [syntax details](http://jinja.pocoo.org/docs/dev/templates/)

