

import sys
import re


class TemplateConverter:
    COLOR = {
        100: "#ffffff", 95: "#fdf9e8",
        90: "#fbf3d0", 85: "#f8edb9",
        80: "#f6e7a2", 75: "#f4e18a",
        70: "#f2db73", 65: "#f0d55c",
        60: "#eecf44", 59: "#edce42",
        55: "#ebc92d", 50: "#e9c316",
        45: "#d2af14", 40: "#bb9c11",
        35: "#a3880f", 30: "#8c750d",
        25: "#75610b", 20: "#5d4e09",
        15: "#463a07", 10: "#2f2704",
        5: "#171302", 0: "#000000"
    }
    PATTERN = re.compile(r"\{\{(.*?)\}\}")
    URL = "https://github.com/zhuny/tgd_css/raw/master/"

    def __init__(self, string):
        self.string = string

    def get_color_g(self, g):
        s = g.group(1).strip()
        if s.isdigit():
            return self.COLOR[int(s)]
        else:
            return self.URL + s

    def do(self):
        return self.PATTERN.sub(self.get_color_g, self.string)


class MinifyConverter:
    PATTERN = re.compile(r"([\{\}])(.*?)(?=[\{\}])")

    def __init__(self, string):
        self.string = string
        self.depth = 0

    def get_depth(self, g):
        first = g.group(1)
        end = self.string[g.end()]
        if first == "{":
            self.depth += 1
            if end == "}":
                return g.group()
            nl = self.depth
        else:
            self.depth -= 1
            if end == "{":
                nl = self.depth
            else:
                nl = self.depth-1
        s = [first, "\n", "  "*nl, g.group(2)]
        return "".join(s)

    def do(self):
        self.depth = 0
        return self.PATTERN.sub(self.get_depth, self.string)


def main(input_file, output_file):
    with open(input_file, encoding='utf8') as f:
        content = "".join([line.strip() for line in f])

    converters = [
        TemplateConverter,
        MinifyConverter
    ]

    for c in converters:
        content = c(content).do()

    with open(output_file, 'w', encoding='utf8') as f:
        f.write(content)
        f.write("\n")


if __name__ == '__main__':
    main(*sys.argv[1:])



