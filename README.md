📄 Technical Documentation Generator (Custom Content Generator)
Overview

The Technical Documentation Generator is a Python-based web application built with Streamlit that uses AI to generate structured, high-quality technical content for a specific use case: technical documentation.

The app allows users to configure the type, tone, length, and audience of documentation, making it useful for developers, technical writers, managers, and beginners who need clear, well-organized technical content quickly.

🎯 Purpose
This web app was created to fulfill the requirement:

Create a specialized content generation tool that produces high-quality outputs for a specific use case.

Specific use case:
➡️ Generating technical documentation such as API guides, setup instructions, troubleshooting manuals, and FAQs.

🧠 What the App Does
Users can:
* Define a project name
* Choose the intended audience
* Select a writing tone
* Control the length of the output
* Select specific documentation sections to include
The app then generates structured technical documentation using AI.

🖥️ Features:
* 🧩 Interactive Streamlit UI
* ⚙️ Sidebar configuration controls
* 📑 Structured documentation output
* 🎨 Custom branding with logo support
* 💾 Download generated content as a text file
* 🔐 Secure API key handling using Streamlit secrets

🛠️ Tech Stack
* Language: Python
* Framework: Streamlit
* AI Integration: OpenAI API
* Environment Management: Virtual environment (venv)
* Secrets Management: .streamlit/secrets.toml

📂 Project Structure
Custom-content-generator/
│
├── WeekThree.py           # Main Streamlit application
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python version specification
├── README.md              # Project documentation
├── NS logo.jpg            # Application logo
└── .streamlit/
    └── secrets.toml       # API key (ignored by Git)

🚀 How to Run Locally
1️⃣ Clone the repository (through git bash)
git clone https://github.com/Chuene01/Custom-content-generator.git
cd Custom-content-generator


2️⃣ Create and activate a virtual environment (through terminal/git bash)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux


3️⃣ Install dependencies (through git bash)
pip install -r requirements.txt


4️⃣ Add your API key
Create the file (through git bash):
.streamlit/secrets.toml

Add:
API_KEY = "your_openai_api_key_here"

⚠️ This file is ignored by Git and should never be committed.


5️⃣ Run the app
streamlit run WeekThree.py

🌐 Deployment
This app can be deployed easily using:
* Streamlit Cloud (recommended)
* Render
* Other Python-compatible hosting platforms
Secrets are managed securely through platform-specific environment settings.

🔐 Security Considerations
* API keys are never hard-coded
* Secrets are excluded from version control
* Keys can be rotated or revoked at any time

📌 Use Cases
* Technical documentation drafting
* API guides
* Setup and installation manuals
* Troubleshooting documentation
* Knowledge base and FAQ creation

✨ Future Improvements
* Support for PDF and Markdown exports
* User authentication
* Template presets per documentation type
* Usage limits and analytics

👤 Author
Chuene Moloto