from python:3.10.0a2-buster

#make a working directory
WORKDIR /app


#install depedentcies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy source code
COPY /app .


#run application
CMD ["python", "test.py"]