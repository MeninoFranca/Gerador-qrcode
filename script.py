import qrcode
import base64

def gerar_pix(valor, chave_pix, nome_recebedor, cidade_recebedor, txid):
    payload = f"""
    000201
    010212
    26{len(chave_pix) + 7}0014BR.GOV.BCB.PIX{len(chave_pix):02d}{chave_pix}
    52040000
    5303986
    540{len(valor)}{valor}
    5802BR
    5910{nome_recebedor}
    6014{cidade_recebedor}
    62070503***{txid}
    6304
    """
  payload = ''.join(payload.split())