from flask import Flask

def init_app(app: Flask):

    from app.views.home_view import home_view
    from app.views.post_view import post_view


    home_view(app)
    post_view(app)

    return app