from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        # Traitez les données ici (par exemple, vérifiez l'authentification, enregistrez les données dans une base de données, etc.)
        return f"Nom d'utilisateur: {username}, Mot de passe: {password} (Ceci est juste un exemple de traitement)"
    return render_template(print("c'est envoyé"))
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True port=5000)
