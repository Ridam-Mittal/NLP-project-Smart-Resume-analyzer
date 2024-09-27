import streamlit as st
import pandas as pd
import os
from PIL import Image
import warnings
import plotly.express as px

# Streamlit Application Title with Style (Visible and Professional)
st.markdown(
    """
    <style>
        .title-style {
            font-size: 50px;
            font-weight: bold;
            color: #f0f0f0;  /* Light color for dark theme */
            text-align: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .subheader-style {
            font-size: 24px;
            color: #f0f0f0;  /* Light color for dark theme */
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="title-style">Smart Resume Analyzer</div>', unsafe_allow_html=True)

# Sidebar for switching between User and Admin modes with Selectbox
st.sidebar.title("Navigation")
mode = st.sidebar.selectbox("Choose Mode:", ("User", "Admin"))

# Display initial image or background image
try:
    initial_image = Image.open(r"Logo/ats.png")  # Use an image named 'ats.png' in the same directory
    st.image(initial_image, use_column_width=True)
except FileNotFoundError:
    st.warning("Initial image not found. Please ensure 'ats.png' is in the correct path.")

# Initialize session state variables for tracking login status
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Callback function to update login status
def login():
    st.session_state.logged_in = True

def logout():
    st.session_state.logged_in = False

# User Mode Section
if mode == "User":
    st.markdown('<div class="subheader-style">User Mode</div>', unsafe_allow_html=True)
    st.write("Choose an option below to proceed:")

    # Radio button to select either Resume or Profile Picture upload
    user_option = st.radio("What would you like to upload?", ('Resume', 'Profile Picture'), index=0)

    if user_option == 'Resume':
        # Display File Upload for Resume
        uploaded_file = st.file_uploader("Upload your resume (PDF or Word)", type=["pdf", "docx"], label_visibility="collapsed")

        # Placeholder for parsed resume data
        resume_data = None

        # Parsing Function for Resume (placeholder for now)
        def parse_resume(file):
            # Implement file reading and parsing logic here (PDF/Docx)
            resume_text = None  # Will hold the extracted text from the resume
            file_type = os.path.splitext(file.name)[1]

            if file_type == ".pdf":
                resume_text = "Parsing logic for PDF goes here"
                # Example: Use PyPDF2 or pdfplumber
            elif file_type == ".docx":
                resume_text = "Parsing logic for DOCX goes here"
                # Example: Use python-docx

            return resume_text

        # Resume File Upload Handling
        if uploaded_file is not None:
            # Parsing the uploaded resume file
            resume_data = parse_resume(uploaded_file)

            # Display the parsed resume text
            if resume_data:
                st.subheader("Parsed Resume Data:")
                st.text(resume_data)
            else:
                st.error("Could not parse the resume. Please check the file format.")

    elif user_option == 'Profile Picture':
        # Display File Upload for Profile Picture
        uploaded_image = st.file_uploader("Upload your profile picture (JPEG or PNG)", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

        # Image Processing Function (placeholder for now)
        def process_image(image_file):
            # You can process the image here using PIL or other libraries
            img = Image.open(image_file)
            return img

        # Image File Upload Handling
        if uploaded_image is not None:
            # Process and display the uploaded image
            st.subheader("Uploaded Profile Picture:")
            img = process_image(uploaded_image)
            st.image(img, caption="Uploaded Image", use_column_width=True)

# Admin Mode Section
elif mode == "Admin":
    st.markdown('<div class="subheader-style">Admin Mode</div>', unsafe_allow_html=True)

    # Initialize session state for `logged_in` if not already set
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'state_changed' not in st.session_state:
        st.session_state.state_changed = False

    # Check if the user is already logged in
    if st.session_state.logged_in:
        st.success("Welcome Admin")

        # Display user data and admin-specific features
        st.header("*User's👨‍💻 Data*")
        df = pd.DataFrame({
            'ID': [1, 2, 3],
            'Name': ['John Doe', 'Jane Doe', 'Alice Smith'],
            'Email': ['john@example.com', 'jane@example.com', 'alice@example.com'],
            'Resume Score': [85, 90, 88],
            'Timestamp': ['2024-09-20', '2024-09-21', '2024-09-22'],
            'Total Page': [2, 3, 2],
            'Predicted Field': ['Data Science', 'Software Engineering', 'Machine Learning'],
            'User Level': ['Intermediate', 'Expert', 'Beginner'],
            'Actual Skills': ['Python, ML', 'Java, JS', 'TensorFlow'],
            'Recommended Skills': ['Deep Learning', 'System Design', 'Advanced ML'],
            'Recommended Course': ['DL with PyTorch', 'Microservices', 'Advanced DL']
        })
        st.dataframe(df)

        # Example Pie Chart using Plotly
        fig = px.pie(df, values='Resume Score', names='Predicted Field', title='Predicted Field Distribution')
        st.plotly_chart(fig)

        # Button to Log Out with callback function
        if st.button('Logout'):
            st.session_state.logged_in = False
            st.session_state.state_changed = not st.session_state.state_changed  # Toggle state_changed to force rerender

    else:
        # Admin Login Page
        st.subheader("Please Log In to Access Admin Features")
        ad_user = st.text_input("Username")
        ad_password = st.text_input("Password", type='password')

        # Button for Login
        if st.button('Login'):
            if ad_user == 'ridam112004' and ad_password == 'abcd':  # Replace with your actual credentials
                st.session_state.logged_in = True
                st.session_state.state_changed = not st.session_state.state_changed  # Toggle state_changed to force rerender
                st.success("Login Successful! Redirecting...")
            elif ad_user == '' or ad_password == '':
                st.warning("Please enter both Username and Password")
            else:
                st.error("Invalid Username or Password")

# Footer with Professional Styling
st.markdown("<hr style='border: 1px solid #666;'>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align: center; color: #cccccc; font-size: 14px;'>
    Make sure the uploaded files are in the correct format. We support PDF, DOCX for resumes and JPG, PNG for images.
    </p>
    """,
    unsafe_allow_html=True,
)
