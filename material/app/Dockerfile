FROM python:3.12-slim

WORKDIR /123456

COPY app.py /123456 

COPY requirements.txt /123456

# COPY asecert.pem /123456/
# COPY asekey.pem /123456/

RUN pip install -r requirements.txt 

EXPOSE 5001

CMD [ "flask","run","--host=0.0.0.0","--port=5001"]