## gapfill

Use this script as a hacky text expander, which replaces the keys in a document (markdown, rtf, txt) with the values specified in a yaml file. The key format is hardcoded as "&key", i.e. 

> On the &date we met &name wearing a &color coat.

becomes

> On the 2015-01-01 we met Mr. White wearing a black coat.

where the yaml file specifies

    name: Mr. White
    date: 2015-01-01
    color: black
    pina: colada
    foo: bar
    price: 200

Usage pattern:

    python3 gapfill.py -h
    python3 gapfill.py -i example.md -o examplemod.md -y example.yaml
