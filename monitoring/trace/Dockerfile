FROM python
ADD requirements.txt /
ADD manual.py /
WORKDIR /
RUN pip install -r requirements.txt
ENV FLASK_APP=manual  
CMD ["flask", "run", "--host", "0.0.0.0"]