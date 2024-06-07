document.getElementById('pixForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var valor = document.getElementById('valor').value;
    fetch('/gerar_pix', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ valor: valor })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('qrcode').innerHTML = `<img src="data:image/png;base64,${data.qrcode}" alt="QR Code">`;
        document.getElementById('copiaCola').innerText = `Código Copia e Cola: ${data.copiaCola}`;
    });
});
