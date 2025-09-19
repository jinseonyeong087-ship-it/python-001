from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def create_shape_pdf(filename):
    # A4 크기 (단위: point)
    width, height = A4

    # 캔버스 생성
    c = canvas.Canvas(filename, pagesize=A4)

    # 한글 폰트 등록 (Windows - 맑은고딕)
    pdfmetrics.registerFont(TTFont('MalgunGothic', 'C:/Windows/Fonts/malgun.ttf'))

    # 배경 사각형 (LIGHT_GRAY)
    c.setFillColor(colors.lightgrey)
    c.setStrokeColor(colors.darkgrey)
    c.rect(50, 600, 500, 100, fill=1, stroke=1)

    # 텍스트 출력
    c.setFillColor(colors.black)
    c.setFont('MalgunGothic', 18)
    c.drawString(60, 640, "이 사각형 안에 들어있는 텍스트입니다.")

    # PDF 저장
    c.save()
    print(f"{filename} 생성 완료!")

if __name__ == "__main__":
    create_shape_pdf("shape-demo-python.pdf")
