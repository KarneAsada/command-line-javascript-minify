#!/usr/bin/python2.4

# Uses Marijn Haverbeke's UglifyJS HTTP API to compress JavaScript
# see http://marijnhaverbeke.nl/uglifyjs
# Alternatively uses Google Closure API

import httplib, urllib, sys
from optparse import OptionParser

def main():

  # Parse arguments and options
  usage = "%prog [options] [input1 .. inputX]"
  parser = OptionParser(usage)
  parser.add_option("-o", "--output", dest="filename",
                    help="Output to FILENAME")
  parser.add_option("-c", "--closure", dest="closure",
                    action="store_true",
                    help="Use Google Closure API instead")
  (options, args) = parser.parse_args()

  js_code = ""

  # Concatenate file input contents
  if len(args) > 0:
    for inputfilename in args:
      inputfile = open(inputfilename, "r")
      js_code += ";" + inputfile.read()

  # Read StdIn if the file inputs were empty
  if js_code == "":
    try:
      js_code = sys.stdin.read()
    except KeyboardInterrupt:
      parser.error("Keyboard Interrupt received.")

  if js_code == "":
    parser.error("No JavaScript was supplied!")

  params = urllib.urlencode([
      ('js_code', js_code),
      ('output_format', 'text'),
      ('output_info', 'compiled_code'),
    ])

  # Set API
  domain = "marijnhaverbeke.nl"
  path   = "/uglifyjs"

  if options.closure:
    domain = "closure-compiler.appspot.com"
    path   = "/compile"


  # Set header and connect
  headers = { "Content-type": "application/x-www-form-urlencoded" }
  conn = httplib.HTTPConnection(domain)
  conn.request('POST', path, params, headers)
  response = conn.getresponse()
  minJs = response.read()

  if options.filename:
    # Write to output
    outputfile = open(options.filename, "w")
    outputfile.write(minJs);
  else:
    print minJs
  conn.close

if __name__ == "__main__":
  main()
