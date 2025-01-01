import streamlit as st
import json
import pyperclip

# Navigation
st.set_page_config(page_title="Cold Email Generator", layout="wide")
st.markdown(
    """
    <h1 style="text-align: center;">Cold Email Generator</h1>
    """,
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <h4 style="text-align: center;">Cold Email Settings</h4>
        """,
        unsafe_allow_html=True
    )
    receiver_email = st.text_input("Recruiter Email")
    receiver_name = st.text_input("Recruiter Name")
    role_type = st.selectbox("Job Role Type", ["Custom", "Data Analysis", "Data Engineer", "Data Science", "SDE"], key="role_select")
    custom_role = ""
    if role_type == "Custom":
        custom_role = st.text_input("Enter Custom Role", key="custom_role_key")
    job_description = st.text_area("Paste Job Description Here")
    uploaded_resume = st.file_uploader("Upload Resume", type=["pdf", "docx"])
    
    submit_button = st.button("Generate Cold Email")
    
    if submit_button:
        if not receiver_email or not receiver_name or not job_description:
            st.error("Please fill all required fields.")
        else:
            st.success("Cold Email Generated Successfully!")

if 'cold_email' not in st.session_state:
    st.session_state.cold_email = ""

with col2:
    st.markdown(
        """
        <h4 style="text-align: center;">Generated Email</h4>
        """,
        unsafe_allow_html=True
    )
    
    # Generate email only on form submission
    if submit_button and receiver_email and receiver_name and job_description:
        role = custom_role if role_type == "Custom" else role_type

        # Load sender details from JSON
        with open("sender_details.json", "r") as f:
            sender_details = json.load(f)

            sender_name = sender_details.get("name", "[Your Name]")
            sender_degree = sender_details.get("degree", "[Your Degree]")
            sender_major = sender_details.get("major", "[Your Major]")
            sender_university = sender_details.get("university", "[Your University]")
            sender_graduation = sender_details.get("graduation", "[Graduation Date]")
            sender_linkedin = sender_details.get("linkedin", "[LinkedIn]")
            sender_portfolio = sender_details.get("portfolio", "[Portfolio]")

            # Generate cold email
            st.session_state.cold_email = f"""
            **Subject:** {role} Role
            
            **Hi {receiver_name},**

            I’m {sender_name}, a {sender_degree} student in {sender_major} at {sender_university}, graduating in {sender_graduation}. My experience aligns with the {role} role at [Company Name], ... (Generated from Job Description and Resume)

            I’ve attached my resume and would welcome the opportunity to discuss how I can contribute to [Company Name].

            --
            **Best Regards,**  
            {sender_name}  
            LinkedIn: {sender_linkedin}  
            Portfolio: {sender_portfolio}
            """

    # Display the email if it exists in session state
    if st.session_state.cold_email:
        st.markdown(st.session_state.cold_email)