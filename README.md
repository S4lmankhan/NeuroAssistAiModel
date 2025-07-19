# 🧠 NeuroAssistAIModel

**Advanced Brain Tumor Detection & Glioma Stage Prediction – now in Streamlit!**

[🔗 **Live Demo** (Streamlit)](https://s4lmankhan-neuroassistaimodel.streamlit.app)

---

## 📌 Overview

NeuroAssistAIModel is a two-stage, PyTorch-powered pipeline that automates:

1. **Brain Tumor Detection** from grayscale MRI images via a custom CNN.  
2. **Glioma Stage Prediction** using patient gene mutation data through an ANN.

Powered by real clinical approaches, this tool supports radiologists and neurologists in early, accurate diagnostics.

---

## 🧪 Live Testing

✔️ Upload a brain MRI to classify tumor type.  
✔️ Provide gene mutation details to predict glioma stage.

[🌐 Launch Live App →](https://s4lmankhan-neuroassistaimodel.streamlit.app)

---

## 📚 Research Basis

Inspired by state-of-the-art research in brain tumor analysis and glioma classification. Designed and implemented from scratch in PyTorch and Streamlit.

---

## 📂 Dataset

- **Source:** Brain Tumor MRI Dataset (e.g., Kaggle)  
- **Classes:** Glioma, Meningioma, Pituitary, No Tumor  
- **Format:** Grayscale .jpg grouped by class

---

## 🧠 Model Architectures

### 🔷 CNN – Tumor Type Detection
- **Input:** Grayscale MRI image (224×224)
- **Layers:** 3×(Conv2D + ReLU + Pooling) → Dense → Output (4 classes)
- **Framework:** PyTorch CNN
- **Training:** From scratch on MRI image dataset  

### 🟢 ANN – Glioma Stage Classification
- **Input:** Numeric mutation data (9 features)
- **Layers:** Dense → Dense → Dense → Output (4 stages)
- **Framework:** PyTorch MLP  
- **Training:** Tailored to mutation-feature input

---

## 💾 Model Files

| File                        | Description                              | Storage Location             |
|-----------------------------|------------------------------------------|------------------------------|
| `BTD_model.pth`            | Brain Tumor Classification Model         | **Download via Google Drive** |
| `glioma_stages.pth`       | Glioma Stage Classification Model        | Included in `models/` folder |

> 🚧 **Note:** `BTD_model.pth` exceeds GitHub’s 100MB limit and must be downloaded separately.

### 🔄 Auto-Download Script

Included in `app.py`, models are auto-fetched at first launch:
```python
# inside load_models()
gdown.download(BTD_MODEL_URL, "models/BTD_model.pth", quiet=True)
````

---

## ⚙️ Tech Stack

* **Language:** Python 3.10+
* **Frameworks:** PyTorch, Streamlit
* **Utils:** torchvision, pillow, gdown
* **Deployment:** Streamlit Community Cloud, Google Drive

---

## 📁 Folder Structure

```
NeuroAssistAiModel/
├── app.py               # Streamlit UI + model loading logic
├── models/              # Contains models and architecture definition
│   └── TumorModel.py    # CNN + ANN definitions
├── requirements.txt     # Project dependencies
├── .gitignore
├── images/              # Screenshots, banner, diagrams
└── README.md            # This documentation
```

---

## 🚀 Run Locally

1. **Clone Repo**

   ```bash
   git clone https://github.com/S4lmankhan/NeuroAssistAiModel.git
   cd NeuroAssistAiModel
   ```

2. **Virtual Environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Start App**

   ```bash
   streamlit run app.py
   ```

---

## 🔗 Embed in Your Site

Add this to your webpage:

```html
<iframe
  src="https://s4lmankhan-neuroassistaimodel.streamlit.app"
  width="100%" height="800" frameborder="0"
  aria-label="Brain Tumor Detector & Glioma Stage Predictor">
</iframe>
```

---

## ✨ Key Features

✅ Tumor classification from MRI images
✅ Glioma stage prediction from genetic data
✅ Fully interactive Streamlit UI
✅ Auto-downloading of large model files
✅ Clean, modular, and extendable architecture

---

## 🔭 Future Enhancements

* ✅ Hugging Face integration for model hosting
* ⚙️ Backend APIs using FastAPI + Docker
* 📊 Analytics dashboard for diagnostic insights
* 📱 Mobile-friendly frontend
* 🤖 Chatbot interaction using GPT

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add YourFeature"`
4. Push to branch: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📝 License

Licensed under the **MIT License** – see `LICENSE` for details.

---

## ✉️ Contact

**Salman Khan** • [@s4lmankhan](https://github.com/S4lmankhan)
📧 [redhawk112233@gmail.com](mailto:redhawk112233@gmail.com)

---

*Disclaimer: For research and educational use only—not intended for clinical diagnosis.*

```

---

### ✅ How to Use

1. **Create** a folder `images/` in your repository.
2. **Add** your own banner screenshot, demo screenshot, and banners there.
3. **Save** the above markdown as `README.md`.
4. **Commit and push** to GitHub.

This style carries your friend’s clean layout, clear sections, and rich content—while spotlighting **your Streamlit version** and maintaining your codebase intact.
::contentReference[oaicite:0]{index=0}
```
