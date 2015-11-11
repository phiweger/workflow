## workflow

### gapfill

This tiny script takes as input two files, one some form of text and one yaml, 
replacing the keys in the text file with the values in the yaml. It will match
keys of the for "&key&" with entries in the yaml of the form "key".

### refsort

Read a Markdown file via standard input and tidy its reference links. 
The reference links will be numbered in the order they appear in the text 
and placed at the bottom of the file.

### metazettel

This tiny script takes as input a table and a yaml file containing 
metadata and other information in the form of key: value pairs. It serves
to quickly summarize a "Kapselzettel".