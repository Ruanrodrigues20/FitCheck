from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from fitcheck.utils.personal_manager import PersonalManager
import env
import os


class PdfReporterController:
    SAVE_GRAPHS_PATH = env.SAVE_GRAPHS_PATH
    RESULTS_DIR = env.RESULTS_DIR
    STATIC_IMAGES_PATH = env.STATIC_IMAGES_PATH

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



    def add_imagens(self):
        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'tabela_de_imc.png'),x=self.mp(138), y=self.mp(220), width= self.mp(105), height= self.mp(90))
        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'tabela_informacoes_avaliado.png'), x=self.mp(-8), y=self.mp(220),  width= self.mp(95), height= self.mp(80))
        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'tabela_de_massa.png'), x=self.mp(77), y=self.mp(220),  width= self.mp(90), height= self.mp(90))
        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'grafico_biotipo.png'), x=self.mp(-5), y=self.mp(145), width= self.mp(105), height= self.mp(100))
        self.cabecalho(f"Personal: {self._personal}")


        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'tabela_biotipo.png'), x=self.mp(90), y=self.mp(120), width= self.mp(120), height= self.mp(105))
        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'tabela_circunferencias.png'), x=self.mp(-11), y=self.mp(-0), width= self.mp(130), height= self.mp(140))
        self.cnv.drawImage(os.path.join(self.STATIC_IMAGES_PATH,'corpo.png'), x=self.mp(110), y=self.mp(0), width= self.mp(90), height= self.mp(150))

        self.cnv.showPage()


        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'table_dobras.png'), x=self.mp(-12), y=self.mp(160), width= self.mp(120), height= self.mp(120))
        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'tabela_composicao_corporal.png'), x=self.mp(-7), y=self.mp(65), width= self.mp(115), height= self.mp(120))
        self.cabecalho(f"Personal: {self._personal}")

        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'tabela_d_osseo.png'), x=self.mp(-15), y=self.mp(-25), width= self.mp(130), height= self.mp(120))
        self.cnv.drawImage(os.path.join(self.STATIC_IMAGES_PATH,'desenho.png'), x=self.mp(110), y=self.mp(140), width= self.mp(100), height= self.mp(130))
        self.cnv.drawImage(os.path.join(self.SAVE_GRAPHS_PATH,'grafico_pesos.png'), x=self.mp(110), y=self.mp(20), width= self.mp(100), height= self.mp(100))


    def create_pdf(self, name):
        nome_pdf = f"resultado_{name}.pdf"
        local = os.path.join(self.RESULTS_DIR, nome_pdf )

        self.cnv = canvas.Canvas(local, pagesize=A4)
        self.add_imagens()  
        self.cnv.save()
