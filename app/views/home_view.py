from flask import Flask, render_template
def home_view(app: Flask):
    @app.get('/')
    def home():
        return render_template('home.html'), 200