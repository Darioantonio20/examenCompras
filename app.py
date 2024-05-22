from flask import Flask, render_template, request

app = Flask(__name__)

# Lista global para almacenar productos
productos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entrada = request.form['entrada']
        try:
            # Dividir la entrada en descripción y precio
            descripcion, precio_str = entrada.rsplit(' ', 1)
            precio = float(precio_str)
            iva = precio * 0.16  # Suponiendo un IVA del 16%
            total = precio + iva

            producto = {
                'descripcion': descripcion.strip(),
                'precio': f"{precio:.2f}",
                'iva': f"{iva:.2f}",
                'total': f"{total:.2f}"
            }
            productos.append(producto)
        except ValueError:
            pass  # Manejar entradas inválidas silenciosamente

    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
