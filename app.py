import json

import streamlit as st

from PIL import Image
from enum import Enum
from typing import Dict
from pathlib import Path


class Page(Enum):
    PAGE_TITLE: str = "Portfolio | Matheus Tosetto"
    PAGE_ICON: str = ":wave:"
    NAME: str = "Matheus Tosetto"
    DESCRIPTION: str = "Data Engineer @AXA Ireland"
    SKILLS: str = "Python | Azure | MLOps"
    EMAIL: str = "22848645+mathTosetto@users.noreply.github.com"
    SOCIAL_MEDIA: Dict[str, str] = {
        "LinkedIn": "https://www.linkedin.com/in/matheus-brizolla/",
        "Github": "https://github.com/mathTosetto",
    }


class Paths(Enum):
    CSS_PATH: Path = Path("src/streamlit_app/assets/css/style.css")
    IMAGES_PATH: Path = Path("src/streamlit_app/assets/images")
    DOCS: Path = Path("src/streamlit_app/assets/docs")
    COUNTER_PATH: Path = Path("data")


class Links(Enum):
    MEDIUM_LINKS: Dict[str, str] = {
        "Spark Series": "https://medium.com/@matbrizolla/list/spark-series-325f7a670644",
        "Code Lists": "https://medium.com/@matbrizolla/list/code-3fc1b5e6935b",
        "DP-203 Study Series": "https://medium.com/@matbrizolla/list/dp203-study-series-f3b29e7b6634",
        "SQL Fundamentals": "https://medium.com/@matbrizolla/list/sql-fundamentals-7b93444f2559",
    }
    GITHUB_LINKS: Dict[str, str] = {
        "Great Expectations Project": "https://github.com/mathTosetto/data-quality-great-expectations",
        "Enhanced Logs": "https://github.com/mathTosetto/logging_example",
        "Web Scraping": "https://github.com/mathTosetto/product_catalog_scraper",
        "Uv Performance": "https://github.com/mathTosetto/uv_performance",
        "Cookiecutter Streamlit": "https://github.com/mathTosetto/cookiecutter_streamlit",
        "Cookiecutter Python": "https://github.com/mathTosetto/cookiecutter_generic_project",
        "Var Declaration Performance": "https://github.com/mathTosetto/var_declaration_performance",
        "Mutable Default Argument": "https://github.com/mathTosetto/mutable_default_argument",
    }


def horizontal_line():
    st.markdown(
        """<hr style="margin-top: 0rem; margin-bottom: 0.5rem;">""",
        unsafe_allow_html=True,
    )


st.set_page_config(
    page_title=Page.PAGE_TITLE.value,
    page_icon=Page.PAGE_ICON.value,
    layout="centered",
    initial_sidebar_state="auto",
)

counter_file: Path = Paths.COUNTER_PATH.value / "viewers_counter.txt"
if not counter_file.exists():
    counter_file.write_text("0")

count: int = int(counter_file.read_text())
count += 1
counter_file.write_text(str(count))

with open(Paths.CSS_PATH.value) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    profile_pic: Image = Image.open(
        Path(Paths.IMAGES_PATH.value / "photo-profile.jpeg")
    )
    st.image(profile_pic, width=320)

