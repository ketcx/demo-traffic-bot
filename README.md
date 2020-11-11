<h1 align='center'>Driving tutor chatbot (spanish)</h1>
<p align="center">Armando Medina</p>
<p align="center">(November, 2020)</p>

<p align="center">
  <img src="https://github.com/ketcx/demo-traffic-bot/blob/master/data/diagram.png" width=600>
</p>

## 1. Introduction

<p>
The purpose of this project is the proof of concept of the stack provided by Amazon for the creation of chatbots. Our goal is to create a demo of a chatbot from the Dominican Republic driving manual.
</p>

## 2. Business Problem

<p>
Our problem is having an easy way to get answers to questions about the Dominican Republic driving manual.
</p>

## 3. Data

<p>The data of this project are based on the driving manual of the INTRANT (Dominican Republic traffic institution). The idea is to show how a chatbot can be created from unstructured text. For the purposes we have taken the document in pdf and converted it into a file with a txt extension.

Both documents can be found in the data folder of this project.
</p>

## 4. Methodology

<p>
For this project we are going to create a notebook that is used to handle the data, we are going to extract the questions and answers from the document, create a database of topics and then generate synonyms like exploring the most common words in the document. Then using Amazon Lex we will create a chatbot that will connect to two lambda functions, one to validate the input and another to evaluate the Intent that the user really wants.
</p>

## 5. Results and Discussion

<p>
As a result we have a chatbot that shows the potential of this pipeline, with the improvements indicated in the section of future works.

**DEMO:** 

URL: [Driving Tutor chatbot (spanish)](https://dev.d163kgck980qhu.amplifyapp.com/)

Example of questions:

- Cómo se acredita la existencia del seguro?
- Qué elementos pueden ser fuente de distracciones?
- Qué efectos tiene el estrés en los conductores?

</p>

## 6. Future work

<p>
For future work, text extraction can be improved, in addition to using Amazon Kendra as a knowledge base of Lex bots and the use of ElasticSearch. Regarding the interface we use Amplify's ui library for this interface it can be custom.
</p>