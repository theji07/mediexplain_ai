 💊 MediExplain AI

MediExplain AI is an AI-powered tool that helps elderly individuals understand their prescriptions by providing simple explanations for each medicine, including:

- ✅ **What it is used for**
- 🕒 **When to take it**
- ⚠️ **Possible side effects**

---

## 📷 Features

- Upload a **prescription image** (JPG, PNG)
- Automatically extract medicine names using OCR
- Uses a local/offline AI model to explain medicines
- Clean, simple interface built with **Streamlit**

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.10+
- `streamlit`
- `pytesseract`
- `Pillow`
- `gpt4all`
- A local `.bin` model file (e.g., `ggml-gpt4all-j-v1.3-groovy.bin`)

### 📦 Install dependencies

```bash
pip install -r requirements.txt
📁 Project structure
python
Copy code
mediexplain_ai/
│
├── app.py
├── gpt_module.py
├── requirements.txt
├── sample_prescription.jpg
└── .gpt4all/
    └── models/
        └── ggml-gpt4all-j-v1.3-groovy.bin
🧠 Run the app
bash
Copy code
streamlit run app.py
📁 Model Notes
The .bin model file is not included in this repo due to GitHub file size limits.

You must download the GPT4All model manually and place it inside:

bash
Copy code
.gpt4all/models/
Example model: ggml-gpt4all-j-v1.3-groovy.bin
Download from: https://gpt4all.io/index.html

👨‍💻 Contributors
@theji07

📄 License
This project is open source under the MIT License.
