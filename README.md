<p align="center">
  <img src="https://raw.githubusercontent.com/S4lmankhan/NeuroAssistAiModel/main/images/logo.png" alt="NeuroAssistAI Logo" width="200"/>
</p>

# NeuroAssistAI Model

**🧠 Brain Tumor Detection & Glioma Stage Prediction**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-blue?logo=streamlit)](https://s4lmankhan-neuroassistaiModel.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

---

## 📖 Project Overview

**NeuroAssistAI** is an end‑to‑end solution for non‑invasive brain tumor analysis:

* **Tumor Type Detection**: Classifies MRI scans into **glioma**, **meningioma**, **no tumor**, or **pituitary**.
* **Glioma Stage Prediction**: Estimates glioma progression stage (I–IV) based on genetic markers.

All wrapped in a sleek **Streamlit** interface and easily embeddable via `<iframe>` in any website.

---

## 🚀 Our Journey

1. **Data & Modeling**
   • Designed and trained two PyTorch models (CNN & MLP) on reputable MRI datasets.
   • Faced architecture mismatches when loading weights—solved by aligning input dimensions and model definitions.

2. **Deployment Challenges**
   • GitHub file‑size limits blocked large `.pth` files.
   • Explored Heroku, AWS, Hugging Face—ran into quotas or permission errors.
   • Settled on **Streamlit Community Cloud** + **Google Drive** for model hosting.

3. **Final Solution**
   • Models auto‑download at runtime via **gdown** from public Drive links.
   • Streamlit app with two tabs: image upload + form input.
   • Embeddable via `<iframe>` for seamless integration on any website (e.g. V0 Agent).

---

## 🎨 Showcase

<p align="center">
  <img src="https://raw.githubusercontent.com/S4lmankhan/NeuroAssistAiModel/main/images/demo_screenshot.png" alt="App Screenshot" width="800"/>
</p>

> **Live Demo:**
> [https://s4lmankhan-neuroassistaiModel.streamlit.app](https://s4lmankhan-neuroassistaiModel.streamlit.app)

---

## 🔧 Installation & Usage

1. **Clone the repo**

   ```bash
   git clone https://github.com/S4lmankhan/NeuroAssistAiModel.git
   cd NeuroAssistAiModel
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   .venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download pretrained models**
   Place them in `models/` or let the app auto‑download at first run:

   * **Tumor Detection Model**

     ```
     https://drive.google.com/file/d/1juQk4AhIi7u7I41uttCUpJYsvtsPyZUy/view
     ```
   * **Glioma Stage Model**

     ```
     https://drive.google.com/file/d/19MrhHVQbSlVmaV-bP_FIpcY5t9wjKMSX/view
     ```

5. **Run the app locally**

   ```bash
   streamlit run app.py
   ```

6. **Embed via `<iframe>`**

   ```html
   <iframe
     src="https://s4lmankhan-neuroassistaiModel.streamlit.app"
     width="100%" height="800" frameborder="0">
   </iframe>
   ```

---

## 🧩 Project Structure

```
NeuroAssistAiModel/
├── app.py                # Streamlit UI + model loader
├── models/
│   └── TumorModel.py     # PyTorch architectures
├── requirements.txt      # Python dependencies
├── .gitignore
└── images/               # Logo & screenshots
```

---

## ⚙️ API Version (Optional)

We also provide a **FastAPI** backend (`newapi.py`) if you prefer REST endpoints:

```bash
uvicorn newapi:app --host 0.0.0.0 --port 8000
```

* `POST /predict-image` → tumor type
* `POST /predict-glioma-stage` → stage prediction

---

## 🛠️ Troubleshooting & FAQ

1. **Model Download Fails**

   * Ensure `gdown` is installed.
   * Verify Drive link is public (“Anyone with link”).

2. **Architecture Mismatch**

   * Adjust `TumorModel.py` to match `(channels, height, width)` seen in error logs.
   * Use `strict=False` in `load_state_dict` during debugging.

3. **Iframe Not Displaying**

   * Confirm your site’s CSP allows `frame-src *`.
   * Test embedding in a simple HTML page first.

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📜 License

[MIT License](LICENSE) © Salman Khan

---

## 🙏 Acknowledgments

* Datasets: \[Your MRI dataset sources]
* Libraries: [PyTorch](https://pytorch.org/), [Streamlit](https://streamlit.io/), [gdown](https://github.com/wkentaro/gdown)

---

<p align="center">
  Made with ❤️ by **Salman Khan**  
  <br/>
  <a href="mailto:redhawk112233@gmail.com">Contact me</a>
</p>
::contentReference[oaicite:0]{index=0}
