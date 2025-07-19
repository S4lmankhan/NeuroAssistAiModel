<p align="center">
  <img src="images/banner.png" alt="NeuroAssistAI" width="800"/>
</p>

# 🧠 NeuroAssistAIModel

**Advanced Brain Tumor Detection & Glioma Stage Prediction**  
_Deployed on Streamlit & Vercel_

[🔗 **Run Live on Streamlit**](https://s4lmankhan-neuroassistaimodel.streamlit.app) •  
[🔗 **Embed on Vercel Site**](https://neuroassistai.vercel.app/)

---

## 📌 Overview

**NeuroAssistAIModel** is a two‑stage diagnostic pipeline that brings AI‑powered brain tumor analysis to your browser:

1. **Tumor Type Detection**  
   A custom **CNN** classifies grayscale MRI scans into  
   `Glioma`, `Meningioma`, `Pituitary` or `No Tumor`.  
2. **Glioma Stage Prediction**  
   A compact **ANN** predicts glioma stage (I–IV) from gene‑mutation inputs.

Built in **PyTorch**, presented via **Streamlit**, and embeddable in any site (e.g. [our Vercel front‑end](https://neuroassistai.vercel.app/)).

---

## 🔄 End‑to‑End Pipeline

```mermaid
flowchart LR
    A[🖼️ Upload MRI Image] --> B[🧠 Streamlit UI: Tumor Detection]
    B --> C[CNN Model → Tumor Type]
    C --> D[📤 Display Prediction]

    E[📝 Input Gene Mutations] --> F[🧬 Streamlit UI: Glioma Stage]
    F --> G[ANN Model → Stage I–IV]
    G --> H[📤 Display Stage]

    subgraph "Live Deployments"
      I[Streamlit Cloud] & J[Vercel Site]
    end
    D & H --> I & J
````

---

## 🎯 Why NeuroAssistAI?

* **Clinically Inspired**: Mirrors real diagnostic workflows.
* **Zero‑Install**: Models auto‑download from Google Drive at first run.
* **Dual Deployment**:

  * Interactive demo on **Streamlit**
  * Seamless embed on your **Vercel**‑powered website
* **Extensible**: Easy to swap models or front‑ends.

---

## 📚 Research Basis

Inspired by the study

> “Brain Tumor Classification and Glioma Stage Prediction Using Deep Learning”
> implemented from scratch with public MRI datasets and gene mutation data.

---

## 📂 Dataset

* **Source**: [Kaggle Brain Tumor Dataset](https://www.kaggle.com/datasets)
* **Classes**: `Glioma`, `Meningioma`, `Pituitary`, `No Tumor`
* **Format**: Grayscale `.jpg` in class‑named folders

---

## 🧠 Model Architectures

### 🔷 CNN – Tumor Type Detection

| Layer         | Details                                        |
| ------------- | ---------------------------------------------- |
| **Input**     | 1×224×224 grayscale MRI                        |
| Conv Block ×3 | Conv2D → ReLU → MaxPool2D                      |
| FC Layers     | Flatten → Dense(512) → Dense(256) → Softmax(4) |
| **Output**    | 4‑class probability                            |

### 🟢 ANN – Glioma Stage Classification

| Layer        | Details                                 |
| ------------ | --------------------------------------- |
| **Input**    | 9 numerical features (gene mutations)   |
| Dense Layers | 100 → 50 → 30 neurons, ReLU activations |
| **Output**   | Softmax(4) → Stage I–IV                 |

---

## 💾 Download Pretrained Models

Due to GitHub’s 100 MB limit, download the TumorDetection model externally:

* **TumorClassification (CNN)**
  [Download BTD\_model.pth](https://drive.google.com/uc?export=download&id=1juQk4AhIi7u7I41uttCUpJYsvtsPyZUy)
* **GliomaStageModel (ANN)**
  [Download glioma\_stages.pth](https://drive.google.com/uc?export=download&id=19MrhHVQbSlVmaV-bP_FIpcY5t9wjKMSX)

After downloading, place them in:

```
models/BTD_model.pth  
models/glioma_stages.pth
```

> *Tip:* The app’s `load_models()` will auto‑fetch these if missing.

---

## ⚙️ Tech Stack

| Category      | Tools / Libraries                    |
| ------------- | ------------------------------------ |
| Language      | Python 3.10+                         |
| Deep Learning | PyTorch                              |
| Frontend      | Streamlit                            |
| Data Science  | torchvision, Pillow, NumPy           |
| Hosting       | Streamlit Community Cloud, Vercel    |
| Model Storage | Google Drive (public download links) |

---

## 📁 Project Structure

```
NeuroAssistAIModel/
├── app.py                    # Streamlit application
├── models/
│   ├── TumorModel.py         # CNN & ANN definitions
│   └── (downloaded .pth files)
├── utils.py                  # Helper functions
├── requirements.txt
├── images/                   # UI assets & screenshots
│   └── banner.png
├── assets/
│   └── pipeline_flow.png     # Flowchart graphic (used above)
└── README.md                 # ← You are here
```

---

## 🚀 Installation & Local Run

1. **Clone**

   ```bash
   git clone https://github.com/S4lmankhan/NeuroAssistAiModel.git
   cd NeuroAssistAiModel
   ```

2. **Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```

3. **Install**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run**

   ```bash
   streamlit run app.py
   ```

---

## 🔗 Embedding

Embed in your site via:

```html
<iframe
  src="https://neuroassistai.vercel.app/"
  width="100%" height="800" frameborder="0"
  aria-label="NeuroAssistAI Models">
</iframe>
```

---

## 🤝 Contributing

1. Fork & clone
2. Create a branch: `git checkout -b feat/YourFeature`
3. Commit & push: `git commit -m "Add YourFeature"`
4. Open a Pull Request

---

## 📜 License

This project is licensed under **MIT**. See [LICENSE](LICENSE) for details.

---

## ✉️ Contact

**Salman Khan**
📧 [redhawk112233@gmail.com](mailto:redhawk112233@gmail.com)
🔗 [GitHub @s4lmankhan](https://github.com/S4lmankhan)
