from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from fitcheck.utils.personal_manager import PersonalManager
from fitcheck.controllers.person_controller import PersonController


class PdfReporterController:
    def __init__(self, person):
        self.imagens = {"biotipo": "./fitcheck/temp/biotipo.png",
                        "grafico_peso": "./fitcheck/temp/grafico_pesos.png",
                        "tab_bio": "./fitcheck/temp/table_biotipo.png",
                        "circuferencia": "./fitcheck/temp/table_circuferencia.png",
                        "corporal": "./fitcheck/temp/table_comp_corporal.png",
                        "dc": "./fitcheck/temp/table_dc.png",
                        "do": "./fitcheck/temp/table_do.png"}
        
        self._person = person
        self.cnv = canvas.Canvas("./resultados/resultado_ruan.pdf", pagesize=A4)
        self._personal = PersonalManager.get_name()
        self.cabecalho(f"Personal: {self._personal}")
        self.cnv.setFillColor(HexColor("#000000"))  # Cor preta
        self.info_aluno()
        self.addImagens()  # Adicionar imagens no relatório
        self.cnv.save()

    def mm2p(self, mm):
        """Converte milímetros para pontos (medida usada pelo ReportLab)."""
        return mm / 0.352777

    def cabecalho(self, nome):
        """Desenha o cabeçalho no PDF."""
        largura, altura = A4  # Tamanho da página

        # Fundo do cabeçalho
        self.cnv.setFillColor(HexColor("#1976D2"))  # Cor azul
        self.cnv.rect(-1, altura - self.mm2p(20), largura + 2, self.mm2p(20), fill=1)

        # Texto do título
        self.cnv.setFillColor(HexColor("#FFFFFF"))  # Cor branca
        self.cnv.setFont("Helvetica-Bold", 20)
        self.cnv.drawCentredString(largura / 2, altura - self.mm2p(15), "AVALIAÇÃO FÍSICA")

        # Nome do usuário
        self.cnv.setFont("Helvetica", 12)
        self.cnv.drawString(10, altura - self.mm2p(19), nome)

    def info_aluno(self):
        """Desenha as informações do aluno no PDF."""
        largura, altura = A4  
        y = altura - self.mm2p(40)  # Posição inicial Y
        margem = self.mm2p(20)      # Margem para o texto

        # Definir a cor do texto como preta
        self.cnv.setFont("Helvetica", 12)

        # Concatenar as informações e desenhá-las na mesma linha
        texto = (f"NOME: {self._person.name}     "
                 f"SEXO: {self._person.gender}    "
                 f"IDADE: {self._person.age()}    "
                 f"PESO (kg): {self._person.ult_weight()}    "
                 f"ESTATURA (m): {self._person.height:.2f}")

        # Escrever todo o texto na mesma linha
        self.cnv.drawString(margem, y, texto)

    def addImagens(self):
        """Adiciona as imagens ao relatório."""
        largura, altura = A4
        # Ajustando a posição da imagem 'biotipo'
        self.cnv.drawImage(self.imagens['corporal'], self.mm2p(0), self.mm2p(180), width=self.mm2p(80), height=self.mm2p(80))

p = PersonController()
luan = p.get_person(4)
PdfReporterController(luan)
