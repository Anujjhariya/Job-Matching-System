from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

load_dotenv()

# Configure Google Generative AI with the API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the Poppler path
poppler_path = r"C:/poppler/Library/bin"  # Update this to your Poppler path

# Function to interact with Gemini API
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Updated PDF processing function
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            # Convert the PDF to images
            images = pdf2image.convert_from_bytes(
                uploaded_file.read(), poppler_path=poppler_path
            )

            # Process the first page of the PDF
            first_page = images[0]

            # Convert the first page to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            # Encode the image to base64 for the Gemini API
            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
                }
            ]
            return pdf_parts
        except Exception as e:
            raise Exception(f"Error processing the PDF: {e}")
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App
st.set_page_config(page_title="Resume Analyser Expert")
st.header("Job Matching System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage match")

submit_query = st.button("Submit Query")




# Prompts for Generative AI
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage and then keywords missing and last final thoughts.
"""

# Button logic
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")





user_query =  st.text_input("Enter your query:",key = "query")

if submit_query:
    if uploaded_file is not None and user_query:
        pdf_content = input_pdf_setup(uploaded_file)
        # Use the query provided by the user as the prompt
        response = get_gemini_response(user_query, pdf_content, input_text)
        st.subheader("Response to Your Query")
        st.write(response)
    else:
        st.write("Please upload the resume and enter a query")

