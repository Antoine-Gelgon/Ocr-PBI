#!/usr/bin/env python

# usage: $ python print-glyphs-fontforge.py "League-Gothic.ufo"

import fontforge
import sys

font = sys.argv[1]

for glyph in fontforge.open(font).glyphs():
    glyph.export("png/" +glyph.glyphname + ".png", 600)



fontforge.open(font).generate('ocr-pbi.ttf')
