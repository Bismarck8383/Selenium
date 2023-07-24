import pdfkit

# Ruta al archivo HTML
html_file = 'index.html'

# Ruta de salida del archivo PDF
pdf_file = 'mi_archivo.pdf'

# Convertir HTML a PDF
pdfkit.from_file(html_file, pdf_file)
