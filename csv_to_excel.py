import csv
import xlwt
from flask import current_app


def transform(filename):
    wkb = xlwt.Workbook()
    sheet = wkb.add_sheet("sheet1")
    with open(filename, encoding="gb18030") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            for j, d in enumerate(row):
                sheet.write(i, j, row[j])
    base_dir = current_app.config['BASE_DIR']
    new_filename = filename.split(".")[0] + ".xlsx"
    wkb.save(base_dir + new_filename)
    return new_filename
