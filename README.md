<!-- Banner -->
<p align="center">
  <img src="images/banner.png" alt="NeuroAssistAI" width="800"/>
</p>

<h1 align="center">🔬 NeuroAssistAIModel</h1>
<p align="center">
  **Advanced Brain Tumor Detection & Glioma Stage Prediction**  
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License"/></a>
  <a href="https://streamlit.io/cloud"><img src="https://img.shields.io/badge/Live%20Demo-Streamlit-red.svg" alt="Streamlit Demo"/></a>
  <a href="https://github.com/S4lmankhan/NeuroAssistAiModel/actions"><img src="https://img.shields.io/github/actions/workflow/status/S4lmankhan/NeuroAssistAiModel/ci.yml?branch=main&label=CI&style=flat-square" alt="CI Status"/></a>
</p>

---

## 📖 Table of Contents
1. [🤔 Why NeuroAssistAI?](#🤔-why-neuroassistai)  
2. [🎨 Highlights](#🎨-highlights)  
3. [⚙️ Architecture](#⚙️-architecture)  
4. [💾 Installation](#💾-installation)  
5. [🚀 Quickstart](#🚀-quickstart)  
6. [📂 Download Models](#📂-download-models)  
7. [📦 Deployment](#📦-deployment)  
8. [🛠 Troubleshooting](#🛠-troubleshooting)  
9. [🤝 Contributing](#🤝-contributing)  
10. [📝 License](#📝-license)  

---

## 🤔 Why NeuroAssistAI?

- **Precision Diagnosis**: Leverages CNN and MLP architectures for accurate, automated brain tumor analysis.  
- **End‑to‑End Pipeline**: From MRI image upload to gene‑mutation form, all in one unified interface.  
- **Instant Deployment**: Models auto‑download from Google Drive; no large files in GitHub.  
- **Embeddable UI**: Integrate via `<iframe>` into any web portal (e.g. V0 Agent).

---

## 🎨 Highlights

<p align="center">
  <img src="images/demo_screenshot.png" alt="Demo Screenshot" width="80%"/>
</p>

- **Dual Tabs**: Separate workflows for **Tumor Detection** and **Glioma Staging**.  
- **Responsive Design**: Fits desktop & mobile.  
- **Graphical Feedback**: Sidebar logs missing/unexpected keys for quick debugging.

---

## ⚙️ Architecture

```mermaid
flowchart LR
  A[Upload MRI] --> B[Streamlit UI]
  B --> C[CNN Model: TumorClassification]
  C --> D[Tumor Type]
  E[Enter Genetic Info] --> B
  B --> F[MLP Model: GliomaStageModel]
  F --> G[Glioma Stage]
  D & G --> H[Results Display]
````

---

## 💾 Installation

1. **Clone**

   ```bash
   git clone https://github.com/S4lmankhan/NeuroAssistAiModel.git
   cd NeuroAssistAiModel
   ```
2. **Environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```
3. **Dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 🚀 Quickstart

```bash
streamlit run app.py
```

* **Tab 1**: Upload an MRI → Predict tumor type
* **Tab 2**: Fill mutation sliders → Predict glioma stage

---

## 📂 Download Models

Models are auto‑downloaded via `gdown`, but you can grab them manually:

| Model                                      | Link                                                                                                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TumorClassification** (`BTD_model.pth`)  | [https://drive.google.com/file/d/1juQk4AhIi7u7I41uttCUpJYsvtsPyZUy/view](https://drive.google.com/file/d/1juQk4AhIi7u7I41uttCUpJYsvtsPyZUy/view)  |
| **GliomaStageModel** (`glioma_stages.pth`) | [https://drive.google.com/file/d/19MrhHVQbSlVmaV-bP\_FIpcY5t9wjKMSX/view](https://drive.google.com/file/d/19MrhHVQbSlVmaV-bP_FIpcY5t9wjKMSX/view) |

Place these in a `models/` folder if you prefer offline use.

---

## 📦 Deployment

### Streamlit Community Cloud

1. Push to **GitHub** (`main` branch).
2. On [Streamlit Cloud](https://streamlit.io/cloud), click **New App**.
3. Select **NeuroAssistAiModel**, branch `main`, entry `app.py`.

> **Live Demo:**
> [https://s4lmankhan-neuroassistaiModel.streamlit.app](https://s4lmankhan-neuroassistaiModel.streamlit.app)

### Embedding via `<iframe>`

```html
<iframe
  src="https://s4lmankhan-neuroassistaiModel.streamlit.app"
  width="100%" height="800" frameborder="0" 
  aria-label="NeuroAssistAI App">
</iframe>
```

---

## 🛠 Troubleshooting

* **Load errors**? Check `models/TumorModel.py` matches checkpoint shapes.
* **Drive download fails**? Ensure links are public; test with:

  ```bash
  gdown "https://drive.google.com/uc?id=1juQk4AhIi7u7I41uttCUpJYsvtsPyZUy"
  ```
* **Iframe blocked**? Verify `X-Frame-Options`; fallback to redirect page.

---

## 🤝 Contributing

1. **Fork** it
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

---

## 📝 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ by **Salman Khan** — [@s4lmankhan](https://github.com/S4lmankhan)  
</p>
