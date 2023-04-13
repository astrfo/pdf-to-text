import PyPDF2


if __name__ == '__main__':
    filename = 'C51.pdf'

    with open(filename, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        num_pages = len(pdf.pages)
        text = ''
        for i in range(num_pages):
            page = pdf.pages[i]
            text += page.extract_text()
    
    with open('paper.txt', 'w', encoding='utf-8') as f:
        f.write(text)
