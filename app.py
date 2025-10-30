from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'lel_ses_me_cai'

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/calcular', methods=['GET','POST'])
def calcular():
    if request.method == "POST":
        peso = float(request.form['peso'])
        altura_cm = float(request.form['altura'])
        altura_m = altura_cm / 100
        error=None

        if altura_m <= 0:
            Error = "La altura debe ser mayor que cero."
        else:
            imc = peso / (altura_m ** 2)
            if imc < 18.5:
                categoria = "Bajo peso"
            elif imc < 24.9:
                categoria = "Normal"
            elif imc < 29.9:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidad"
            resultado = f"Tu IMC es {imc:.2f}. Categoría: {categoria}"
            return render_template('resultado.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(debug=True)
