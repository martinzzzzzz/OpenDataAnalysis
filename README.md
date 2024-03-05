[![DOI]
#OpenDataAnalysis

##Description

##Requirements

##Documentation

##Installation and execution instructions

###Grobid generation

The Grobid XML files are generated using the Grobid Server [grobid server](https://github.com/kermitt2/grobid) through the Grobid-Client for Python [grobid_client](https://github.com/kermitt2/grobid_client_python)

for installing the python client:

```
pip install grobid_client_python

```
for running the server

```
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

```
###Anaconda enviroment

You need to have anaconda / miniconda installed

```
conda config --add channels conda-forge
conda create -n [nombre_de_tu_enviroment] python=3.8 nltk grobid_client_python wordcloud matplotlib lxml pytest
conda acivate [nombre_de_tu_enviroment]

```


###Docker enviroment

You need to have docker installed

```
docker build -t opendataanalysis

docker run opendataanalysis

```

###Running examples
`figuresperArticle` contains the histogram of the number of figures per article
`listOfLinks` contains the list of links in each article
`pdfs` contains the 10 pdfs used as input
`tests`contains a script with a set of tests for the script
`WordClouds` contains the word clouds plots of each document
`XMLS` contains the XML grobid response for each pdf input

##Preferred citation

If you use this code or results in your research, please cite our paper:

```bib
@article{opendataanalysis,
  title   = {{opendataanalysis}},
  author  = {Martin Quevedo},
  year    = {2023},
  doi     = {https://zenodo.org/badge/latestdoi/599152914}
}
