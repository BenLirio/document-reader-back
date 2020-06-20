from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def my_background_task(arg1, arg2):
    result = arg1 + arg2
    return result


@app.route('/')
def hello_world():
    my_background_task.delay(10, 20)
    return 'ello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
