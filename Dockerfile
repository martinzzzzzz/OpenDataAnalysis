FROM ubuntu:20.04
WORKIDR /app
COPY . /app
RUN apt-get update && \
    apt-get install -y python3.8 && \
    apt-get clean
RUN apt-get update && \
    apt-get install -y python3-pip
RUN apt-get update
RUN pip install nltk
RUN pip install wordcloud
RUN pip install matplotlib
RUN pip install pytest
RUN pip install lxml
RUN python3 -c "import 
RUN nltk;nltk.download('stopwords');nltk.download('punkt')"
CMD ["python3" , "practica.py"]

