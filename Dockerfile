FROM python:3.8-alpine

WORKDIR /app

#Copy everythin in the working directory
COPY . /app
RUN python3 -m venv .venv
RUN . .venv/bin/activate
RUN pip install -r requirements.txt

CMD [ "gunicorn", "--bind", "0.0.0.0:3000" ,"wsgi:application" ] 