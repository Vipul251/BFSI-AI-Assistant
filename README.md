<img width="1457" height="539" alt="image" src="https://github.com/user-attachments/assets/11d40390-68b8-4d64-9a40-3b8d89416068" /># BFSI-AI-Assistant
# 🏦 BFSI Call Center AI Assistant

A lightweight, compliant, and fully local GenAI assistant designed to handle common Banking, Financial Services, and Insurance (BFSI) customer queries with high accuracy and safety.

Built with **Python, Streamlit, Ollama, and TinyLlama (LoRA fine-tuned)**.

---

## 🚀 Project Overview

Call centers in BFSI face three major challenges:

* High volume of repetitive queries
* Need for regulatory-compliant responses
* Requirement for low-latency local solutions

This project solves the problem using a **multi‑tier intelligent pipeline** that prioritizes deterministic answers before using generation.

### 🎯 Supported Query Types

* Loan eligibility & application status
* EMI details & schedules
* Interest rate information
* Payment & transaction queries
* Basic account support

---

## 🧠 System Architecture

```
User Query
   ↓
Similarity Search (Alpaca Dataset)
   ↓ (if weak match)
Fine‑Tuned TinyLlama (Local SLM)
   ↓ (if complex)
RAG Knowledge Retrieval
   ↓
Guardrails & Compliance Filter
   ↓
Final Response
```

### ✅ Response Priority

1. **Tier 1 — Dataset Match (Highest Priority)**
2. **Tier 2 — Fine‑Tuned SLM**
3. **Tier 3 — RAG Retrieval**

This ensures **safety first, generation second**.

---

## 🧩 Tech Stack

| Layer        | Technology            |
| ------------ | --------------------- |
| UI           | Streamlit             |
| Backend      | Python                |
| Local LLM    | Ollama (TinyLlama)    |
| Fine‑Tuning  | PEFT LoRA             |
| Similarity   | Sentence Transformers |
| Vector Store | FAISS                 |
| Retrieval    | Custom RAG Pipeline   |
| Safety       | Rule‑based Guardrails |

---
<img width="1457" height="539" alt="image" src="https://github.com/user-attachments/assets/6b713b1d-697c-4285-9e39-6a32baf3bc11" />

## 📁 Project Structure

```
bfsi-assistant/
│
├── data/
│   └── alpaca_bfsi.json        # BFSI conversation dataset
│
├── src/
│   ├── guardrails.py           # Safety & compliance checks
│   ├── ollama_client.py        # Local LLM interface
│   ├── rag_pipeline.py         # Knowledge retrieval logic
│   └── similarity.py           # Dataset similarity matching
│
├── app.py                      # Streamlit UI entry point
├── requirements.txt            # Dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd bfsi-assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\\Scripts\\activate   # Windows
source venv/bin/activate    # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install & Start Ollama

Download Ollama and pull TinyLlama:

```bash
ollama pull tinyllama
ollama serve
```

✅ Verify:

```bash
ollama run tinyllama
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

Open browser → `http://localhost:8501`

---

## 🧪 Example Queries

Try these in the UI:

* "What is my loan application status?"
* "Explain EMI calculation"
* "Why was my payment declined?"
* "What is the current interest rate?"

---

## 🔒 Guardrails & Compliance

The system enforces strict BFSI safety rules:

* ❌ No guessing financial numbers
* ❌ No fake interest rates
* ❌ No exposure of sensitive data
* ❌ Rejects out‑of‑domain queries
* ✅ Professional banking tone

Implemented in: `src/guardrails.py`

---

## 🧠 Fine‑Tuning Approach

Model: **TinyLlama‑1.1B‑Chat**

Method:

* Alpaca‑formatted BFSI dataset
* LoRA (PEFT) fine‑tuning
* Quantized local inference via Ollama

### Why LoRA?

* Low VRAM requirement
* Fast training
* Easy adapter loading
* Production friendly

---

## 📚 RAG Knowledge Base

Used for complex financial explanations such as:

* EMI breakdown
* Interest calculations
* Penalty rules
* Policy explanations

Flow:

```
Query → Embedding → FAISS Search → Context → LLM
```
---

## 📈 Scalability Considerations

* Modular pipeline design
* Version‑controlled dataset
* Swappable local models
* FAISS index persistence ready
* Streamlit can be containerized

---

## 🐳 (Optional) Future Improvements

* Docker deployment
* Redis caching
* Async request handling
* Multi‑language support
* Voice integration for call centers

---

## 👨‍💻 Author

**Vipul Bhatt**

## ⭐ If This Helped

Give the repo a star and use it in your portfolio or interviews 🚀
