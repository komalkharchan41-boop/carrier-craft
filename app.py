from flask import Flask, render_template, request, jsonify, session
import uuid

app = Flask(__name__)
app.secret_key = "careercraft-student-degrees-" + str(uuid.uuid4())

# ==========================================================
# 1. ACADEMIC & VOCATIONAL KNOWLEDGE BASE
# ==========================================================
CAREER_DATABASE = {
    "bioinformatics": {
        "title": "Bioinformatics & Genomic Data Analyst",
        "tagline": "Analyze DNA sequencing, genetics, and clinical datasets using biological science and statistical tools.",
        "icon": "🧬",
        "market_demand": "94% (High Demand in Healthcare & Biotech)",
        "salary_tiers": {"Junior": "₹6 - ₹11 LPA", "Mid": "₹13 - ₹22 LPA", "Lead": "₹28+ LPA"},
        "radar_profile": {"Biology": 95, "Genetics": 90, "Analytics": 85, "Research": 90, "Coding": 65},
        
        # EXACT ACADEMIC PATHWAYS FOR STUDENTS:
        "pathways": {
            "degrees": [
                {"name": "B.Tech / B.Sc in Biotechnology or Bioinformatics", "duration": "3 - 4 Years", "eligibility": "12th Science (PCB/PCMB)"},
                {"name": "M.Sc in Bioinformatics / Computational Biology", "duration": "2 Years", "eligibility": "Graduation in Life Sciences or CS"}
            ],
            "diplomas": [
                {"name": "PG Diploma in Bioinformatics & Cheminformatics", "duration": "1 Year", "eligibility": "Post-Graduation / Final Year BSc"},
                {"name": "Advanced Diploma in Clinical Data Management", "duration": "6 - 12 Months", "eligibility": "12th or Graduate in Science"}
            ],
            "certifications": [
                {"name": "Genomic Data Science Specialization (Johns Hopkins)", "platform": "Coursera", "duration": "3 Months"},
                {"name": "NPTEL Bioinformatics: Algorithms & Applications", "platform": "Swayam / IIT", "duration": "12 Weeks"},
                {"name": "BioPython & Molecular Alignment Practice", "platform": "edX", "duration": "6 Weeks"}
            ]
        },
        "roadmap": [
            {"phase": "Semester / Phase 1", "desc": "Cell Biology, Genetics & Statistical Foundations"},
            {"phase": "Semester / Phase 2", "desc": "Sequence Alignment Algorithms, FASTA/FASTQ Formats & BioPython"},
            {"phase": "Semester / Phase 3", "desc": "RNA-Seq differential analysis & Genomic Visualizations in R"},
            {"phase": "Semester / Phase 4", "desc": "Machine Learning for Disease Biomarkers & Capstone Research Project"}
        ]
    },
    "computational_chemistry": {
        "title": "Computational Chemist & Molecular Modeler",
        "tagline": "Apply chemical theory, molecular modeling, and simulation tools for modern drug synthesis and material science.",
        "icon": "🧪",
        "market_demand": "92% (High Growth in Pharma & R&D)",
        "salary_tiers": {"Junior": "₹6 - ₹10 LPA", "Mid": "₹12 - ₹20 LPA", "Lead": "₹26+ LPA"},
        "radar_profile": {"Chemistry": 95, "Research": 90, "Simulations": 85, "Coding": 60, "Analytics": 75},
        
        "pathways": {
            "degrees": [
                {"name": "B.Sc / B.Tech in Chemistry / Chemical Engineering", "duration": "3 - 4 Years", "eligibility": "12th Science (PCM/PCMB)"},
                {"name": "M.Sc in Computational / Medicinal Chemistry", "duration": "2 Years", "eligibility": "B.Sc Chemistry / B.Pharm"}
            ],
            "diplomas": [
                {"name": "PG Diploma in Cheminformatics & Drug Design", "duration": "1 Year", "eligibility": "B.Sc Chemistry / B.Pharm"},
                {"name": "Diploma in Analytical Chemistry & Instrumentation", "duration": "6 - 12 Months", "eligibility": "12th Science"}
            ],
            "certifications": [
                {"name": "Python for Chemistry (RDKit & Molecular Docking)", "platform": "Open Science / GitHub", "duration": "8 Weeks"},
                {"name": "NPTEL Computational Chemistry by IIT Madras", "platform": "Swayam / NPTEL", "duration": "12 Weeks"},
                {"name": "GROMACS Molecular Dynamics Essentials", "platform": "BioExcel", "duration": "4 Weeks"}
            ]
        },
        "roadmap": [
            {"phase": "Semester / Phase 1", "desc": "Thermodynamics, Organic Mechanisms & Quantum Chemistry Basics"},
            {"phase": "Semester / Phase 2", "desc": "Molecular Visualization (Avogadro, PyMOL) & Chemical DBs (PubChem)"},
            {"phase": "Semester / Phase 3", "desc": "Python for Cheminformatics (RDKit) and Molecular Docking (AutoDock)"},
            {"phase": "Semester / Phase 4", "desc": "Molecular Dynamics Simulation & Real Drug Target Capstone"}
        ]
    },
    "data_science_ai": {
        "title": "AI & Data Science Engineer",
        "tagline": "Extract predictive insights from massive data pools and deploy automated neural network architectures.",
        "icon": "🧠",
        "market_demand": "98% (Extremely High)",
        "salary_tiers": {"Junior": "₹8 - ₹12 LPA", "Mid": "₹16 - ₹26 LPA", "Lead": "₹32+ LPA"},
        "radar_profile": {"Math": 95, "Coding": 85, "Machine Learning": 90, "Analytics": 95, "System Design": 65},
        
        "pathways": {
            "degrees": [
                {"name": "B.Tech in CSE (AI & ML) or B.Sc in Data Science / BCA", "duration": "3 - 4 Years", "eligibility": "12th with Mathematics"},
                {"name": "M.Tech / M.Sc in Data Science or Artificial Intelligence", "duration": "2 Years", "eligibility": "Graduation in Engineering / Math / CS"}
            ],
            "diplomas": [
                {"name": "Post Graduate Diploma in Data Science (PGDDS)", "duration": "11 Months", "eligibility": "Graduation in any analytical stream"},
                {"name": "Diploma in Applied Artificial Intelligence", "duration": "6 Months", "eligibility": "Basic coding exposure"}
            ],
            "certifications": [
                {"name": "DeepLearning.AI: Machine Learning Specialization", "platform": "Coursera", "duration": "3 Months"},
                {"name": "Google Professional Data Analytics Certificate", "platform": "Coursera", "duration": "6 Months"},
                {"name": "NPTEL: Problem Solving through Programming / Python", "platform": "Swayam", "duration": "12 Weeks"}
            ]
        },
        "roadmap": [
            {"phase": "Semester / Phase 1", "desc": "Linear Algebra, Calculus, Python Syntax & Data Analysis (Pandas)"},
            {"phase": "Semester / Phase 2", "desc": "Data Cleaning, Scikit-Learn Classifiers & Feature Engineering"},
            {"phase": "Semester / Phase 3", "desc": "Deep Learning Models (CNNs, NLP, Hugging Face Transformers)"},
            {"phase": "Semester / Phase 4", "desc": "MLOps, Model Deployment via FastAPI & Production Streamlit Dashboards"}
        ]
    },
    "fullstack_dev": {
        "title": "Full-Stack Web & Software Architect",
        "tagline": "Build responsive websites, interactive user interfaces, and robust backend server databases.",
        "icon": "💻",
        "market_demand": "95% (Massive Industry Demand)",
        "salary_tiers": {"Junior": "₹6 - ₹10 LPA", "Mid": "₹12 - ₹20 LPA", "Lead": "₹28+ LPA"},
        "radar_profile": {"Coding": 95, "UI Design": 85, "Backend Architecture": 90, "Problem Solving": 85, "Math": 50},
        
        "pathways": {
            "degrees": [
                {"name": "B.Tech in Computer Science / Information Technology or BCA", "duration": "3 - 4 Years", "eligibility": "12th Science / Math"},
                {"name": "MCA (Master of Computer Applications)", "duration": "2 Years", "eligibility": "BCA or any graduate with Math"}
            ],
            "diplomas": [
                {"name": "Diploma in Computer Engineering / IT (Polytechnic)", "duration": "3 Years", "eligibility": "10th or 12th Pass"},
                {"name": "Post Graduate Diploma in Full-Stack Web Development", "duration": "6 - 9 Months", "eligibility": "Any Graduate"}
            ],
            "certifications": [
                {"name": "Meta Front-End & Back-End Developer Professional Cert", "platform": "Coursera", "duration": "7 Months"},
                {"name": "Full Stack Open (React, Node, GraphQL, TypeScript)", "platform": "Univ. of Helsinki", "duration": "Self-paced"},
                {"name": "The Odin Project (Full-Stack JavaScript)", "platform": "Open Source", "duration": "Self-paced"}
            ]
        },
        "roadmap": [
            {"phase": "Semester / Phase 1", "desc": "Modern HTML5, CSS3 Grid/Flexbox & Advanced ES6+ JavaScript"},
            {"phase": "Semester / Phase 2", "desc": "Frontend Component Architecture (React.js) & State Management"},
            {"phase": "Semester / Phase 3", "desc": "Backend REST APIs (Node.js/Express or Python/Flask) & SQL DBs"},
            {"phase": "Semester / Phase 4", "desc": "Docker, CI/CD Cloud Deployment & Full-Stack Portfolio Repository"}
        ]
    },
    "cybersecurity_analyst": {
        "title": "Cybersecurity Specialist & Ethical Hacker",
        "tagline": "Protect digital infrastructure, conduct ethical vulnerability audits, and defend against security breaches.",
        "icon": "🛡️",
        "market_demand": "96% (Critical Global Need)",
        "salary_tiers": {"Junior": "₹7 - ₹11 LPA", "Mid": "₹14 - ₹24 LPA", "Lead": "₹30+ LPA"},
        "radar_profile": {"Security": 98, "Networking": 95, "Linux": 85, "Investigation": 90, "Coding": 65},
        
        "pathways": {
            "degrees": [
                {"name": "B.Tech in CSE (Cybersecurity) or B.Sc in IT/Cyber Forensics", "duration": "3 - 4 Years", "eligibility": "12th Science (PCM)"},
                {"name": "M.Tech in Information Security / Cyber Forensics", "duration": "2 Years", "eligibility": "B.Tech CSE / IT / MCA"}
            ],
            "diplomas": [
                {"name": "PG Diploma in Cyber Security & Ethical Hacking", "duration": "1 Year", "eligibility": "Graduate in any stream"},
                {"name": "Advanced Diploma in Network & Information Security", "duration": "6 Months", "eligibility": "12th or Graduate"}
            ],
            "certifications": [
                {"name": "Google Cybersecurity Professional Certificate", "platform": "Coursera", "duration": "6 Months"},
                {"name": "CompTIA Security+ (Global Industry Standard)", "platform": "CompTIA", "duration": "2 - 3 Months"},
                {"name": "Practical Ethical Hacking (PEH) & TCM Labs", "platform": "TCM Security", "duration": "Hands-on"}
            ]
        },
        "roadmap": [
            {"phase": "Semester / Phase 1", "desc": "Computer Networks (TCP/IP, Subnetting, Routing) & Packet Sniffing"},
            {"phase": "Semester / Phase 2", "desc": "Linux CLI Mastery, System Hardening & Bash Security Scripts"},
            {"phase": "Semester / Phase 3", "desc": "OWASP Top 10 Web Exploitation, Burp Suite & Network Scanners"},
            {"phase": "Semester / Phase 4", "desc": "SOC Procedures, SIEM Threat Analysis & Live CTF Competitions"}
        ]
    },
    "ui_ux_product": {
        "title": "UI/UX & Product Design Specialist",
        "tagline": "Design intuitive digital products, wireframes, and accessible visual user experiences (Minimal coding).",
        "icon": "🎨",
        "market_demand": "90% (High Startup Demand)",
        "salary_tiers": {"Junior": "₹5 - ₹9 LPA", "Mid": "₹11 - ₹18 LPA", "Lead": "₹24+ LPA"},
        "radar_profile": {"Creativity": 95, "User Empathy": 90, "Prototyping": 95, "Design Systems": 85, "Coding": 30},
        
        "pathways": {
            "degrees": [
                {"name": "B.Des (Bachelor of Design) in Interaction / Visual Communication", "duration": "4 Years", "eligibility": "12th (Any Stream - Arts, Science, Commerce)"},
                {"name": "M.Des in User Experience & Interaction Design", "duration": "2 Years", "eligibility": "Graduation in any stream (UCEED/CEED)"}
            ],
            "diplomas": [
                {"name": "Diploma in UX/UI Design & Digital Media", "duration": "1 Year", "eligibility": "12th Pass"},
                {"name": "Professional Certificate Diploma in Product Design", "duration": "6 Months", "eligibility": "Any Stream"}
            ],
            "certifications": [
                {"name": "Google UX Design Professional Certificate", "platform": "Coursera", "duration": "6 Months"},
                {"name": "Figma for UI/UX Masterclass", "platform": "Udemy", "duration": "4 Weeks"},
                {"name": "Interaction Design Foundation (IxDF) Certification", "platform": "IxDF", "duration": "Self-paced"}
            ]
        },
        "roadmap": [
            {"phase": "Semester / Phase 1", "desc": "Typography, Color Psychology, Visual Hierarchy & Grid Layouts"},
            {"phase": "Semester / Phase 2", "desc": "Figma Mastery: Components, Auto-Layout, Interactive Prototype Flows"},
            {"phase": "Semester / Phase 3", "desc": "User Research Personas, Information Architecture & Usability Audits"},
            {"phase": "Semester / Phase 4", "desc": "Design 2 End-to-End Case Studies on Behance / Notion Portfolio"}
        ]
    }
}

