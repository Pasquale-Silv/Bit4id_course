from Course_Bit4id.TenthDay.Project_Work_con_classi_codifica.CoderCifraMessaggio import Coder
from Course_Bit4id.TenthDay.Project_Work_con_classi_codifica.MessaggioPrivato import MessaggioPrivato
from Course_Bit4id.TenthDay.Project_Work_con_classi_codifica.UtenteMittente_e_Destinatario import UtenteMittente, \
    UtenteDestinatario
from datetime import datetime

mittente1 = UtenteMittente('Pasquale', 'Silvestre', 23, 'Pasquale@live.it')
destinatario1 = UtenteDestinatario('Bryan', 'La Monica', 24, 'Bryan_La_Monica#live.com')

messaggio_privato1 = MessaggioPrivato('Documenti', 'Hai comprato i fuochi d\'artificio per stasera?'
                                      , mittente1, destinatario1, datetime.now())

coder1 = Coder(messaggio_privato1)
print(coder1)
print("Messaggio passato al coder:", coder1.MessaggioPrivatoDaCifrare)

coder1.cifraMessaggioConfidenziale()
print(coder1.parolaCifrata)

coder1.decifraMessaggioConfidenziale()
print(coder1.parolaDecifrata)
