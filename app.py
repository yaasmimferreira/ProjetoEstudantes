from flask import Flask, render_template, request, redirect
lista=[]

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('Home.html', Titulo="Bem-Vindo ao Cadastro Escolar")


@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Titulo="Sobre o nosso site")


@app.route('/galeria')
def galeria():
    return render_template('Sobre.html', Titulo="Sobre o nosso site")


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo="Cadastro de Estudantes")


@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Titulo="Estudantes Cadastrados", lista=lista)


@app.route('/criar', methods=['POST'])
def criar():
    rm = request.form['RM']
    nome = request.form['nome']
    idade = request.form['idade']
    sexo = request.form['sexo']
    serie = request.form['serie']
    estudante = [rm, nome, idade, sexo, serie]
    lista.append(estudante)
    return redirect('/exibir')


if __name__ == '__main__':
    app.run()
