## workflow

### gapfill

This tiny script takes a template and a yaml, and will use the latter to 
fill fields in the former. This is coordinated through corresponding keys,
i.e. a "{{ variable }}" in the template will be filled with its value as 
specified in the yaml "variable: value" entry.

### refsort

Read a Markdown file via standard input and tidy its reference links. 
The reference links will be numbered in the order they appear in the text 
and placed at the bottom of the file.

### metazettel

This tiny script takes as input a table and a yaml file containing 
metadata and other information in the form of key: value pairs. It serves
to quickly summarize a "Kapselzettel".