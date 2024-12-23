# Job Matching System
Tool that enhances the recruitment process by automating the alignment of resumes with job requirements and evaluating interview content.


## Setup Instructions
Follow the steps below to set up and run the ATS Resume Expert locally.

Prerequisites
Python 3.7 or higher

## Step 1: Clone the repository
git clone https://github.com/Anujjhariya/Job-Matching-System.git
cd Job-Matching-System

## Step 2: Create a virtual environment
python -m venv venv

### Activate the virtual environment:
On Windows:
venv\Scripts\activate
On Mac/Linux:
source venv/bin/activate

## Step 3: Install required dependencies
Install all the required packages by running:
pip install -r requirements.txt

## Step 4: Configure environment variables
Create a .env file in the project root directory and add your Google API key as follows:
GOOGLE_API_KEY=your-google-api-key

## Step 5: Install Poppler for PDF processing
On Windows: Download Poppler for Windows ("https://github.com/oschwartz10612/poppler-windows/releases/")
On Linux/Mac: You can install Poppler using package managers like apt or brew.
For example, on Mac:
brew install poppler

## Step 6: Run the application
Start the Streamlit application by running:
streamlit run app.py


## Usage Guidelines
1. Job Description: Input the job description for which you want to evaluate resumes.
2. Resume Upload: Upload a PDF resume that you want to evaluate against the job description.
3. Querying: You can ask specific questions about the resume by entering your query in the designated input box.
4. Response: Based on your query or actions, the model will return insights regarding the alignment of the resume with the job description, including percentage match and strengths/weaknesses.

### Example Queries:
"Does the candidate have experience in Python?"
"What are the strengths of the candidate's profile?"
"How well does the resume match the job description?"


## Architecture Overview
### System Components
1. Streamlit App: Provides the frontend interface for the user to interact with the application, input the job description, upload a resume, and query the resume.
2. PDF Processing: The pdf2image library converts the uploaded PDF resume into an image, which is then encoded in base64 for the Gemini model to process.
3. Google Generative AI (Gemini 1.5-flash): Used to analyze the job description and resume (via PDF content) and generate responses. This involves evaluating how well the resume matches the job description, as well as responding to specific user queries about the resume.
4. Poppler: A required utility for converting PDF files into images. It is essential for extracting content from resumes in PDF format.


## Flow of the System

1. User Input:
The user inputs a job description and uploads a PDF resume via the Streamlit interface.
Optionally, the user can submit a query to request specific details from the resume.

2. PDF Processing:
The PDF file is converted to images using pdf2image. The first page of the PDF is then processed into a byte array and encoded in base64 format.

3. Model Interaction:
The base64-encoded image data of the PDF, along with the job description (if provided), is sent to the Google Gemini 1.5-flash model.
The model analyzes the resume against the job description and generates a response, which is then displayed to the user.

4. Response Generation:
Depending on the user's actions (e.g., querying the resume or asking for a match percentage), the model returns feedback such as:
Whether the resume matches the job description.
Specific details about the resume (e.g., strengths, weaknesses).
The percentage of match and missing keywords.


## Dependencies
The following dependencies are required to run the tool:

1. streamlit: For the web interface.
2. google-generativeai: For using Google's generative AI model.
3. pdf2image: For converting PDF pages to images.
4. Pillow: For image manipulation.
5. python-dotenv: For loading environment variables.
6. requests: For making HTTP requests.

### Install dependencies by running:
pip install -r requirements.txt


