# Resume_Reviewer

The Automated Resume Reviewer is a tool designed to analyze resumes and match them with job descriptions using Natural Language Processing (NLP). It helps job seekers assess how well their resumes match a job description by identifying keywords and calculating a match score.

This tool supports PDF and DOCX file formats for resumes and text or image formats for job descriptions. The project uses spaCy for text processing, PyPDF2 for PDF handling, and Streamlit for building an interactive web application.

# Tools Used
* Python: The primary programming language used for developing the application.
* spaCy: Used for natural language processing, including tokenization, lemmatization and keyword extraction.
* PyPDF2: Used for extracting text from PDF resumes.
* python-docx: Used for extracting text from DOCX resumes.
* Streamlit: A framework to build an interactive UI for users to upload resumes and job descriptions.
* Tesseract OCR: Used for extracting text from images (screenshots) of job descriptions.

# Key Features
* Resume Matching: The tool compares resumes against job descriptions and calculates a match score.
* Keyword Extraction: Extracts important keywords from both resumes and job descriptions.
* Flexible Input Options: Users can either paste job descriptions or upload screenshots.
* PDF and DOCX Support: Supports popular file formats for resumes (PDF and DOCX).
* Real-Time Results: Interactive web app built using Streamlit for seamless user experience.

# How It Works
* Resume Upload: Upload your resume in PDF or DOCX format.
* Job Description Input: Provide the job description by either pasting the text or uploading a screenshot of the job description.
* Text Processing: The uploaded resume and job description are processed using spaCy for keyword extraction.
* Matching & Scoring: The system calculates the match score based on the overlap of keywords between the resume and the job description.
* Results: The match score and matching/missing keywords are displayed in real time.

# Installation
  Clone the Repository
   1. Clone the repositiory

          git clone https://github.com/Saurabh-SR/automated-resume-reviewer.git

   2. Install Dependencies
      Make sure you have Python 3.6+ installed. Then, install the necessary dependencies:

          cd automated-resume-reviewer
          pip install -r requirements.txt

# Run the Application
  To start the application, run the following command in cmd or bash:

         streamlit run resume_reviewer1.py

  The app will open in your browser, allowing you to upload resumes and job descriptions.

# Requirements
* Python 3.6+
* spaCy: For NLP tasks like tokenization, lemmatization, etc.
* Streamlit: For creating the interactive web interface.
* PyPDF2: For reading and extracting text from PDF resumes.
* python-docx: For reading DOCX resumes.
* Tesseract OCR: For extracting text from images.

# Contributing
Feel free to fork the repository and submit pull requests. If you have any suggestions or bug fixes, please create an issue and we’ll try to resolve it ASAP.

# Future Enhancements
I am currently working on further enhancing the NLP tasks in this project, including better keyword extraction algorithms, improved text matching techniques, and incorporating machine learning models for more accurate job-resume analysis.





