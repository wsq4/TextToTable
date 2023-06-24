from openpyxl import Workbook
from sys import argv

cnt = 1

def parse_cell(cell):
    cell = cell.strip()
    if cell == '':
        return None
    try:
        return int(cell)
    except:
        return cell

def format_ws(ws):
    for col in ws.columns:
        column = col[0].column_letter
        max_length = 0
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = max_length + 2 # 这里设置一个缓冲宽度，避免过于拥挤
        ws.column_dimensions[column].width = adjusted_width


def handle_book(book):
    workBook = Workbook()
    workBook.remove(workBook.active)
    workSheet = None
    book.strip()

    lines = book.split('<NEWLINE>')
    for line in lines:
        line = line.strip()
        if line[0] == '|':
            line = line[1:]
        sheet_flag = str(line).find(':')
        if sheet_flag != -1:
            sheet_name = line[:sheet_flag]
            workSheet = workBook.create_sheet(sheet_name)
            continue
        if workSheet is None:
            continue

        cells = line.split('|')
        workSheet.append(
            [
                parse_cell(cell) for cell in cells
            ]
        )

    for ws in workBook.worksheets:
        format_ws(ws)

    return workBook

print(argv)

with open(argv[1],'r',encoding = 'utf-8') as f:
    for line in f:
        book = handle_book(line)
        book.save(argv[2] + str(cnt) + '.xlsx')
        cnt += 1