from flask import Flask, render_template

app = Flask('My first site')


@app.route('/')
def start_jo():
    return 'Привіт, друже'


@app.route('/list')
def list_ul():
    a = []
    with open('eng.txt', 'r') as file_one:
        k = file_one.readlines()
    for text in k:
        a.append(text)
    return render_template('list.html', title='List', a=a)


@app.route('/show/<int:number>')
def show_number(number):
    a = []
    with open('eng.txt', 'r') as file_one:
        k = file_one.readlines()
    for text in k:
        a.append(text)
    b = a[0:number]
    return render_template('show_number.html', title='Show number', number=number, b=b)


@app.route('/filter/<word>')
def filter_word(word):
    a = []
    with open('eng.txt', 'r') as file_one:
        k = file_one.readlines()
    for text in k:
        a.append(text)
    return render_template('filter_word.html', title='Filter word', word=word, a=a)


if __name__ == '__main__':
    app.run()
