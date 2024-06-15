import win32com.client
import os
import csv
from tqdm import tqdm

word = win32com.client.Dispatch("Word.Application")
word.visible = False

def word_to_csv(filename_in, filename_out):
    # Open word file
    wb = word.Documents.Open(os.path.abspath(filename_in))
    doc = word.ActiveDocument

    # to index table and find merged cells
    for i, table in enumerate(doc.Tables):

        # keep track of all cell ids [(row, col)...]
        cell_ids = []
        for cell in table.Range.Cells:
            cell_ids.append((cell.RowIndex, cell.ColumnIndex))

        # calculate size of the table
        rows = max([c[0] for c in cell_ids]) + 1
        cols = max([c[1] for c in cell_ids]) + 1

        # find merged cells and store index in the cell ID
        for cell in table.Range.Cells:
            ri = cell.RowIndex
            ci = cell.ColumnIndex
            sr = 1
            sc = 1

            # the cell below it is merged if we cannot find it in cell_ids
            while ri+sr < rows and (ri+sr, ci) not in cell_ids:
                sr += 1

            # the cell on the right is merged if we cannot find it in cell_ids
            while ci+sc < cols and (ri, ci+sc) not in cell_ids:
                sc += 1

            cell.ID = f'{i},{sr},{sc}'

    # open destination csv file and start to parse line by line
    with open(filename_out, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["text",  "style", "space_before", "space_after",
                        "col_id", 'row_id', 'cell_width', 'cell_height', 'cell_id'])

        # Access each paragraph
        for paragraph in tqdm(doc.Paragraphs):

            cell_width = ''
            cell_height = ''
            col_id = ''
            row_id = ''
            cell_id = ''

            text = paragraph.Range.Text

            # try if the paragraph is in the table
            try:
                col_id = paragraph.Range.Cells[0].ColumnIndex
                row_id = paragraph.Range.Cells[0].RowIndex
                cell_id, cell_height, cell_width = \
                    paragraph.Range.Cells[0].ID.split(',')
            except:
                # the above code will fail if it's not in the table
                pass
            
            # find the style and all base styles of the paragraph
            style = paragraph.style
            style_list = []

            while len(str(style))>0:
                try:
                    style_list.append(str(style))
                    style = style.BaseStyle
                except:
                    break

            space_before = paragraph.SpaceBefore
            space_after = paragraph.SpaceAfter

            writer.writerow(
                ['\n'.join(text.splitlines()), '/'.join(style_list), space_before, space_after, col_id, row_id, cell_width, cell_height, cell_id])
    # Close the document (optional)
    wb.Close()


# "test 1"
# word_to_csv('./download/doc/LCEWA01_110106_00070.doc',
#             './parsed/doc_csv/LCEWA01_110106_00070.csv')

# "test 2"
# word_to_csv('./download/doc/LCEWA01_110114_00277.doc',
#             './parsed/doc_csv/LCEWA01_110114_00277.csv')

folder='./download/doc'
folder_out='./parsed/doc_csv'
for file in os.listdir(folder):
    if file.endswith('.doc'):
        print(os.path.join(folder, file), os.path.join(
            folder_out, file.split('.')[0]+'.csv'))
        word_to_csv(os.path.join(folder, file), os.path.join(
            folder_out, file.split('.')[0]+'.csv'))
word.Quit()
