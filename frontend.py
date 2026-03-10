import streamlit as st
import time
import pickle
import numpy as np

from backend import ml_predict
from backend import text_predict

st.set_page_config(
    page_title="AI Career Predictor",
    page_icon="🎯",
    layout="centered"
)

st.markdown("""
<style>
body {
    background-color: #f0f2f6 !important; 
    color: #0f111a !important;            
}

.stTextInput>div>input,
.stTextArea>div>textarea,
.stSelectbox>div>div>div>select {
    background-color: #1e1e1e !important; 
    color: #ffffff !important;            
    border-radius: 5px;
    padding: 5px;
}
.stButton>button {
    background-color: #1f1f1f !important; 
    color: #ffffff !important;           
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}
.stRadio>div,
.stSelectbox>div {
    color: #ffffff !important;
}

hr {
    border-top: 1px solid #333333;
}

div.stMarkdown p, div.stMarkdown span {
    color: #AAAAAA !important;
}

.stButton>button:hover {
    background-color: #333333 !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():
    model = pickle.load(open("model.pkl", "rb"))
    le_skills = pickle.load(open("le_skills.pkl", "rb"))
    le_interest = pickle.load(open("le_interest.pkl", "rb"))
    le_education = pickle.load(open("le_education.pkl", "rb"))
    le_career = pickle.load(open("le_career.pkl", "rb"))
    return model, le_skills, le_interest, le_education, le_career

model, le_skills, le_interest, le_education, le_career = load_models()

st.markdown("<h1 style='text-align:center;'>🎓 AI Based Career Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Predict your career using AI & skills analysis</p>", unsafe_allow_html=True)
st.divider()

mode = st.radio(
    "Select Prediction Mode",
    ("ML Based", "Free Text")
)

if mode == "ML Based":

    st.subheader("🤖 ML Based Prediction")

    skills = st.text_input("🛠️Enter Skills (comma separated)")
    interest = st.text_input("💡Enter Interest")
    education = st.selectbox(
        "🎓Education Level",
        ["B.Tech", "MBA", "LLB", "B.Sc", "BA", "BCA", "BBA"
        ""]
    )

    if st.button(" Predict Career"):
       with st.spinner("Analyzing skills & interests..."):
        time.sleep(1.5)
        result = ml_predict (skills, interest, education)

        st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.35);
    margin-top: 25px;
">
    <h2 style="color:white; margin-bottom:10px;">🎯 Recommended Career</h2>
    <h1 style="color:#000000; font-weight:800;">{result}</h1>
</div>
""", unsafe_allow_html=True)
        
        #  WHY THIS CAREER 
       st.markdown(f"""
           <div style="
               background-color:#0f172a;
               padding: 25px;
               border-radius: 16px;
               margin-top: 20px;
         ">
              <h3 style="color:#38bdf8;">💡 Why this career?</h3>
              <ul style="color:#e5e7eb;">
              <li>Matches your skills: <b>{skills}</b></li>
              <li>Aligned with your interest in <b>{interest}</b></li>
              <li>Suitable for your education level: <b>{education}</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif mode == "Free Text":

    st.subheader(" Free Text Prediction")

    free_skills = st.text_area("🛠️ Describe your Skills")
    free_interests = st.text_area("🎯 Describe your Interests")
     
    if st.button(" Predict Career"):
       text = free_skills + " " + free_interests

       with st.spinner("Understanding your profile..."):
        time.sleep(1.5)
        result = text_predict(free_skills,free_interests)

       with st.spinner("Understanding your profile..."):
        time.sleep(1.5)
        result = text_predict(free_skills, free_interests)

    
        st.markdown(f"""
              <div style="
               background: linear-gradient(135deg, #1f4037, #99f2c8);
               padding: 25px;
               border-radius: 15px;
               text-align: center;
               box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
               margin-top: 20px;
          ">
        <h2 style="color:#ffffff;">🎯 Recommended Career</h2>
        <h1 style="color:#000000; font-weight:bold;">{result}</h1>
    </div>
    """, unsafe_allow_html=True)

    #  WHY THIS CAREER 
       st.markdown("""
         <div style="
              background:#1e1e1e;
              padding:20px;
              border-radius:12px;
              margin-top:15px;
              box-shadow: 0px 2px 10px rgba(0,0,0,0.3);
         ">
             <h3 style="color:#00ffcc;">💡 Why this career?</h3>
             <ul style="color:#ffffff; font-size:16px;">
             <li>Matches your <b>skills and interests</b></li>
             <li>High demand in the <b>current job market</b></li>
             <li>Good long-term <b>career growth</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
st.divider()
st.markdown("""
<hr>
<p style="text-align:center; font-size:14px; color:#AAAAAA;">
AI Based Career Predictor <br>
Final Year Project | AKTU CSE <br>

</p>

""", unsafe_allow_html=True)

