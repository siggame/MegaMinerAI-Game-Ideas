# This takes csv output from a Google Forms asking for game Rankings, and puts them into format for this website:
# http://www.cs.wustl.edu/~legrand/rbvote/calc.html

import csv
import re
import argparse

argparser = argparse.ArgumentParser(
    description='Runs the game voter algorithm'
)

argparser.add_argument('input', nargs='?', action='store', help='the input file', default='data.csv')
args = argparser.parse_args()

games = []
first = True
ignore_columns = 2
regex = re.compile('[^a-zA-Z]')

with open(args.input, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        ballot = None

        if not first:  # we have read the first row, time to make a ballot
            ballot = [[] for game in games]  # a list of list, nested list is for equal preference levels

        for j, col in enumerate(row):
            col = col.replace(" ", "")
            if j < ignore_columns:  # first two rows are timestamp, and email
                continue

            if first:  # first column, which is the games
                game = col[col.find("[") + 1:col.find("]")]
                game = regex.sub('', game)
                games.append(game)
            else:  # it's a ballot
                place = int(col[:-2]) - 1  # "1st" -> 0, , "2nd" -> 1, and so on
                ballot[place].append(games[j - ignore_columns])

        if ballot:
            formatted = []
            for choices in ballot:
                if choices:
                    formatted.append(" = ".join(choices))
            print(" > ".join(formatted))

        first = False
