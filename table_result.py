import prettytable

from parser import parser_1, parser_2, parser_3


table = prettytable.PrettyTable(("Link", "Buy", "Sell"))

data = [
    parser_1("USD"),
    parser_2("USD"),
    parser_3("USD"),
]

for row in data:
    table.add_row(row)



