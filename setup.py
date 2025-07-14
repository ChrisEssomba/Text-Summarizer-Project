import setuptools

#Add to the library a long description initially written in the readme file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
#define the version
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "ChrisEssomba"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "chris.essomba357@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME, 
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP text summarization", 
    long_description=long_description, 
    long_description_content="text/markdown", 
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", 
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    }, 
    package_dir={"": "src"}, 
    packages=setuptools.find_packages(where="src")
)