    #!/usr/bin/env python
# coding: utf-8

# In[7]:

import PyPDF2
import docx 
import spacy # for NLP task


# In[8]:


def resume_text_pdf(file):                # This is for the pdf folders
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def resume_text_word(file):
    reader = docx.Document(file)
    text = ""
    for para in reader.paragraphs:
        text += para.text + "\n"
    return text

# ## NLP TASK
# Tokenization using spacy <br/>
# lemmatizing all the words and filttering out irrelevent ones

# In[9]:


nlp = spacy.load("en_core_web_sm")

def keywords(text, key):
    doc = nlp(text)
    resume_key = set() # set because it does not allow duplicates
    for token in doc:
        if token.is_alpha and not token.is_stop:
            resume_key.add(token.lemma_.lower())
    matching_keywords = keywords.intersection(set(key))
    return matching_keywords
    
# ## Now Calculating score 
# score is basically the ratio of matching keywords to the total number of job related keywords expressed as percentage

# In[10]:


def calculating_score(resume_key, key):
    match = len(resume_keywords)
    total = len(key)
    score = (match/ total) * 100
    missing_key = list(set(key) - resume_key)
    return score, missing_key


# ## Lets do a Image scrapping or word preprocessing for JD now 
# I am Using pytesseract to extract word from either screen shot taken from user of his job description
# or User can copy paste the whole job description

# In[14]:


import pytesseract
from PIL import Image
import re


# In[20]:


def preprocess_text(text):
    doc = nlp(text.lower())  
    tokens = [
        token.lemma_
        for token in doc
        if token.is_alpha and not token.is_stop and token.pos_ in {"NOUN", "VERB", "ADJ"} # this was done to only extract nouns, verbs and adjective in keywords
    ]
    return set(tokens)

def extract_image_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f'Error extracting text from image : {e}'


## Ok now Lets make an custom web application using streamlit

import streamlit as st

st.title("Automated Resume Reviewer")

upload = st.file_uploader("Upload your resume", type=["pdf", "docx"])
resume_text = ""
if upload:
    if upload.name.endswith(".pdf"):
        resume_text = resume_text_pdf(upload) # for pdf folders
    elif upload.name.endswith(".docx"):
        resume_text = resume_text_word(upload) # for word folders
    else:
        st.error("Unsupported file format!") # other folders are not supported for now


# In[19]:


st.write("Now")
st.write("Provide the Job Description: ")
jd = st.radio("How would provide JD to match your resume to the JD", ("Copy-paste JD text", "Upload JD Screenshot") )

jd_text = ""  # whole JD text will be inputed here
if jd == "Copy-paste JD text":
    jd_text = st.text_area("Paste the Job Description here:")
elif jd == "Upload JD Screenshot":
    jd_image = st.file_uploader("Upload the JD Screenshot", type=["jpg", "jpeg", "png"])
    if jd_image is not None:
        jd_text = extract_image_text(jd_image)
        st.write("Extracted Job Description:")
        st.write(jd_text)


# In[22]:


if resume_text and jd_text:
    # Preprocess JD and Resume
    jd_keywords = preprocess_text(jd_text)
    resume_keywords = preprocess_text(resume_text)

    # Find Matching and Missing Keywords
    matching_keywords = jd_keywords.intersection(resume_keywords) # intersection is used to take out common between both jd and resume keywords 
    missing_keywords = jd_keywords - resume_keywords # this will provide whats missing in resume or you should add in resume
    
    # Calculate Match Score
    match_score = (len(matching_keywords) / len(jd_keywords)) * 100 if jd_keywords else 0  # the final score basically percentage of keywords present in both by jd keywords + it checks if jd keywords is not empty
                                                                                           
    # Display Results
    st.subheader("Resume Analysis Results")
    st.write(f"Resume Match Score: {match_score:.2f}%")
    st.write("Matching Keywords:", ", ".join(sorted(matching_keywords)))
    st.write("Missing Keywords:", ", ".join(sorted(missing_keywords)))
