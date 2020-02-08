import json
import sys


def fileReader(f):
    # opens file given as argument
    companyPairings = {}
    lineList = f.read().split("-\n")
    # don't like this special casing
    lineList.remove("|")
    for e in lineList:
        # removes all the bits we don't want
        a = e.translate(str.maketrans({"|": "", "\n": "", "]": "", "-": "", " ": ""}))
        # splits into acronym and company name
        companyPairings[a.split("[[")[0]] = a.split("[[")[1]
    # creates data.json file in same directory as this file
    with open("data.json", "w") as outfile:
        json.dump(companyPairings, outfile)


if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    fileReader(file)
