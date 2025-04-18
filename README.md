# 📁 Personal Portfolio

Welcome to my personal portfolio built with Streamlit
This app showcases my background, key projects, and helpful Python tools I've created to enhance productivity and DevOps workflows.

[Online profile](https://matheus-tosetto-portfolio.streamlit.app/)

---

## 🚀 About the Project

This is a fully responsive portfolio web app built with **Streamlit** and styled using **custom CSS**.

---

## 📌 Features

- ✨ Clean two-column layout for profile + intro
- 📷 Circular profile image (styled with CSS)
- 🛠️ Projects expandable in collapsible sections
- 📄 Downloadable CV with `st.download_button`
- 🔗 Social media and contact links with custom badges
- ⚙️ Modular design using `Enum` and `Pathlib` for configuration
- 🧪 Code snippets and project highlights shown using Markdown and `st.code()`

---

## 🧱 Tech Stack

- `Python`
- `Streamlit`
- `Pillow` for image handling
- `Enum`, `Pathlib`, and modern Python practices
- `Shields.io` for badge-style buttons

---

## 🧪 Running the App Locally

```bash
# 1. Install py-make
pip install py-make

# 2. Install dependencies
make

# 2. Activate the virtual environment
poetry env activate

# 3. Run the app
streamlit run app.py
