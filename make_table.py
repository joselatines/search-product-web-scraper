from rich.console import Console
from rich.table import Table

def make_table(rows, columns, title):
    table = Table(title=title)
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style="bright_green")

    console = Console()
    console.print(table)
