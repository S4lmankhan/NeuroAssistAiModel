# 🧠 NeuroAssist-AI

### A Deep Learning-Powered System for Brain Tumor Detection and Glioma Stage Prediction  
**🔬 Powered by Streamlit | Deployed on HuggingFace Spaces**

---

## 📌 Overview

**NeuroAssist-AI** is a modular smart diagnosis system that mimics real-world clinical pipelines:

1. **Brain Tumor Detection** from MRI/CT grayscale scans using a custom Convolutional Neural Network (CNN).
2. **Glioma Stage Prediction** from numerical gene mutation reports using an Artificial Neural Network (ANN).

This project reimagines the diagnosis workflow in a user-friendly interface — empowering clinicians and students with real-time predictions.

---

## 🔄 Complete Flow (How it Works)

![Pipeline Flowchart](https://github.com/yourusername/NeuroAssist-AI/blob/main/assets/pipeline_flow.png)

**Legend**:  
🧠 = Tumor Detection | 🧬 = Stage Prediction | 📤 = Output | 🖼️ = Image | 📊 = Data

---

## 🌐 Live Demo

👉 Try it now: [Live Web App on HuggingFace Spaces](https://huggingface.co/spaces/yourusername/NeuroAssist-AI)

No installation needed — just upload an MRI or gene mutation file and let the AI do the rest!

---

## 🧪 Research Context

📚 Based on the paper:  
**“Brain Tumor Classification and Glioma Stage Prediction Using Deep Learning”**  
While the original paper lacked public datasets or code, **this implementation was built entirely from scratch** using public MRI datasets and custom model training.

---

## 📂 Dataset Info

- **Source**: [Kaggle - Brain Tumor Dataset](https://www.kaggle.com/datasets)
- **Classes**: `Glioma`, `Meningioma`, `Pituitary`, `No Tumor`
- **Format**: Grayscale `.jpg` images sorted into class folders

---

## 🧠 Model Architectures

### 🔷 CNN – Brain Tumor Detection

| Layer         | Description                                |
|---------------|--------------------------------------------|
| Input         | Grayscale MRI/CT image                     |
| Conv Blocks   | 3 × Conv2D + ReLU + MaxPooling             |
| FC Layers     | Flatten → Dense → Softmax                  |
| Output        | 4-Class Classification                     |
| Framework     | PyTorch                                    |

✅ Trained from scratch  
❌ Dropout not used (no overfitting observed)

---

### 🟢 ANN – Glioma Stage Classification

| Layer         | Description                                |
|---------------|--------------------------------------------|
| Input         | Gene Mutation Test Data                    |
| Dense Layers  | 2-3 Fully Connected Layers                 |
| Activation    | ReLU → Softmax                             |
| Output        | Stage I–IV                                 |
| Framework     | PyTorch                                    |

---

## 💾 Model Files

| File                  | Purpose                        | Location                      |
|-----------------------|--------------------------------|-------------------------------|
| `BTD_model.pth`       | Tumor Detection (CNN)          | 🔗 [Download Link](https://drive.google.com/uc?export=download&id=your_model_id) |
| `glioma_stage.pth`    | Glioma Stage Prediction (ANN)  | Included in `/models`         |

📁 Place `BTD_model.pth` manually inside:

```

/models/BTD\_model.pth

````

### 📥 Optional: Auto Download Script

```python
import os, urllib.request

url = "https://drive.google.com/uc?export=download&id=your_model_id"
path = "models/BTD_model.pth"

if not os.path.exists(path):
    os.makedirs("models", exist_ok=True)
    print("Downloading model...")
    urllib.request.urlretrieve(url, path)
    print("Model downloaded.")
````

---

## ⚙️ Tech Stack

| Category      | Tools / Libraries                   |
| ------------- | ----------------------------------- |
| Language      | Python 3.10+                        |
| DL Framework  | PyTorch                             |
| Web Interface | Streamlit                           |
| Data Handling | OpenCV, NumPy, scikit-learn, pandas |
| Visualization | Matplotlib, Seaborn                 |
| Hosting       | HuggingFace Spaces                  |

---

## 📁 Project Structure

```
NeuroAssist-AI/
├── app.py                    # Streamlit App (Main)
├── detect_tumor.py           # CNN Model logic
├── predict_stage.py          # ANN Model logic
├── utils.py                  # Helper functions
├── models/
│   ├── BTD_model.pth
│   └── glioma_stage.pth
├── images/
│   └── sample.jpg
├── assets/
│   └── pipeline_flow.png
├── requirements.txt
└── README.md
```

---

## 🚀 Running Locally

1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/NeuroAssist-AI.git
cd NeuroAssist-AI
```

2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

3️⃣ Launch Streamlit

```bash
streamlit run app.py
```

---

## ✨ Features

✅ Brain Tumor detection with CNN
✅ Glioma stage classification via gene data
✅ Intuitive web interface
✅ Modular codebase for easy extension
✅ Pretrained models included
✅ Open-source and reproducible

---

## 🧠 Future Enhancements

* 🧬 API integration with real-world gene mutation data sources
* 🤖 AI-powered assistant chatbot using GPT
* 📱 Responsive mobile UI with Streamlit Lite / React Native
* 📊 Medical dashboards for clinics

---

## 📩 Contact

**👨‍💻 Salman Khan**
📧 Email: [your.email@gmail.com](mailto:your.email@gmail.com)
🔗 GitHub: [@yourgithub](https://github.com/yourgithub)

Feel free to connect for collaborations or training notebooks!

---

## ⚠️ Disclaimer

This project is intended **strictly for academic and research purposes.**
Not to be used for clinical decisions without proper medical validation.

---

```

---

> ✅ **What I kept from your version**:
- Streamlit-based deployment  
- Custom flowchart  
- Your app structure and code  
- Gene mutation support  
- Real-time deployment on HuggingFace Spaces  

> 🎨 **What I added/inspired from your friend**:
- Elegant sections  
- Model architecture tables  
- Auto-download code  
- Flow-style headings and icons  
- Feature checklist and tech stack  

Would you like me to export this `README.md` file for you directly?
```
