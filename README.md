# STT-AI
I am enrolled in this course at IITgn. I am sharing my solved labs and assignments here.

## Course Overview

This course teaches the **complete software engineering stack for AI/ML development**—from collecting and labeling data to deploying and monitoring models in production. While most ML courses focus on algorithms, this course focuses on the **engineering practices** that make ML systems work in the real world.

---

## What I'll Learn

By the end of this course, I will be able to:

| Module | Skills |
|--------|--------|
| **Data Engineering** | Collect data via APIs/scraping, validate with schemas, set up annotation pipelines, measure labeling quality |
| **Labeling at Scale** | Use active learning, weak supervision, and LLMs to reduce labeling costs by 50-80% |
| **Model Development** | Train models with scikit-learn/PyTorch, use AutoML, fine-tune LLMs with LoRA |
| **LLM Integration** | Call LLM APIs, engineer prompts, build multimodal applications |
| **MLOps** | Containerize with Docker, version data with DVC, track experiments with MLflow |
| **Deployment** | Build APIs with FastAPI, create demos with Streamlit/Gradio, set up CI/CD |
| **Production** | Optimize models for edge devices, profile performance, monitor for drift |

---

## Course Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        CS 203: 15-Week Journey                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PART I: DATA ENGINEERING (Weeks 1-5)                                   │
│  ├── Week 1: Data Collection (APIs, Scraping)                           │
│  ├── Week 2: Data Validation (Schemas, Quality)                         │
│  ├── Week 3: Data Labeling (Annotation, IAA)                            │
│  ├── Week 4: Optimizing Labeling (Active Learning, Weak Supervision)    │
│  └── Week 5: Data Augmentation (Image, Text, Audio)                     │
│                                                                         │
│  PART II: MODEL DEVELOPMENT (Weeks 6-11)                                │
│  ├── Week 6: LLM APIs (Gemini, Prompt Engineering)                      │
│  ├── Week 7: Model Training (AutoML, Fine-tuning)                       │
│  ├── Week 8: Reproducibility (Docker, DVC, MLflow)                      │
│  ├── Week 9: Interactive Demos (Streamlit, Gradio)                      │
│  ├── Week 10: ML APIs (FastAPI, REST)                                   │
│  └── Week 11: CI/CD (GitHub Actions, Testing)                           │
│                                                                         │
│  PART III: PRODUCTION (Weeks 12-15)                                     │
│  ├── Week 12: Edge Deployment (ONNX, Quantization)                      │
│  ├── Week 13: Profiling & Optimization (AMP, Distillation)              │
│  ├── Week 14: Monitoring (Drift Detection, Alerts)                      │
│  └── Week 15: Course Summary & Future Trends                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```
## Weekly Topics & Tools

| Week | Topic | Key Tools | Lab | Lab Solution |
|:----:|-------|-----------|:---:|:------------:|
| 1 | Data Collection | curl, requests, BeautifulSoup | [PDF](pdf/week01-data-collection-lab.pdf) | [PDF](pdf/week01-data-collection-solution.pdf) |
| 2 | Data Validation | jq, Pydantic, pandas | [PDF](pdf/week02-data-validation-lab.pdf) | [PDF](pdf/week02-data-validation-solution.pdf) |
| 3 | Data Labeling | Label Studio, Cohen's Kappa | [PDF](pdf/week03-data-labeling-lab.pdf) | [PDF](pdf/week03-data-labeling-solution.pdf) |
| 4 | Optimizing Labeling | modAL, Snorkel, cleanlab | [PDF](pdf/week04-active-learning-lab.pdf) | [PDF](pdf/week04-active-learning-solution.pdf) |
| 5 | Data Augmentation | Albumentations, nlpaug | [PDF](pdf/week05-data-augmentation-lab.pdf) | [PDF](pdf/week05-data-augmentation-solution.pdf) |
| 6 | LLM APIs | Gemini API, OpenAI | [PDF](pdf/week06-llm-apis-lab.pdf) | [PDF](pdf/week06-llm-apis-solution.pdf) |
| 7 | Model Development | scikit-learn, AutoGluon | [PDF](pdf/week07-model-development-lab.pdf) | [PDF](pdf/week07-model-development-solution.pdf) |
| 8 | Reproducibility | Docker, DVC, MLflow | [PDF](pdf/week08-reproducibility-lab.pdf) | [PDF](pdf/week08-reproducibility-solution.pdf) |
| 9 | Interactive Demos | Streamlit, Gradio | [PDF](pdf/week09-interactive-demos-lab.pdf) | [PDF](pdf/week09-interactive-demos-solution.pdf) |
| 10 | HTTP & APIs | FastAPI, Pydantic | [PDF](pdf/week10-http-apis-lab.pdf) | [PDF](pdf/week10-http-apis-solution.pdf) |
| 11 | Git & CI/CD | GitHub Actions, pytest | [PDF](pdf/week11-git-cicd-lab.pdf) | [PDF](pdf/week11-git-cicd-solution.pdf) |
| 12 | Edge Deployment | ONNX, Quantization | [PDF](pdf/week12-deployment-constrained-lab.pdf) | [PDF](pdf/week12-deployment-constrained-solution.pdf) |
| 13 | Profiling | PyTorch Profiler, AMP | [PDF](pdf/week13-profiling-optimization-lab.pdf) | [PDF](pdf/week13-profiling-optimization-solution.pdf) |
| 14 | Monitoring | Evidently AI, Drift | [PDF](pdf/week14-model-monitoring-lab.pdf) | [PDF](pdf/week14-model-monitoring-solution.pdf) |
| 15 | Summary | — | — | — |
---
| Assignment | Topic | Key Tools | Assignment | Assignment Solution |
|:----------:|-------|-----------|:----------:|:------------------:|
| 1 | Data Collection | curl, requests, BeautifulSoup | [PDF](pdf/week01-data-collection-lab.pdf) | [PDF](pdf/week01-data-collection-solution.pdf) |
| 2 | Data Validation | jq, Pydantic, pandas | [PDF](pdf/week02-data-validation-lab.pdf) | [PDF](pdf/week02-data-validation-solution.pdf) |
| 3 | Data Labeling | Label Studio, Cohen's Kappa | [PDF](pdf/week03-data-labeling-lab.pdf) | [PDF](pdf/week03-data-labeling-solution.pdf) |
| 4 | Optimizing Labeling | modAL, Snorkel, cleanlab | [PDF](pdf/week04-active-learning-lab.pdf) | [PDF](pdf/week04-active-learning-solution.pdf) |
| 5 | Data Augmentation | Albumentations, nlpaug | [PDF](pdf/week05-data-augmentation-lab.pdf) | [PDF](pdf/week05-data-augmentation-solution.pdf) |
| 6 | LLM APIs | Gemini API, OpenAI | [PDF](pdf/week06-llm-apis-lab.pdf) | [PDF](pdf/week06-llm-apis-solution.pdf) |
| 7 | Model Development | scikit-learn, AutoGluon | [PDF](pdf/week07-model-development-lab.pdf) | [PDF](pdf/week07-model-development-solution.pdf) |
| 8 | Reproducibility | Docker, DVC, MLflow | [PDF](pdf/week08-reproducibility-lab.pdf) | [PDF](pdf/week08-reproducibility-solution.pdf) |
| 9 | Interactive Demos | Streamlit, Gradio | [PDF](pdf/week09-interactive-demos-lab.pdf) | [PDF](pdf/week09-interactive-demos-solution.pdf) |
| 10 | HTTP & APIs | FastAPI, Pydantic | [PDF](pdf/week10-http-apis-lab.pdf) | [PDF](pdf/week10-http-apis-solution.pdf) |
| 11 | Git & CI/CD | GitHub Actions, pytest | [PDF](pdf/week11-git-cicd-lab.pdf) | [PDF](pdf/week11-git-cicd-solution.pdf) |
| 12 | Edge Deployment | ONNX, Quantization | [PDF](pdf/week12-deployment-constrained-lab.pdf) | [PDF](pdf/week12-deployment-constrained-solution.pdf) |
| 13 | Profiling | PyTorch Profiler, AMP | [PDF](pdf/week13-profiling-optimization-lab.pdf) | [PDF](pdf/week13-profiling-optimization-solution.pdf) |
| 14 | Monitoring | Evidently AI, Drift | [PDF](pdf/week14-model-monitoring-lab.pdf) | [PDF](pdf/week14-model-monitoring-solution.pdf) |
| 15 | Summary | — | — | — |
