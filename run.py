from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # Instancia de la clase Flask

# Secret key para la correcta funcionalidad de los formularios
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

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

""" @app.route("/signup/", methods=["GET", "POST"]) # Tipos de CRUD que admite la ruta
def show_signup_form():
    if request.method == 'POST':
		# request.form, obtiene la informacion enviada por el cliente en el formulario,
		# en el input de atributo name="name"
        name = request.form['name'] 
        email = request.form['email']
        password = request.form['password']
		# request.args.get, obtiene la informacion enviada en la url.
        next = request.args.get('next', None) # Si no se envia nada, queda como None
        if next:
            return redirect(next) # Si es True (Se pasa info. por la url), redirecciona hacia el "next" entregado
        return redirect(url_for('index')) # Si el "post" es correcto, redirecciona al index
    return render_template("signup_form.html") # Si no es "post", muestra el formulario """

from forms import SignupForm

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=form)