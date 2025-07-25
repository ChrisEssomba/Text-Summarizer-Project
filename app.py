import streamlit as st
import os
import time
from datetime import datetime
from textSummarizer.pipeline.prediction import PredictionPipeline

# App configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load custom CSS (you'll need to create this file)
try:
    local_css("style.css")
except:
    pass  # Use default styling if custom CSS not found

# App header
st.title("✂️ AI Text Summarizer")
st.markdown("""
    <div style="border-bottom: 1px solid #eee; margin-bottom: 2rem;"></div>
""", unsafe_allow_html=True)

# Sidebar for additional options
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=Your+Logo", width=150)
    st.title("Settings")
    
    summary_length = st.slider(
        "Summary Length", 
        min_value=50, 
        max_value=300, 
        value=150,
        help="Adjust the length of the generated summary"
    )
    
    model_version = st.selectbox(
        "Model Version",
        ("Base", "Advanced", "Custom"),
        index=0,
        help="Select which model version to use"
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
        This AI-powered tool creates concise summaries of your text documents 
        using state-of-the-art natural language processing.
    """)

# Main content area
tab1, tab2 = st.tabs(["Summarize Text", "Train Model"])

with tab1:
    st.header("Text Summarization")
    st.markdown("Enter your text below and click the summarize button.")
    
    input_text = st.text_area(
        "Input Text",
        height=200,
        placeholder="Paste your text here...",
        help="The text you want to summarize"
    )
    
    col1, col2 = st.columns([1, 6])
    with col1:
        summarize_btn = st.button("Summarize", type="primary")
    with col2:
        clear_btn = st.button("Clear")
    
    if clear_btn:
        input_text = ""
        st.experimental_rerun()
    
    if summarize_btn and input_text:
        with st.spinner("Generating summary..."):
            start_time = time.time()
            
            try:
                # Call your prediction pipeline
                predictor = PredictionPipeline()
                summary = predictor.predict(input_text)
                
                processing_time = time.time() - start_time
                
                # Display results
                st.success("Summary generated successfully!")
                
                st.subheader("Original Text")
                st.text_area("Original", value=input_text, height=150, disabled=True)
                
                st.subheader("Generated Summary")
                st.text_area("Summary", value=summary, height=150, disabled=True)
                
                # Metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Original Length", f"{len(input_text.split())} words")
                with col2:
                    st.metric("Summary Length", f"{len(summary.split())} words")
                with col3:
                    st.metric("Processing Time", f"{processing_time:.2f} seconds")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

with tab2:
    st.header("Model Training")
    st.warning("This will retrain the model with new data. This may take some time.")
    
    if st.button("Start Training", type="secondary"):
        with st.spinner("Training in progress. Please wait..."):
            start_time = time.time()
            training_log = st.empty()
            
            try:
                # Redirect output to Streamlit
                with st_capture(training_log.code):
                    os.system("python main.py")
                
                training_time = time.time() - start_time
                st.success(f"Training completed successfully in {training_time:.2f} seconds!")
                
            except Exception as e:
                st.error(f"Training failed: {str(e)}")

# Helper function to capture command line output
import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def st_capture(output_func):
    with StringIO() as stdout, StringIO() as stderr:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        try:
            sys.stdout = stdout
            sys.stderr = stderr
            yield
            output_func(stdout.getvalue() + stderr.getvalue())
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <p>© 2023 AI Text Summarizer | <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
    </div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    # For development, you can run this directly with: streamlit run app.py
    pass