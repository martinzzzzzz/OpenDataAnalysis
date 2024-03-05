#Rationale

The purpose of the Rationale document is to explain the assumption the programmer takes during the development of the project.

#Draw a keyword cloud based on the words found in the abstract of your papers.

In order to create the keyword clouds , and also the visualization of the number of figures per article plus the list of links found in each paper, i have created a folder called XMLS in which the XML documents resulting from the Grobid call services are saved.

Parting from those XML documents i made the script that accomplish the main objectives of the project.

For the keyword cloud, i created a token for each word of the abstract section in the xml file, and used them for the word figure.

The validation of this point has been made by counting the words in the abstract section of the papers and comparing them with the wordcloud.

#Create a visualization showing the number of figures per article.

This point is accomplished in the folder "figuresperArticle" which are zero as none of the articles i chose has any figure.

For the validation of this fact i checked each article and proved that there are no figures to show in the histogram.

#Create a list of the links found in each paper.

In order to accomplish this last point, i listed the links present in bibliography of the docs, validated by checking the reference section and the list.
