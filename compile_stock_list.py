#!/usr/bin/env python

from yahoo_finance import Share

google = Share('YHOO')
print google.get_open()