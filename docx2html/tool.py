from docx2html.core import convert

if __name__ == "__main__":
    import sys
    import_filename = sys.argv[1]
    print sys.argv[1]
    html = convert(import_filename)
    new_html = open(import_filename.replace('.docx','.html'), 'w')
    new_html.write(html)
    new_html.close()

