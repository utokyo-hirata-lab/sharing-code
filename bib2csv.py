import PyPDF2, glob, csv, sys

class Color:
    RED       = '\033[31m'
    END       = '\033[0m'

filename = sys.argv[1]

with open(filename, 'w', encoding='shift_jis') as f:
    fieldnames = ['Author','Title','Subject']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    list_pdf = glob.glob('*.pdf')
    for name_pdf in list_pdf:
        pdf = PyPDF2.PdfFileReader(name_pdf)
        try:
            writer.writerow({'Author':pdf.documentInfo['/Author'].replace('\xa0', ''),'Title':pdf.documentInfo['/Title'].replace('\xa0', ''),'Subject':pdf.documentInfo['/Subject'].replace('\xa0', '')})
        except (KeyError,UnicodeEncodeError,PyPDF2.utils.PdfReadError, TypeError, ValueError):
            print(Color.RED + 'Error' + Color.END+' : '+name_pdf)
