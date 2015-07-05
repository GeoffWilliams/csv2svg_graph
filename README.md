# csv2svg_graph
Convert csv to SVG graphs - the easy way!

# Features
* Reads a CSV file and turns it into a line graph
* Uses [pygal](http://pygal.org/)
* Uses lines starting with `#` as a title
* Automatically maps CSV headers to the legend
* Blank lines are automatically skipped

# Missing features
This is a very quick and dirty CSV to SVG converter which I wrote because I 
couldn't for the life of me find a good python tool do to this already.

This tool is pretty basic at the moment and is missing things like better
error handling, X-axis labels, different graph types, etc.

If your interested in helping developing this tool, drop me a line!

# Usage
```shell
$ csv2svg_graph.py --input_file /path/to/csv_file --output_file output_file.svg
```

# Example
![Generated graph](https://cdn.rawgit.com/GeoffWilliams/csv2svg_graph/master/example/memory.svg)
Generated from a CSV file in the format:
```csv
# Command line arguments:-XX:+UseConcMarkSweepGC -Xmx6000m 

used memory, free memory, total memory, xmx
5,242,247,5933
161,86,247,5933
328,116,444,5933
494,156,650,5933
600,394,994,5933
763,231,994,5933
934,610,1544,5933
1055,488,1544,5933
1229,315,1544,5933
1395,148,1544,5933
1554,816,2370,5933
1697,673,2370,5933
1799,571,2370,5933
```


