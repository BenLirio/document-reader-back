FROM python AS dev

WORKDIR /flask-app

# install requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY web ./web

ENV FLASK_APP=web/app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]