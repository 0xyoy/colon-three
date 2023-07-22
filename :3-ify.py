#!python3
# 
# :3 code generator from brainfuck code. im too lazy to like actually program this shit
# copyright 2023 anna 

import sys

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    code = f.read()
    code = code.replace("[", ":3333")
    code = code.replace("]", ":cccc")
    code = code.replace(",", ":333")
    code = code.replace(".", ":ccc")
    code = code.replace("+", ":33")
    code = code.replace("-", ":cc")
    code = code.replace(">", ":3")
    code = code.replace("<", ":c")
    filename = sys.argv[1].rsplit('.', 1)[0]
    f2 = open(filename + ".:3", "w")
    f2.write(code)
    f2.close()
    f.close()