with col2:
    st.title(Page.NAME.value)
    st.write(Page.DESCRIPTION.value)
    st.write(Page.SKILLS.value)
    st.markdown(
        f"""
    <div style="margin-bottom: 15px;">
        <img src="https://img.shields.io/badge/👁️_Views-{count}-blue?style=flat-square" alt="View Counter">
    </div>
    """,
        unsafe_allow_html=True,
    )
    horizontal_line()

    st.markdown("### 🗣️ Get in touch")
    st.write("\n")
    st.markdown(
        f"""
        <div class="social-icons">
            <a href={Page.SOCIAL_MEDIA.value["LinkedIn"]} target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&style=for-the-badge" alt="LinkedIn">
            </a>
            <a href={Page.SOCIAL_MEDIA.value["Github"]} target="_blank">
                <img src="https://img.shields.io/badge/GitHub-black?logo=github&style=for-the-badge" alt="GitHub">
            </a>
            <a href={Page.EMAIL.value} target="_blank">
                <img src="https://img.shields.io/badge/Email-red?logo=gmail&style=for-the-badge" alt="Email">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with open(Path(Paths.DOCS.value / "curriculum-vitae.pdf"), "rb") as file:
        st.download_button(
            label="📄 Curriculum Vitae",
            data=file,
            file_name="Curriculum Vitae - Matheus Tosetto.pdf",
            mime="application/pdf",
        )

st.subheader("📦 Projects")
horizontal_line()

with st.expander("Data quality with Great Expectations"):
    st.write(
        "Cool project to use Great Expectations. The idea is to create a data quality pipeline to validate the data from the WAP (Write-Audit-Publish) architecture."
    )
    st.write(f"[Project]({Links.GITHUB_LINKS.value['Great Expectations Project']})")
    st.image(Image.open(Paths.IMAGES_PATH.value / "wap_architecture.png"))
    st.write("Tools: Python, Docker, Unit Tests, Airflow, SQL")

with st.expander("Enhanced Logs"):
    st.write(
        "Project to create a robust logging system for any projects. The logger is configured to output logs in both plain text (for stderr) and JSON (to a file)."
    )
    st.write(f"[Project]({Links.GITHUB_LINKS.value['Enhanced Logs']})")
    data: Dict[str, str | int] = {
        "level": "ERROR",
        "message": "Error message",
        "timestamp": "2023-12-23T15:45:01+00:00",
        "logger": "my_app",
        "module": "main",
        "function": "main",
        "line": 35,
        "thread_name": "MainThread",
        "exc_info": 'Traceback (most recent call last):\n  File "main.py", line 28, in main\n    1 / 0\nZeroDivisionError: division by zero\n',
    }
    st.code(json.dumps(data, indent=2), language="json")
    st.write("Tools: Python, Unit Tests")

with st.expander("Web scraping"):
    st.write("Web scraping project to extract product data from a supermarket website.")
    st.write(f"[Project]({Links.GITHUB_LINKS.value['Web Scraping']})")
    st.image(Image.open(Paths.IMAGES_PATH.value / "web_scraper.png"), width=280)
    st.write("Tools: Python, BeautifulSoup")

st.subheader("📘 Python Projects that teach by doing")
horizontal_line()

with st.expander("DevOps enhancement - UV library"):
    st.write(
        "Project to prove that using UV can help decrease pipeline deployment time."
    )
    st.write(f"[Project]({Links.GITHUB_LINKS.value['Uv Performance']})")
    st.image(Image.open(Paths.IMAGES_PATH.value / "uv_project.png"))
    st.write("Tools: Python, Unit Tests, DevOps")

with st.expander("Streamlining daily workflows with Cookiecutter"):
    st.write(
        "This is a Streamlit app starter template built with Cookiecutter. Perfect for quickly spinning up clean and organized projects."
    )
    st.write(
        f"[Streamlit Cookiecutter]({Links.GITHUB_LINKS.value['Cookiecutter Streamlit']})"
    )
    st.write(
        f"[Python Cookiecutter]({Links.GITHUB_LINKS.value['Cookiecutter Python']})"
    )
    st.image(Image.open(Paths.IMAGES_PATH.value / "cookiecutter.png"), width=280)
    st.write("Tools: Python")

with st.expander("Variable declaration performance test"):
    st.write(
        "This project contains a Python script that measures the time it takes to declare variables for different data types using their respective constructors and literal syntax."
    )
    st.write(f"[Project]({Links.GITHUB_LINKS.value['Var Declaration Performance']})")

    results: str = """
    Int results:
    Function declaration: 0.01401954 seconds.
    Literal declaration: 0.00408096 seconds.
    Declaring Int using literals is faster by 70.89%.
    """
    st.code(results, language="python")
    st.write("Tools: Python")

with st.expander("Mutable default arguments"):
    st.write(
        "This repository demonstrates the concept of mutable default arguments in Python."
    )
    st.write(f"[Project]({Links.GITHUB_LINKS.value['Mutable Default Argument']})")

    results: str = """
    from typing import List

    def add_to_list_mutable_default(item: str, list_items: List[str] = []) -> List[str]:
        list_items.append(item)
        return list_items

    print("Mutable Default Argument")
    print(add_to_list_mutable_default("banana"))  # ['banana']
    print(add_to_list_mutable_default("apple"))  # ['banana', 'apple']
    print("-" * 40)
    """
    st.code(results, language="python")
    st.write("Tools: Python")

st.subheader("✨ Medium Articles")
horizontal_line()

for key, value in Links.MEDIUM_LINKS.value.items():
    st.write(f"[{key}]({value})")
