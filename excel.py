import openpyxl

def fetch_data_from_excel(file_path):
    # Load the Excel workbook
    wb = openpyxl.load_workbook(file_path)

    # Select the active sheet
    sheet = wb.active

    # Iterate through rows and columns to fetch data
    for row in sheet.iter_rows(values_only=True):
        for cell in row:
            print(cell)

    # Close the workbook
    wb.close()

# Example usage
file_path = "example.xlsx"  # Replace with the path to your Excel file
fetch_data_from_excel(file_path)
