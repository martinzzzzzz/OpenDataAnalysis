#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:09:50 2024

@author: martin
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from grobid_client.grobid_client import GrobidClient
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk as nltk
import os
from lxml import etree

import xml.etree.ElementTree as ET

client = GrobidClient(config_path="OpenDataAnalysis/config.json")

pdf_folder = "OpenDataAnalysis/pdfs"
xml_folder ="OpenDataAnalysis/XMLS"
wordcloud_folder = "OpenDataAnalysis/WordClouds"

num_figures = []
for pdf_file in os.listdir(pdf_folder):
    
    
    
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        
        
        result = client.process_pdf("processHeaderDocument", pdf_path, generateIDs=True, consolidate_header=True, consolidate_citations=True, include_raw_citations=True, include_raw_affiliations=True, tei_coordinates=True, segment_sentences=True)
        if result and "body" in result and "div" in result["body"]:
   
            abstract_xml = result["body"]["div"]
            root = ET.fromstring(abstract_xml)
            doi = root.find(".//idno[@type='DOI']").text
            xml_filename = f"{doi}.xml"
            xml_path = os.path.join(xml_folder, xml_filename)
            with open(xml_path, "w", encoding="utf-8") as xml_file:
                xml_file.write(abstract_xml)
            print(f"Guardado: {xml_path}")
            



for xml_file in os.listdir(xml_folder):
    
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(xml_folder, xml_file)
        
        #load xml file
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # namespace prefix
        xmlns = root.tag[root.tag.find('{')+1 : root.tag.find('}')]
        ns = {'tei': xmlns}
        
        #extract abstract label
        abTag = root.find('.//tei:abstract/tei:p',ns)
        if abTag is None:
            continue
        abstract = abTag.text
        
        
        # tokenize critical words
        tokens = word_tokenize(abstract.lower())
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if not token in stop_words]
        
        #frequency dist.
        
        freq_dist = nltk.FreqDist(tokens)
        
        #word cloud from freq. distribution
        
        wordcloud = WordCloud().generate_from_frequencies(freq_dist)
        
        #save as PNG
        
        plt.imshow(wordcloud,interpolation='bilinear')
        plt.axis("off")
        xml_file_name = xml_file[0:xml_file.find('.')]
        ruta_guardado = os.path.join(wordcloud_folder, f"WordClouds_{xml_file_name}.png")
        plt.savefig(ruta_guardado, bbox_inches="tight")
        
        #Number of figures per article
       
        # parse the XML file using lxml
        tree = etree.parse(xml_path)
        # find the number of figure elements in the file
        num_figures_in_file = len(tree.xpath("//tei:figure", namespaces=ns))
        print(num_figures_in_file)
        # append the number of figures to the list
        for i in range(num_figures_in_file):
            num_figures.append(xml_file)
            
         #create list of links

        f = open("listOfLinks/"+  xml_file[0:xml_file.find('.')] +'.txt', "w")
        # find all the biblStruct elements
        
        biblstructs = tree.xpath("//tei:biblStruct", namespaces=ns)

        # print the contents of each biblStruct element
        
        for biblstruct in biblstructs:
            f.write(etree.tostring(biblstruct, pretty_print=True, encoding='unicode') + '\n')
        f.close()
            
            
plt.clf()
plt.hist(list(el[0: el.find('.')] for el in num_figures), bins=range(len(num_figures)), width= 0.8)

plt.xlabel("Name of Articles", fontsize=12)
plt.xticks(rotation=25, ha='right', fontsize=8)
plt.subplots_adjust(bottom=0.4, left=0.3)
plt.ylabel("Number of Figures")
plt.savefig('figuresperArticle/figure.png')


