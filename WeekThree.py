import streamlit as st
import openai
import os

# -------------------------
# Setup API key (replace with your own or use environment variables)
# -------------------------
openai.api_key = "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"

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="TechDoc Generator", page_icon="📄", layout="wide")

st.title("📄 Technical Documentation Generator")
st.write("Generate structured technical documentation using AI.")

# Sidebar inputs
st.sidebar.header("⚙️ Configuration")

project_name = st.sidebar.text_input("Project Name", "My AI Tool")
api_used = st.sidebar.text_input("API / Service", "OpenAI GPT-4")
audience = st.sidebar.selectbox("Audience", ["Developer", "Manager", "Beginner"])
tone = st.sidebar.selectbox("Tone", ["Formal", "Concise", "Explanatory"])
length = st.sidebar.radio("Length", ["Short", "Medium", "Detailed"])

sections = st.sidebar.multiselect(
    "Sections to Include",
    ["Architecture", "API Selection Rationale", "Prompt Methodology", "Performance & Limitations"],
    default=["Architecture", "API Selection Rationale"]
)

generate_btn = st.sidebar.button("🚀 Generate Documentation")

# -------------------------
# Prompt Template
# -------------------------
def build_prompt():
    return f"""
    Generate {length.lower()} technical documentation for a project called "{project_name}".
    The documentation should be written in a {tone.lower()} tone for a {audience.lower()} audience.

    Sections to include: {", ".join(sections)}.

    Provide structured, clear writing with headings and bullet points if helpful.
    """

# -------------------------
# Call OpenAI API
# -------------------------

def generate_documentation(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert technical writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.7,
    )
    return response["choices"][0]["message"]["content"]

# For testing without hitting OpenAI
response = {"choices":[{"message":{"content":"Hello! This is a dummy response."}}]}

# -------------------------
# Main Logic
# -------------------------
if generate_btn:
    with st.spinner("Generating documentation..."):
        prompt = build_prompt()
        try:
            output = generate_documentation(prompt)
            st.subheader("📑 Generated Documentation")
            st.write(output)

            # Export options
            st.download_button("💾 Download as TXT", output, file_name="documentation.txt")
        except Exception as e:
            st.error(f"Error: {e}")
