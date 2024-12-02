#importamos las bibliotecas
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/presentacion.html')
def presentacion():
    return render_template('presentacion.html')

@app.route('/index_t1tarea2.html')
def x():
    return render_template('index_t1tarea2.html')

@app.route('/git.html')
def git():
    return render_template('git.html')

@app.route('/vr.html')
def vr():
    return render_template('vr.html')

@app.route('/scan.html')
def scan():
    return render_template('scan.html')

@app.route('/framework.html')
def framework():
    return render_template('framework.html')

@app.route('/hangman.html')
def hangman():
    return render_template('hangman.html')

@app.route('/entorno_virtual.html')
def entorno_virtual():
    return render_template('entorno_virtual.html')

@app.route('/home')
def home2():
    return render_template('index.html')

@app.route('/flutter_flow.html')
def flutter():
    return render_template('flutter_flow.html')

@app.route('/ibero.html')
def ibero():
    return render_template('ibero.html')

@app.route('/techable.html')
def techable():
    return render_template('techable.html')

if __name__ == '__main__':
    app.run(debug=True)
