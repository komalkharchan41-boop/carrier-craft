⚡ CareerCraft Pro: Cognitive Career & Academic Trajectory AgentAn autonomous, interactive AI counseling engine that maps student competencies, subject affinities, and problem-solving styles to precise academic degrees, vocational diplomas, verified online certifications, and milestone roadmaps.📌 Table of ContentsOverviewKey FeaturesSystem ArchitectureInference & Decision LogicTech StackProject Directory StructureGetting StartedUsage WorkflowFuture ScopeAuthor🚀 OverviewStudents transitioning from high school or early undergraduate semesters often face a major hurdle: navigating between 3–4 year college degrees, 6–12 month fast-track diplomas, and self-paced certification courses.CareerCraft Pro replaces static quizzes and generic articles with an adaptive dialogue-driven agent. The engine dynamically branches inquiries based on user background (e.g., routing Life Science/Chemistry students into Bioinformatics & Molecular Modeling, or Math/CS students into AI & Full-Stack tracks), displaying interactive multi-axis competency radars, compensation data, and downloadable execution blueprints.✨ Key FeaturesDynamic Dialogue State Machine: Adapts questions based on domain input instead of forcing uniform, hardcoded questionnaires.Tri-Tier Academic Pathways: Categorizes output into:🎓 Degree Programs: Full-time university tracks (e.g., B.Tech, B.Sc, BCA, M.Sc) with eligibility criteria.📜 Vocational Diplomas: 6–12 month industry-focused technical diplomas.⚡ Industry Certifications: Verified courses from platforms like Coursera, NPTEL/Swayam, and edX.Interactive Spider / Radar Telemetry: Uses Chart.js with elastic easing animations to map mathematical, programmatic, analytical, and research skill balances.Market Compensation Indicators: Outlines realistic salary brackets across Entry-Level/Intern, Mid-Level, and Lead/Architect tiers.Fluid Glassmorphism UI & Motion Feedback: Features radial gradient mesh backgrounds, interactive card click ripples, and smooth page transition animations.Client-Side Blueprint Export: Built-in support to save and print personalized roadmaps as PDFs.🏗️ System ArchitecturePlaintext               +-------------------------------------------------+
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
🧠 Inference & Decision LogicThe recommendation engine models multi-factor alignment:$$\text{Vector Composite} = f(\text{Skill Background}, \text{Domain Interest}, \text{Coding Comfort})$$Domain Extraction: Identifies technical clusters (e.g., Chemistry, Biology, Networks, Web, Data/Math).Path Mapping:Chemistry Background + Drug Discovery $\longrightarrow$ Computational Chemist & Molecular ModelerBiology/Genetics + Health Data $\longrightarrow$ Bioinformatics & Genomic AnalystMath/Logic + Predictive Systems $\longrightarrow$ AI & Data Science SpecialistCreative Design + Low-Code Comfort $\longrightarrow$ UI/UX & Digital Product SpecialistComputer Architecture + Web $\longrightarrow$ Full-Stack Software ArchitectNetworks + Defensive Investigation $\longrightarrow$ Cybersecurity SpecialistCurriculum Synthesis: Pulls specific degree levels (UG/PG), short-term diplomas, and NPTEL/Coursera certifications aligned with that cluster.🛠️ Tech StackBackend: Python 3, Flask (Session-based multi-turn dialog system)Frontend: HTML5, Modern CSS3 (Glassmorphism, CSS Grid, Flexbox, Keyframe animations)Visualization: Chart.js (Interactive multi-axis radar charts)Typography: Outfit via Google FontsDeployment Compatibility: WSGI servers (Gunicorn, Waitress), Docker-ready📁 Project Directory StructurePlaintextCareerCraft-AI/
│
├── app.py                     # Flask application, routing, inference engine & knowledge base
│
├── templates/
│   └── index.html             # Responsive chat interface, styles, motions & Chart.js logic
│
├── static/                    # Custom stylesheets, scripts, and asset icons
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── requirements.txt           # Python dependency manifest
└── README.md                  # Project documentation
⚡ Getting StartedPrerequisitesPython 3.8 to 3.12 installed on your system.pip package manager.InstallationClone the repository:Bashgit clone https://github.com/your-username/CareerCraft-AI.git
cd CareerCraft-AI
Create and activate a virtual environment (recommended):Bash# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
Install dependencies:Bashpip install flask
Launch the application:Bashpython app.py
Open the interface:Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.🚦 Usage WorkflowInitiation: The agent greets the user with dynamic option chips covering core sciences, mathematics, computer science, and beginner paths.Context Discovery: The user selects or inputs their academic background (e.g., Chemistry, Pharma & Science).Adaptive Querying: The bot adjusts step 2 to show field-specific interest vectors (e.g., Drug Discovery, Chemical Simulations) instead of generic programming questions.Parameter Balancing: Captures coding comfort level (ranging from no-code / pure science to daily programming).Blueprint Generation: The final dashboard renders:Radar Graph: Visual balance of mathematical, research, coding, and analytical skills.Degree Options: Recommended 3–4 year university programs and entrance pathways.Diploma Options: 6–12 month targeted technical diplomas.Online Certifications: MOOCs from NPTEL, Coursera, and edX.PDF Export: Instant download/print for personal records.🔮 Future ScopeLLM Hybrid Mode: Integrating lightweight LLM APIs (e.g., Google Gemini or OpenAI) to handle freeform student queries alongside deterministic rule-based pathways.Resume / Transcript Parsing: Allowing students to upload marksheets or resumes in PDF format to automatically extract skill tags.Entrance Exam & Cutoff Directory: Incorporating eligibility cutoffs for state and national examinations (e.g., JEE, GATE, NEET, CUET).Live Job Board Telemetry: Connecting job board APIs to display real-time hiring trends for recommended tracks.
