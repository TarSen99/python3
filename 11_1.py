#!/usr/bin/env python3

fname = input("File name: ")

s = 0
with open(fname) as f:
  pos = f.tell()
  while True:
    content = f.readline()

    newpos = f.tell()
    if newpos == pos:
        break
    else:
        pos = newpos

    s = s + int(content[content.find("\"", content.find("\"") + 1) + 1:].split(' ')[2]);

print("Total bytes: " + str(s))
