from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__, static_url_path='/static')
bootstrap = Bootstrap(app)


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def homepage():
    if request.method == "POST":
        print(request.form)
        name = request.form["text"]
        email = request.form["email"]
        phone = request.form["phone"]
        print(name, email)
        with open("Client_data.txt", "w") as file:
            file.write(name)
            file.write(email) 
            file.write(phone)
    return render_template('home.html')


@app.route('/eng')
def english():
    return render_template('eng.html', title = "English")
    


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)))



