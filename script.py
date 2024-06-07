from flask import Flask, request, jsonify
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

def gerar_pix(valor, chave_pix, nome_recebedor, cidade_recebedor, txid):
    payload = f"""
    000201
    010212
    26{len(chave_pix) + 7}0014BR.GOV.BCB.PIX{len(chave_pix):02d}{chave_pix}
    52040000
    5303986
    54{len(valor)}{valor}
    5802BR
    5910{nome_recebedor}
    6014{cidade_recebedor}
    62070503***{txid}
    6304
    """
    payload = ''.join(payload.split())
    
    crc16 = calcular_crc16(payload)
    payload += crc16
    
    return payload

def calcular_crc16(payload):
    polinomio = 0x1021
    resultado = 0xFFFF
    
    for byte in payload.encode('utf-8'):
        resultado ^= (byte << 8)
        for _ in range(8):
            if (resultado & 0x8000) != 0:
                resultado = (resultado << 1) ^ polinomio
            else:
                resultado = resultado << 1
            resultado &= 0xFFFF
    return f"{resultado:04X}"

