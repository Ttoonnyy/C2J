import csv
import getopt
import json
import sys


def main(argv):
    csvfile = ""
    jsonfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('Usage: C2J.exe -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: C2J.exe -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            csvfile = open(arg, 'rU')
        elif opt in ('-o', '--ofile'):
            jsonfile = open(arg, 'w')

    try:
        fieldnames = next(csv.reader(csvfile))
        reader = csv.DictReader(csvfile, fieldnames)
    except StopIteration:
        print('Usage: C2J.exe -i <inputfile> -o <outputfile>')
        sys.exit()
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

    print(csvfile.name + " successfully converted")

if __name__ == '__main__':
    main(sys.argv[1:])

