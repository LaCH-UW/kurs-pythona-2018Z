import PyPDF2  # wymaga instalacji pypdf2
# https://pythonhosted.org/PyPDF2/

pot_fname = 'dane/pot_2018.pdf'
with open(pot_fname, 'rb') as fp:  # 'rb' oznacz odczyt w trybie binarnym (nie otwieramy pliku jako tekst, tylko surowe dane)
    pdf = PyPDF2.PdfFileReader(fp)
    print(pdf.numPages)
    a_page = pdf.getPage(102)
    print(a_page.extractText()[:100])
