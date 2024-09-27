import streamlit as st
import spacy
from textblob import TextBlob
import docx2txt
import PyPDF2

# Load Spacy model for text extraction
nlp = spacy.load('en_core_web_sm')

# Function to extract text from DOCX file
def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)

# Function to extract text from PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

# Function to perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity

# Function to validate if text is likely a cover letter
def is_cover_letter(text):
    keywords = ["dear", "sincerely", "cover letter", "application", "position", "resume", "regards"]
    count = sum([1 for word in keywords if word.lower() in text.lower()])
    return count > 2

# Streamlit Page Configuration
st.set_page_config(page_title="Cover Letter Sentiment Analyzer", page_icon="✉️", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1F4E79;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #5D6D7E;
        text-align: center;
        margin-top: -15px;
        margin-bottom: 30px;
    }
    .footer {
        font-size: 0.9rem;
        text-align: center;
        color: #95A5A6;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Title and Subtitle
st.markdown("<div class='main-title'>Cover Letter Sentiment Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Analyze the emotional tone of your cover letter to ensure it conveys the right message.</div>", unsafe_allow_html=True)

# Cover Letter Upload Section
cover_letter_file = st.file_uploader("📄 Upload your Cover Letter (DOCX or PDF)", type=["docx", "pdf"], help="Upload a .docx or .pdf file for sentiment analysis.")

if cover_letter_file is not None:
    # Extract text from cover letter based on file type
    if cover_letter_file.type == "application/pdf":
        cover_letter_text = extract_text_from_pdf(cover_letter_file)
    else:
        cover_letter_text = extract_text_from_docx(cover_letter_file)

    # Check if the extracted text is likely a cover letter
    if is_cover_letter(cover_letter_text):
        st.subheader("📄 Extracted Cover Letter Text")
        st.write(cover_letter_text)

        # Sentiment analysis on the cover letter
        polarity, subjectivity = analyze_sentiment(cover_letter_text)
        st.subheader("🧠 Sentiment Analysis Results")

        # Display progress bars for polarity and subjectivity
        st.markdown("### Sentiment Polarity")
        st.progress((polarity + 1) / 2)  # Normalize polarity (-1 to 1) to range (0 to 1)

        # Display interpretation text for Polarity
        polarity_label = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        st.write(f"**Polarity Score:** {polarity:.2f} ({polarity_label})")

        st.markdown("### Sentiment Subjectivity")
        st.progress(subjectivity)  # Subjectivity is already in range (0 to 1)

        # Display interpretation text for Subjectivity
        subjectivity_label = "Highly Subjective" if subjectivity > 0.5 else "Objective"
        st.write(f"**Subjectivity Score:** {subjectivity:.2f} ({subjectivity_label})")

        # Provide feedback based on polarity
        st.write("---")
        if polarity > 0:
            st.success("The cover letter has a positive tone. This will likely make a good impression.")
        elif polarity < 0:
            st.warning("The cover letter has a negative tone. Consider revising it to sound more positive or neutral.")
        else:
            st.info("The cover letter has a neutral tone. Adding some enthusiasm can help it stand out.")
    else:
        st.error("🚫 The uploaded file doesn't appear to be a cover letter. Please upload the correct file.")
else:
    st.info("📄 Please upload a cover letter for analysis.")

# Footer Section
st.markdown("<div class='footer'>© 2024 Cover Letter Sentiment Analyzer | Designed for Professional Use</div>", unsafe_allow_html=True)
