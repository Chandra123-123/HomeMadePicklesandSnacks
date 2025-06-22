from flask import Flask, request, jsonify, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission (optional)
        return redirect(url_for('sucess'))
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login (optional auth logic)
        return redirect(url_for('sucess'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup (optional)
        return redirect(url_for('sucess'))
    return render_template('signup.html')

@app.route('/sucess')
def sucess():
    return render_template('sucess.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Handle order placement (optional)
        return redirect(url_for('sucess'))
    return render_template('checkout.html')

@app.route('/snackes')
def snackes():
    return render_template('snackes.html')

@app.route('/veg_pickles')
def veg_pickles():
    return render_template('veg_pickles.html')

@app.route('/non_veg_pickles')
def non_veg_pickles():
    return render_template('non_veg_pickles.html')


if __name__ == '__main__':
    app.run(debug=True)