import streamlit as st
import time
from src.model import train_model
from src.preprocess import clean_text
from src.priority import assign_priority


st.set_page_config(page_title="Support Ticket Classifier", page_icon="🎫", layout="centered")


st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(120deg, #dbeafe, #fce7f3);
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #1f2937;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #374151;
            margin-bottom: 20px;
        }
        .card {
            background-color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
        }
        .result {
            text-align: center;
            font-size: 20px;
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="title">🎫 Support Ticket Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart classification & priority prediction system</div>', unsafe_allow_html=True)


model, vectorizer = train_model()


st.markdown('<div class="card">', unsafe_allow_html=True)


issue_type = st.selectbox(
    "📌 Select a common issue or choose 'Other':",
    [
         # 🟢 Low Priority
        "General inquiry about plans",
        "Need information about account features",

        # 🟡 Medium Priority
        "Internet not working",
        "Payment failed",
        "Login problem",
        "App crashing",

        # 🔴 High Priority
        "Refund not received urgently",
        "Server down urgently",
        "System not responding ASAP",

        "Other"
    ]
)


if issue_type == "Other":
    user_input = st.text_area("✏️ Enter your issue:", height=120)
else:
    user_input = issue_type


if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("⚠ Please enter an issue")
    else:
        with st.spinner("Analyzing your issue... ⏳"):
            time.sleep(1.5)

        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])

        category = model.predict(vector)[0]
        priority = assign_priority(user_input)

        
        if category == "Technical Issue":
            icon = "🛠️"
        elif category == "Billing Issue":
            icon = "💰"
        else:
            icon = "🔐"

        
        if priority == "High":
            priority_display = "🔴 High"
        elif priority == "Medium":
            priority_display = "🟡 Medium"
        else:
            priority_display = "🟢 Low"

      
        st.success("✅ Analysis Completed!")

        
        st.markdown(f"""
        <div class="result">
            {icon} Category: <b>{category}</b><br><br>
            ⚡ Priority: <b>{priority_display}</b>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)