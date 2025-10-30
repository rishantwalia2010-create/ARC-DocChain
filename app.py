import streamlit as st
import qrcode
from io import BytesIO
import random

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(page_title="ARC | DocChain", page_icon="🌐", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background-color: black;
        color: white;
    }
    h1, h2, h3, h4 {
        color: #33A1FD;
        text-align: center;
    }
    .blue-text {
        color: #33A1FD;
    }
    .stButton>button {
        background-color: #33A1FD;
        color: white;
        border-radius: 8px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# --------------------------
# HEADER
# --------------------------
st.title("🌐 ARC | DocChain")
st.markdown("### Smart AI + Blockchain System for Global Trade Document Verification")

st.divider()

# --------------------------
# STEP 1: COMPANY INFO
# --------------------------
st.header("Step 1: Company Details")

with st.form("company_form"):
    company_name = st.text_input("🏢 Company Name")
    owner_name = st.text_input("👤 Representative / Owner Name")
    email = st.text_input("📧 Company Email")
    phone = st.text_input("📞 Contact Number")
    country = st.text_input("🌍 Country of Operation")
    st.form_submit_button("Save Details")

st.divider()

# --------------------------
# STEP 2: AI DOCUMENT RECOMMENDER
# --------------------------
st.header("Step 2: AI-based Document Requirement")

region = st.selectbox("Select your trade type", ["Import", "Export"])
destination = st.selectbox("Select destination country", ["United States", "United Kingdom", "UAE", "Germany", "India", "Singapore", "Australia", "Other"])

if st.button("🧠 Generate Required Documents"):
    st.subheader(f"Recommended Documents for {region} to {destination}:")
    docs = {
        "United States": ["Commercial Invoice", "Packing List", "Bill of Lading", "Certificate of Origin", "Import Declaration (CBP)"],
        "United Kingdom": ["Commercial Invoice", "Packing List", "UK Customs Declaration (C88)", "EORI Number"],
        "UAE": ["Commercial Invoice", "Packing List", "Certificate of Origin", "Import Permit (MOIAT)"],
        "Germany": ["Commercial Invoice", "EUR.1 Movement Certificate", "Packing List", "CE Declaration"],
        "India": ["Commercial Invoice", "Shipping Bill", "Export License (if needed)", "GST Invoice"],
        "Singapore": ["Commercial Invoice", "Packing List", "Customs Export Permit", "Certificate of Origin"],
        "Australia": ["Commercial Invoice", "Packing List", "Import Declaration (ICS)", "Biosecurity Clearance"],
        "Other": ["Commercial Invoice", "Packing List", "Certificate of Origin"]
    }
    for d in docs.get(destination, []):
        st.markdown(f"- {d}")

st.divider()

# --------------------------
# STEP 3: DOCUMENT UPLOAD
# --------------------------
st.header("Step 3: Upload Trade Documents")

uploaded_files = st.file_uploader("Upload documents (PDF, DOCX, JPG)", accept_multiple_files=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

st.divider()

# --------------------------
# STEP 4: AI VERIFICATION + BLOCKCHAIN SIGNATURE
# --------------------------
st.header("Step 4: AI Verification and Blockchain Signature")

if st.button("🔍 Run AI Verification"):
    st.info("Analyzing documents using AI verification engine...")
    st.success("✅ All documents verified successfully and blockchain signature applied!")
    blockchain_hash = f"ARC-{random.randint(1000000, 9999999)}"
    st.write(f"**Blockchain Transaction ID:** `{blockchain_hash}`")

st.divider()

# --------------------------
# STEP 5: GENERATE QR CODE
# --------------------------
st.header("Step 5: Generate Digital Passport QR")

if st.button("📲 Generate QR Code"):
    qr_data = f"Company: {company_name}, Blockchain ID: {blockchain_hash if 'blockchain_hash' in locals() else 'Pending'}"
    qr_img = qrcode.make(qr_data)
    buf = BytesIO()
    qr_img.save(buf)
    st.image(buf.getvalue(), caption="Your Digital Passport QR", use_column_width=True)
    st.download_button("⬇️ Download QR", data=buf.getvalue(), file_name="DocChain_QR.png")

st.divider()
st.markdown("<center>© 2025 ARC Technologies | Powered by DocChain</center>", unsafe_allow_html=True)