# ==========================================================
# 2. INFERENCE ENGINE
# ==========================================================
def infer_career(skills_text, interest_text, code_comfort):
    st = skills_text.lower()
    it = interest_text.lower()
    cc = code_comfort.lower()

    if any(k in st for k in ["chem", "molecule", "pharma", "lab"]) or any(k in it for k in ["chem", "molecule", "drug", "science", "lab", "medicine"]):
        return CAREER_DATABASE["computational_chemistry"]
    if any(k in st for k in ["bio", "gene", "dna", "medical", "botany", "zoology"]) or any(k in it for k in ["bio", "gene", "dna", "medical", "healthcare"]):
        return CAREER_DATABASE["bioinformatics"]
    if "creative" in it or "design" in it or "ui" in it or "visual" in it or "no coding" in cc:
        if "design" in it or "creative" in it:
            return CAREER_DATABASE["ui_ux_product"]
    if any(k in st for k in ["network", "linux", "security"]) or any(k in it for k in ["security", "hacking", "cyber", "defense", "investigation"]):
        return CAREER_DATABASE["cybersecurity_analyst"]
    if any(k in st for k in ["math", "data", "python", "stats"]) or any(k in it for k in ["data", "ai", "machine learning", "patterns", "analytics"]):
        return CAREER_DATABASE["data_science_ai"]
    if any(k in st for k in ["web", "html", "javascript", "code"]) or any(k in it for k in ["web", "apps", "software", "building"]):
        return CAREER_DATABASE["fullstack_dev"]

    if "no coding" in cc or "minimal" in cc:
        return CAREER_DATABASE["ui_ux_product"]
    return CAREER_DATABASE["data_science_ai"]

