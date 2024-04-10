from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm, PostForm, LoginForm

from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from models import users, get_user, User
from urllib.parse import urlparse

app = Flask(__name__) # Instancia de la clase Flask

# Secret key para la correcta funcionalidad de los formularios
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

login_manager = LoginManager(app)
login_manager.login_view = "login"

posts = []

# Creando las rutas y vistas para renderizar los templates
@app.route("/")
def index():
    # Flask trae por defecto un motor de renderizado de plantillas llamado Jinja2
    # render_template("template a renderizar", Contexto en clave-valor que se le pasa al template)
	return render_template("index.html", posts=posts)

@app.route("/p/<string:slug>/")
def show_post(slug):
	return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required #Para proteger las vistas
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data

        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)

        return redirect(url_for('index'))
    return render_template("admin/post_form.html", form=form)


@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # Crea una instancia de la clase creada en forms.py
    form = SignupForm()
    # form.validate_on_submit(), valida si es correcta la info enviada.
    # form.name.data, obtiene la informacion enviada por el cliente en el formulario
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        # request.args.get, obtiene la informacion enviada en la url 
        # (En caso de que el usuario haya querido entrar a una url habilitada solo para usuarios autorizados y no anonimos).
        next_page = request.args.get('next', None) # Si no se envia nada, queda como None
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("signup_form.html", form=form) # Si no es "post", muestra el formulario como contexto

#Valida si el usuario que esta en la sesion es anonimo o no.
#El metodo user_loader, le envia el user_id de la session.
@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

#Ruta para login de usuarios
@app.route('/login', methods=['GET', 'POST'])
def login():
    #current_user, metodo del flask_login
    if current_user.is_authenticated: #Si hay un usuario en session, redirecciona
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data) #Obtiene el usuario de la lista de usuarios
        if user is not None and user.check_password(form.password.data): #Revisa que sea True el user y la contraseña enviadas
            login_user(user, remember=form.remember_me.data) #logea al usuario con el metodo de flask_login
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))