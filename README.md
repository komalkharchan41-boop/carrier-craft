# ⚡ CareerCraft Pro: Cognitive Career & Academic Trajectory Agent

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![Frontend](https://img.shields.io/badge/Frontend-Glassmorphism%20UI-indigo.svg)]()
[![Charts](https://img.shields.io/badge/Visualization-Chart.js-coral.svg)](https://www.chartjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

> An autonomous, interactive AI counseling engine that maps student competencies, subject affinities, and problem-solving styles to precise academic degrees, vocational diplomas, verified online certifications, and milestone roadmaps.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Inference & Decision Logic](#-inference--decision-logic)
- [Tech Stack](#-tech-stack)
- [Project Directory Structure](#-project-directory-structure)
- [Getting Started](#-getting-started)
- [Usage Workflow](#-usage-workflow)
- [Future Scope](#-future-scope)
- [Author](#-author)

---

## 🚀 Overview

Students transitioning from high school or early undergraduate semesters often face a major hurdle: **navigating between 3–4 year college degrees, 6–12 month fast-track diplomas, and self-paced certification courses**.

**CareerCraft Pro** replaces static quizzes and generic articles with an adaptive dialogue-driven agent. The engine dynamically branches inquiries based on user background (e.g., routing Life Science/Chemistry students into Bioinformatics & Molecular Modeling, or Math/CS students into AI & Full-Stack tracks), displaying interactive multi-axis competency radars, compensation data, and downloadable execution blueprints.

---

## ✨ Key Features

* **Dynamic Dialogue State Machine**: Adapts questions based on domain input instead of forcing uniform, hardcoded questionnaires.
* **Tri-Tier Academic Pathways**: Categorizes output into:
  * 🎓 **Degree Programs**: Full-time university tracks (e.g., B.Tech, B.Sc, BCA, M.Sc) with eligibility criteria.
  * 📜 **Vocational Diplomas**: 6–12 month industry-focused technical diplomas.
  * ⚡ **Industry Certifications**: Verified courses from platforms like Coursera, NPTEL/Swayam, and edX.
* **Interactive Spider / Radar Telemetry**: Uses Chart.js with elastic easing animations to map mathematical, programmatic, analytical, and research skill balances.
* **Market Compensation Indicators**: Outlines realistic salary brackets across Entry-Level/Intern, Mid-Level, and Lead/Architect tiers.
* **Fluid Glassmorphism UI & Motion Feedback**: Features radial gradient mesh backgrounds, interactive card click ripples, and smooth page transition animations.
* **Client-Side Blueprint Export**: Built-in support to save and print personalized roadmaps as PDFs.

---

## 🏗️ System Architecture

```text
               +-------------------------------------------------+
               |              Client Browser (UI)                |
               |  (Glassmorphic Workspace, Chart.js, CSS Motion) |
               +-------------------------------------------------+
                                      |
                           HTTP POST  |  JSON Payload
                           (/chat)    |  { message: "..." }
                                      v
               +-------------------------------------------------+
               |                 Flask Backend                   |
               |        (Session-Backed State Machine)           |
               +-------------------------------------------------+
                                      |
                    +-----------------+-----------------+
                    |                                   |
                    v                                   v
+------------------------------------+ +----------------------------------+
|   Domain & Intent Classifier       | |   Inference Engine               |
|   - Multi-disciplinary routing     | |   - Matches Skills + Interests   |
|   - Contextual question dispatch   | |   - Evaluates Coding Comfort     |
|   - Keyword normalization          | |   - Generates Weighted Vectors   |
+------------------------------------+ +----------------------------------+
                    |                                   |
                    +-----------------+-----------------+
                                      |
                                      v
               +-------------------------------------------------+
               |          Structured Knowledge Base              |
               |  - Degree & Diploma Matrices                    |
               |  - NPTEL / Coursera Certification Data          |
               |  - Compensation Tiers & Roadmap Milestones      |
               +-------------------------------------------------+
                                      |
                                      v
               +-------------------------------------------------+
               |             Synthesized Response                |
               |   (JSON Payload -> Interactive DOM Card Render) |
               +-------------------------------------------------+