# ==========================================================
# 3. ROUTES
# ==========================================================
@app.route("/")
def index():
    session.clear()
    session["step"] = 0
    session["answers"] = {}
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_msg = data.get("message", "").strip()
    step = session.get("step", 0)
    answers = session.get("answers", {})

    if user_msg.lower() in ["restart", "reset", "clear"]:
        session.clear()
        session["step"] = 0
        session["answers"] = {}
        step = 0

    if step == 0:
        session["step"] = 1
        return jsonify({
            "reply": "Namaste! I am **CareerCraft Pro** 🎓.\n\nI will evaluate your skills & interests to tell you **exactly which Degree, Diploma, or Certification Course** you should pursue.\n\n**Step 1:** What is your **current background, subject, or skill set**?",
            "options": [
                "Chemistry, Pharma & Science",
                "Biology, Biotech & Life Sciences",
                "Mathematics, Statistics & Logic",
                "Computer Basics / Coding (Python, Web, C++)",
                "10th / 12th Pass (Complete Beginner)"
            ],
            "recommendation": None
        })

    elif step == 1:
        answers["skills"] = user_msg
        session["answers"] = answers
        session["step"] = 2

        skills_lower = user_msg.lower()
        if "chem" in skills_lower:
            int_options = [
                "Pharmaceuticals & Drug Discovery",
                "Chemical Simulations & Molecular Research",
                "Data Analysis in Science",
                "Pure Lab Work & Quality Analysis"
            ]
        elif "bio" in skills_lower:
            int_options = [
                "Genomics, DNA & Genetics Research",
                "Healthcare & Clinical Data Analytics",
                "Biotechnology Product Development",
                "Bio-Computing & Computational Biology"
            ]
        else:
            int_options = [
                "Building Web Apps & Digital Products",
                "Artificial Intelligence & Data Insights",
                "Cyber Defense, Ethical Hacking & Security",
                "Creative UI/UX Visual Product Design"
            ]

        return jsonify({
            "reply": f"Understood! Foundation in **{user_msg}** recorded. 💡\n\n**Step 2:** Which specific work domain excites you most?",
            "options": int_options,
            "recommendation": None
        })

    elif step == 2:
        answers["interest"] = user_msg
        session["answers"] = answers
        session["step"] = 3

        return jsonify({
            "reply": f"Great choice! (**{user_msg}**) 🔥\n\n**Step 3:** What is your comfort level with **coding / programming**?",
            "options": [
                "Comfortable writing code / Want to learn deep coding",
                "Can learn basic scripting & tools if needed",
                "Prefer Minimal / Low-Code software tools",
                "Prefer Pure Domain roles (No coding required)"
            ],
            "recommendation": None
        })

    elif step == 3:
        answers["coding_comfort"] = user_msg
        session["answers"] = answers
        session["step"] = 4

        return jsonify({
            "reply": "Almost done! 🎯\n\n**Step 4:** What is your current academic stage or immediate target?",
            "options": [
                "Looking for the Right Degree Program (UG / PG College)",
                "Looking for a 6 - 12 Month Job-Ready Diploma",
                "Looking for Short Online Certification Courses",
                "Preparing for Placements & Internships"
            ],
            "recommendation": None
        })

    elif step == 4:
        answers["goal"] = user_msg
        session["answers"] = answers
        session["step"] = 5

        matched = infer_career(
            answers.get("skills", ""),
            answers.get("interest", ""),
            answers.get("coding_comfort", "")
        )

        reply_text = f"""🎯 **Academic & Career Recommendation Ready!**

Based on your background in **{answers.get('skills')}** and interest in **{answers.get('interest')}**, here is the comprehensive evaluation:

### 🏆 **{matched['title']}**
_{matched['tagline']}_

* **Industry Demand:** `{matched['market_demand']}`
* **Salary Horizon:** `{matched['salary_tiers']['Mid']}` (Mid-Level)

Check out your **Exact Degrees, Diplomas, and Courses** broken down below:"""

        return jsonify({
            "reply": reply_text,
            "options": ["Restart Evaluation", "Why this path?", "How to apply for these?"],
            "recommendation": matched
        })

    else:
        if "why" in user_msg.lower():
            return jsonify({
                "reply": f"🔍 **Inference Reasoning:**\nYour background in **{answers.get('skills', 'your field')}** combined with **{answers.get('interest', 'your domain')}** offers the highest return-on-investment in this specialization. Choosing these degrees or diplomas guarantees you won't waste time on irrelevant subjects.",
                "options": ["Restart Evaluation"],
                "recommendation": None
            })
        return jsonify({
            "reply": "Type **'restart'** to test another profile or subject!",
            "options": ["Restart Evaluation"],
            "recommendation": None
        })

if __name__ == "__main__":
    app.run(debug=True, port=5000)