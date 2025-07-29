import streamlit as st
from ocr_module import extract_text_from_image, extract_medicines
from gpt_module import get_medicine_explanation
from tts_module import speak_text
import tempfile

st.set_page_config(page_title="MediExplain AI 💊", layout="centered")
st.title("💊 MediExplain AI")
st.write("An AI Assistant to Help Elderly Understand Their Prescriptions")

uploaded_file = st.file_uploader("📷 Upload a prescription image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    with st.spinner("🔍 Extracting text from prescription..."):
        raw_text = extract_text_from_image(temp_path)
        st.text_area("📝 Extracted Text", raw_text, height=200)

    meds = extract_medicines(raw_text)
    if meds:
        st.subheader("🧠 Medicine Explanations:")
        for med in meds:
            with st.spinner(f"Explaining {med}..."):
                explanation = get_medicine_explanation(med)
                st.success(f"💊 {med}: {explanation}")
                speak_text(explanation)
    else:
        st.warning("No medicines found. Please try a clearer image.")
