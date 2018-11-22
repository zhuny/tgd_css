

import sys
import re


COLOR = {
  100: "#ffffff",
  95: "#fdf9e8",
  90: "#fbf3d0",
  85: "#f8edb9",
  80: "#f6e7a2",
  75: "#f4e18a",
  70: "#f2db73",
  65: "#f0d55c",
  60: "#eecf44",
  59: "#edce42",
  55: "#ebc92d",
  50: "#e9c316",
  45: "#d2af14",
  40: "#bb9c11",
  35: "#a3880f",
  30: "#8c750d",
  25: "#75610b",
  20: "#5d4e09",
  15: "#463a07",
  10: "#2f2704",
  5: "#171302",
  0: "#000000"
}



pattern = re.compile(r"\{\{(.*?)\}\}")

with open(sys.argv[1]) as f:
  content = f.read()

def replace(g):
  num = int(g.group(1))
  return COLOR[num]

content = pattern.sub(replace, content)

with open(sys.argv[2], 'w') as f:
  print(content.strip(), file=f)


