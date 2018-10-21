import csv
import xlwt


def transport(filename):
    wkb = xlwt.Workbook()
    sheet = wkb.add_sheet("sheet1")
    with open(filename, encoding="gb18030") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            for j, d in enumerate(row):
                sheet.write(i, j, row[j])

    wkb.save(filename.split(".")[0] + ".xlsx")

transport("经济-15.csv")
transport("经济-16.csv")
transport("经济-17.csv")
transport("经济-18.csv")
