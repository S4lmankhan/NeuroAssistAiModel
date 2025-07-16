import os, requests, streamlit as st
import torch
from torchvision import transforms
from PIL import Image
from TumorModel import TumorClassification, GliomaStageModel

# ── Helpers to download from Google Drive ─────────────────────────────────────
def download_from_gdrive(file_id, dest):
    if os.path.exists(dest):
        return
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    r = session.get(URL, params={'id': file_id}, stream=True)
    for k, v in r.cookies.items():
        if k.startswith('download_warning'):
            r = session.get(URL, params={'id': file_id, 'confirm': v}, stream=True)
            break
    with open(dest, 'wb') as f:
        for chunk in r.iter_content(32768):
            if chunk:
                f.write(chunk)

# ── Your Google Drive File IDs ────────────────────────────────────────────────
TUMOR_ID = "1juQk4AhIi7u7I41uttCUpJYsvtsPyZUy"      # BTD_model.pth
STAGE_ID = "19MrhHVQbSlVmaV-bP_FIpcY5t9wjKMSX"      # glioma_stages.pth

# ── Download models once ───────────────────────────────────────────────────────
download_from_gdrive(TUMOR_ID, "BTD_model.pth")
download_from_gdrive(STAGE_ID, "glioma_stages.pth")

# ── Load models into memory ────────────────────────────────────────────────────
@st.cache_resource
def load_models():
    tm = TumorClassification()
    sm = GliomaStageModel()
    tm.load_state_dict(torch.load("BTD_model.pth", map_location="cpu"))
    sm.load_state_dict(torch.load("glioma_stages.pth", map_location="cpu"))
    tm.eval(); sm.eval()
    return tm, sm

tumor_model, glioma_model = load_models()

# ── Labels & Preprocessing ────────────────────────────────────────────────────
tumor_labels = ['glioma','meningioma','notumor','pituitary']
stage_labels = ['Stage 1','Stage 2','Stage 3','Stage 4']

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5],[0.5])
])

# ── Build Streamlit UI ────────────────────────────────────────────────────────
st.set_page_config(page_title="Brain Tumor Predictor", layout="centered")
st.title("🧠 Brain Tumor Detector & Glioma Stage Predictor")

tab1, tab2 = st.tabs(["Tumor Detection","Glioma Stage"])

with tab1:
    st.header("Upload MRI Image")
    img_file = st.file_uploader("", type=["jpg","png","jpeg"])
    if img_file:
        img = Image.open(img_file).convert("L")
        st.image(img, use_column_width=True)
        x = transform(img).unsqueeze(0)
        with torch.no_grad():
            out = tumor_model(x)
            pred = tumor_labels[int(torch.argmax(out))]
        st.success(f"**Tumor Type:** {pred.upper()}")

with tab2:
    st.header("Patient & Genetic Info")
    gender = st.radio("Gender", ["Male","Female"])
    age    = st.slider("Age",1,100,25)
    genes  = {g: st.radio(g, [0,1], horizontal=True)
              for g in ["IDH1","TP53","ATRX","PTEN","EGFR","CIC","PIK3CA"]}
    if st.button("Predict Stage"):
        vals = [0 if gender=="Male" else 1, age] + list(genes.values())
        x = torch.tensor([vals], dtype=torch.float32)
        with torch.no_grad():
            out = glioma_model(x)
            pred = stage_labels[int(torch.argmax(out))]
        st.success(f"**Glioma Stage:** {pred}")
