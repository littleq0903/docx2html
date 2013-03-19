from docx2html.core import convert

if __name__ == "__main__":
    import sys
    try:
        import_filename = sys.argv[1]
    except:
        print 'Please provide the filename, like `python -m docx2html.tool foo.docx`'
        sys.exit(1)
    html = convert(import_filename)
    new_html = open(import_filename.replace('.docx','.html'), 'w')
    new_html.write(html)
    new_html.close()

