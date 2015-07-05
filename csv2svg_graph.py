#!/usr/bin/env python
import pygal
import argparse

def parse_csv_file(input_file):
  first = True
  comment = False
  data = {}
  with open(input_file) as f:
    for line in f:
      # skip blank lines
      if not line.isspace():
        if line.startswith("#"):
          comment = line[1:].strip()


        elif first:
          # headers
          fields = line.split(",")
          for field in fields:
            data[field] = []
          first = False
        else:
          # data
          row = line.split(",")
          i = 0
          for field in fields:
            data[field].append(float(row[i]))
            i+=1
  return comment,data

def draw_chart(output_file, title, comment, data):
  line_chart = pygal.Line(show_dots=False)

  if title:
    graph_title = title
  else:
    graph_title = ""

  if comment:
    graph_title += "\n" + comment

  line_chart.title = graph_title
  
  #line_chart.x_labels = map(str, range(2002, 2013))
    
  for field in data:
    line_chart.add(field, data[field])

  line_chart.render_to_file(output_file)

def parse_command_line():
  parser = argparse.ArgumentParser(description="convert csv to svg")
  parser.add_argument("--input_file")
  parser.add_argument("--output_file")
  parser.add_argument("--title")
  args = parser.parse_args()
  return args

def main():
  args = parse_command_line()
  input_file = args.input_file
  output_file = args.output_file
  title = args.title

  print("input_file:  " + input_file)
  print("output_file:  " + output_file)

  comment, data = parse_csv_file(input_file)
  draw_chart(output_file, title, comment, data)

main()
