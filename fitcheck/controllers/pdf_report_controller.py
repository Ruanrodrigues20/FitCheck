from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from fitcheck.utils.personal_manager import PersonalManager
from fitcheck.controllers.person_controller import PersonController


class PdfReporterController:
    def __init__(self):
        self._personal = PersonalManager.get_name()


    def mp(self, mm):
        return mm / 0.352777
    

    def cabecalho(self, nome):
        """Desenha o cabeçalho no PDF."""
        largura, altura = A4  

        self.cnv.setFillColor(HexColor("#1976D2")) 
        self.cnv.rect(-1, altura - self.mp(20), largura + 2, self.mp(20), fill=1)

        self.cnv.setFillColor(HexColor("#FFFFFF"))  
        self.cnv.setFont("Helvetica-Bold", 20)
        self.cnv.drawCentredString(largura / 2, altura - self.mp(15), "AVALIAÇÃO FÍSICA")

        self.cnv.setFont("Helvetica", 12)
        self.cnv.drawString(10, altura - self.mp(19), nome)



    def addImagens(self):
        self.cnv.drawImage('./fitcheck/temp/tabela_informacoes_avaliado.png', x=self.mp(-8), y=self.mp(220),  width= self.mp(95), height= self.mp(80))
        self.cnv.drawImage('./fitcheck/temp/tabela_de_massa.png', x=self.mp(80), y=self.mp(220),  width= self.mp(90), height= self.mp(90))
        self.cnv.drawImage('./fitcheck/temp/grafico_biotipo.png', x=self.mp(-5), y=self.mp(145), width= self.mp(105), height= self.mp(100))
        self.cabecalho(f"Personal: {self._personal}")


        self.cnv.drawImage('./fitcheck/temp/tabela_biotipo.png', x=self.mp(90), y=self.mp(149), width= self.mp(120), height= self.mp(105))
        self.cnv.drawImage('./fitcheck/temp/tabela_circunferencias.png', x=self.mp(-11), y=self.mp(-0), width= self.mp(130), height= self.mp(140))
        self.cnv.drawImage('./fitcheck/static/corpo.png', x=self.mp(110), y=self.mp(0), width= self.mp(90), height= self.mp(180))

        self.cnv.showPage()


        self.cnv.drawImage('./fitcheck/temp/table_dobras.png', x=self.mp(-12), y=self.mp(160), width= self.mp(120), height= self.mp(120))
        self.cnv.drawImage('./fitcheck/temp/tabela_composicao_corporal.png', x=self.mp(-7), y=self.mp(65), width= self.mp(115), height= self.mp(120))
        self.cabecalho(f"Personal: {self._personal}")

        self.cnv.drawImage('./fitcheck/temp/tabela_d_osseo.png', x=self.mp(-15), y=self.mp(-25), width= self.mp(130), height= self.mp(120))
        self.cnv.drawImage('./fitcheck/static/desenho.png', x=self.mp(110), y=self.mp(120), width= self.mp(100), height= self.mp(150))
        self.cnv.drawImage('./fitcheck/temp/grafico_pesos.png', x=self.mp(110), y=self.mp(20), width= self.mp(100), height= self.mp(80))


    def create_pdf(self, name):
        self.cnv = canvas.Canvas(f"./resultados/resultado_{name}.pdf", pagesize=A4)
        self.addImagens()  
        self.cnv.save()


