# Command Line JavaScript Minify Using UglifyJS or Closure

A simple tool that minifies JavaScript files using [Marijn Haverbeke's UglifyJS HTTP API](http://marijnhaverbeke.nl/uglifyjs) or [Google's Closure API](http://closure-compiler.appspot.com/home).  It takes a list of JavaScript files to concatenate or reads from StdIn.

## Usage

    uglifyjs.py [options] [input1 .. inputX]

    Options:
      -h, --help            show this help message and exit
      -o FILENAME, --output=FILENAME
                            Output to FILENAME
      -c, --closure         Use Google Closure API instead

