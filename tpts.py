#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import requests
import re
import os
from pathlib import Path
from django.utils.http import parse_http_date


parser = argparse.ArgumentParser(description="tpts.py")
parser.add_argument("path")
args = parser.parse_args()

p = Path(args.path)
m = re.match(r'(^[^\.]*)\.(.*$)', str(p.name))
filename = m.group(1)
ext = re.sub("[\-\.].*", "", m.group(2))
ext = ext.replace('_large', '')
url = 'https://pbs.twimg.com/media/' + filename + "." + ext + ":orig"
print(url)
r = requests.head(url)
if "Last-Modified" in r.headers:
    lm = parse_http_date(r.headers["Last-Modified"])
    cl = int(r.headers["Content-Length"])

    if p.stat().st_size < cl:
        r = requests.get(url)
        with p.open("wb") as f:
            f.write(r.content)

    nf = p.parent / Path(filename + "." + ext + "-orig." + ext)

    p.rename(nf)
    os.utime(str(nf), (lm, lm))
