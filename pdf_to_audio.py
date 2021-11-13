from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import pyttsx3

file = open("F:\Downloads\Ata da Audiência.pdf", 'rb')  # Diretório do arquivo pdf para conversão em áudio
rscmgr = PDFResourceManager()
restr = io.StringIO()
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rscmgr, restr, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(file)
for page in pages:
    interpreter.process_page(page)
    data = retstr.getvalue()
    print(data)

# leitura de voz

speaker = pyttsx3.init('sapi5') #

voices = speaker.getProperty('voices')

for voice in voices:
    print(voice, voice.id)

speaker.setProperty('voice', voices[0].id)  # voices id seleciona o voz de saída, escolhe a voz diacordo com ordem do seu pacote de linguagem
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-100) # rate-100 é para indicar a velocidade de saída do áudio, quanto menor o valor mais lento


speaker.say(data)  # seleciona qual arquivo vai ser feita a leitura
speaker.runAndWait()
file.close()
