from flask import Flask
from celery import Celery

def make_celery(app=None):
    app = app or create_app()
    celery = Celery(
        app.import_name,
        backend="redis://localhost:6379/0",
        broker="redis://localhost:6379/1"
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

def create_app():
    app = Flask(__name__)
    celery = make_celery(app)
    from app.all import bp
    app.register_blueprint(bp)
    return app