from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 20)
    c.drawString(100, 750, "Hello, Python PDF!")
    c.save()

if __name__ == "__main__":
    create_pdf("hello.pdf")
    print("PDF 생성 완료: hello.pdf")
