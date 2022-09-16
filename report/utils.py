from openpyxl import load_workbook


# takes excel file and makes report into, then returns changed file
def make_report(file_name):
    excel_file = load_workbook(file_name)
    page = excel_file["Лист1"]

    # {"Bob":
    #     {
    #         "01.01.2022": 150,
    #         "02.01.2022": 180,
    #         # ...
    #     }
    #     # 'Julian'
    #     # ...
    # }

    lst = page["A"]
    res = {}
    for cell in lst:  # A2
        row_number = cell.row  # 2

        if row_number == 1:
            continue

        name = cell.value
        if name not in res:
            res[name] = {}

        date_cell = page[f"B{row_number}"].value  # 01.01.2022

        if date_cell not in res[name]:
            res[name][date_cell] = 1
        else:
            res[name][date_cell] += 1

    print("result dict is rdy!")

    # header
    row_number = 1
    page[f"E{row_number}"] = "seller name"
    letters = "FGHIJKLMNOPQR"  # ...
    i = 0
    for date_value in res[name]:
        # print(date_value)
        page[f"{letters[i]}{row_number}"] = date_value
        i += 1

    # cells
    for name, date_qty_dict in res.items():
        row_number += 1

        page[f"E{row_number}"] = name

        i = 0
        for date_value, qty in date_qty_dict.items():
            page[f"{letters[i]}{row_number}"] = qty
            i += 1

    excel_file.save("rep2.xlsx")
    return excel_file
