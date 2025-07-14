from flask import render_template, redirect, url_for, flash, abort, session
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.utils import secure_filename
from ext import app, db
from models import User, Book
from forms import RegisterForm, LoginForm, BookForm
import os


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "adminpassword"


@app.route("/")
def home():
    books = Book.query.all()
    role = current_user.role if current_user.is_authenticated else None
    return render_template("mainpage.html", books=books, role=role)


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "adminpassword"

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        if User.query.filter_by(username=form.username.data).first():
            flash("Username already exists. Choose a different one.", "danger")
            return render_template("register.html", form=form)

        image = form.profile_img.data
        image_filename = image.filename
        upload_folder = os.path.join(app.root_path, "static", "uploads")
        os.makedirs(upload_folder, exist_ok=True)
        image_path = os.path.join(upload_folder, image_filename)
        image.save(image_path)

        user_role = "Admin" if (
            form.username.data == ADMIN_USERNAME and
            form.password.data == ADMIN_PASSWORD
        ) else "user"


        new_user = User(
            username=form.username.data,
            password=form.password.data,
            birthday=form.birthday.data,
            gender=form.gender.data,
            country=form.country.data,
            img=f"uploads/{image_filename}",
            role=user_role
        )

        db.session.add(new_user)
        db.session.commit()

        flash("✅ Registered successfully! Now log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)




@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data: 
            login_user(user)
            session['cart'] = []
            session["role"] = user.role

            flash("✅ Logged in successfully!", "success")
            return redirect(url_for("home"))
        else:
            flash("Wrong username or password", "danger")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect("/")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/detailed/<int:book_id>")
def detailed(book_id):
    book = Book.query.get(book_id)
    return render_template("detailed.html", book=book)

@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

@app.route('/add-book', methods=['GET', 'POST'])
@login_required
def add_book():
    if current_user.role != "Admin":
        abort(403)

    form = BookForm()
    if form.validate_on_submit():
        image = form.cover_image.data
        filename = secure_filename(image.filename)

        upload_path = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)

        image.save(os.path.join(upload_path, filename))

        new_book = Book(
            name=form.title.data,
            author=form.author.data,
            price=form.price.data,
            img=filename,
            description=form.description.data
        )

        db.session.add(new_book)
        db.session.commit()
        flash(" Book added successfully!", "success")
        return redirect("/")

    return render_template("add_book.html", form=form)


def get_cart_items():
    return session.get('cart', [])

@app.route("/cart")
def cart():
    cart_book_ids = get_cart_items()
    length = len(cart_book_ids)
    if cart_book_ids:
        books = Book.query.filter(Book.id.in_(cart_book_ids)).all()
        total = sum(float(book.price) for book in books)
    else:
        books = []
        total = 0.0

    return render_template('cart.html', books=books, cart_items=length, total=total)

@app.route('/add_to_cart/<int:book_id>', methods=["GET","POST"])
def add_to_cart(book_id):
    cart = session.get('cart', [])
    cart.append(book_id)
    session['cart'] = cart
    return redirect("/")

@app.route("/remove_from_cart/<int:book_id>")
def remove_from_cart(book_id):
    cart = session.get("cart", [])
    if book_id in cart:
        cart.remove(book_id)
        session["cart"] = cart
        flash("Book removed from cart.", "success")
    else:
        flash("Book not found in cart.", "warning")
    return redirect(url_for("cart"))

@app.route("/admin/functions")
@login_required
def admin_functions():
    if current_user.role != "Admin":
        abort(403)

    users = User.query.all()
    return render_template("admin_functions.html", users=users)

@app.route("/admin/delete/<int:user_id>")
@login_required
def delete_user(user_id):
    if current_user.role != "Admin":
        abort(403)

    user = User.query.get_or_404(user_id)
    if user.role != "Admin":
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully.", "success")

    return redirect("/admin/functions")





