from flask import Flask, render_template

app = Flask(__name__) # Instancia de la clase Flask

posts = []

# Creando las rutas y vistas para renderizar los templates
@app.route("/")
def index():
    # Flask trae por defecto un motor de renderizado de plantillas llamado Jinja2
    # render_template("template a renderizar", Contexto en clave-valor que se le pasa al template)
	return render_template("index.html", num_posts=len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
	return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/") # Ruta para POST
@app.route("/admin/post/<int:post_id>/") # Ruta UPDATE
def post_form(post_id=None): # Se da el valor por defecto, por si la ruta es usada solo para POST
	return render_template("admin/post_form.html", post_id=post_id)