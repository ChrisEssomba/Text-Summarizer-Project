# 📚 Text Summarization System

This project aims to develop a robust automated text summarization system using state-of-the-art machine learning techniques. The system is trained on a domain-specific dataset (Samsung-related texts) to generate concise and coherent summaries of longer documents. It includes a **training pipeline**, **data validation**, and a **FastAPI web application** for real-time inference and deployment.

---

## 🚀 Purpose

As the volume of textual data continues to grow, automatic summarization tools become increasingly important. This project provides a way to distill large bodies of information into essential summaries, helpful for improving productivity, gaining quick insights, or powering downstream NLP systems.

---

## 🚀 Key Features
- **State-of-the-Art Model**: Fine-tuned HuggingFace seq2seq transformer
- **Production API**: 
  - POST `/summarize` endpoint
  - Request rate limiting
  - Input validation
- **Data Validation**: Automated checks for:
  - Text quality
  - Summary consistency
  - Dataset balance
 
---

## 🛠️ Technologies Used
| Component           | Technologies                         |
|---------------------|--------------------------------------|
| **Model Training**  | Transformers, PyTorch                |
| **API**             | FastAPI, Uvicorn                     |
| **Data Processing** | Pandas, NLTK                         |
| **Deployment**      | Docker, GitHub Actions               |
| **Monitoring**      | Prometheus, Grafana (optional)       |

## 📊 Model Performance
- **ROUGE-1**: 0.45
- **ROUGE-2**: 0.30  
- **ROUGE-L**: 0.40
- **Inference Speed**: ~500ms (on CPU)

---

## 🧱 Project Structure

```
├── .github/workflows/         # CI/CD pipelines
├── config/                    # Configuration files
│   └── params.yaml            # Model/training parameters
├── research/                  # Experimental notebooks
├── src/textSummarizer/       # Core Python package
│   ├── __init__.py
│   ├── data_validation.py     # Data quality checks
│   └── model_training.py      # Training pipeline
├── summarizer-data/           # Processed dataset
│   └── samsung_dataset/       # Raw/processed data
│
├── app.py                     # FastAPI application
├── main.py                    # CLI entry point
├── Dockerfile                 # Containerization
├── requirements.txt           # Production dependencies
├── setup.py                   # Package configuration
└── template.py                # API response templates
```

---

## 🧪 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer
   ```

2. **Set up the environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Or use `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

3. **Train the model**  
   ```bash
   python main.py train
   ```

4. **Launch the API**  
   ```bash
   uvicorn app:app --reload
   ```

5. **Docker (Optional)**  
   ```bash
   docker build -t text-summarizer .
   docker run -p 8000:8000 text-summarizer
   ```

---

## 📦 API Usage

Once the FastAPI server is running, visit:  
`http://localhost:8000/docs`  
You'll find an interactive Swagger UI to test endpoints.

---

## 📈 Future Improvements

- Add multilingual summarization support
- Integrate more domain-specific datasets
- Improve latency with model quantization
- Deploy via Kubernetes on Azure/GCP

---

## 🧑‍💻 Author

Chris Essomba – *Machine Learning Engineer & Data Enthusiast*

---

## 📄 License

MIT License — Free to use with attribution.
