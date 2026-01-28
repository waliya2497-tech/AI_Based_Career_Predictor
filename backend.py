import pickle
import pandas as pd
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
le_skills = pickle.load(open("le_skills.pkl", "rb"))
le_interest = pickle.load(open("le_interest.pkl", "rb"))
le_education = pickle.load(open("le_education.pkl", "rb"))
le_career = pickle.load(open("le_career.pkl", "rb"))

def text_predict(skill, interest):
    skill = skill.lower()
    interest = interest.lower()

    # Law
    if "law" in skill or "legal" in skill or "court" in skill:
        return "Lawyer / Legal Consultant"

    # Medical
    elif "medical" in skill or "doctor" in skill or "health" in skill:
        return "Doctor / Medical Researcher / Health Consultant"

    # Data / AI
    elif "python" in skill or "machine learning" in skill or "data" in skill:
        return "Data Scientist / AI Engineer / Data Analyst"

    # Software
    elif "java" in skill or "software" in skill or "c++" in skill:
        return "Software Engineer / Backend Developer"

    # Web
    elif "html" in skill or "css" in skill or "javascript" in skill:
        return "Frontend Developer / Web Developer / UI Designer"

    # Business
    elif "business" in skill or "management" in skill or "finance" in skill:
        return "Business Analyst / Marketing Manager / Entrepreneur"

    # Teaching
    elif "teaching" in skill or "education" in skill:
        return "Teacher / Education Consultant / Counselor"

    # Content
    elif "content" in skill or "writing" in skill or "creative" in skill:
        return "Content Writer / Creative Professional"

    else:
        return "Career Counselling Required"


def ml_predict(skill, interest, education):

    skill = skill.lower()
    interest = interest.lower()
    education = education.lower()

     # =================================================
    # 🎓 B.TECH
    # =================================================
    if education in ["b.tech", "btech", "engineering"]:

        if "coding" in skill or "programming" in skill:
            return "Software Engineer"

        elif "data" in skill or "ml" in skill or "ai" in skill:
            return "Data Scientist / ML Engineer"

        elif "network" in skill or "security" in skill:
            return "Network / Cyber Security Engineer"

        elif "hardware" in skill:
            return "Hardware Engineer"

        else:
            return "Graduate Engineer Trainee (GET)"

    # =================================================
    # ⚖️ LLB
    # =================================================
    elif education in ["llb", "law"]:

        if "corporate" in interest:
            return "Corporate Lawyer"

        elif "criminal" in interest:
            return "Criminal Lawyer"

        elif "civil services" in interest or "judiciary" in interest:
            return "Judicial Services Aspirant"

        else:
            return "Legal Advisor"

    # =================================================
    # 💻 BCA
    # =================================================
    elif education in ["bca"]:

        if "web" in skill:
            return "Web Developer"

        elif "software" in skill or "coding" in skill:
            return "Software Developer"

        elif "data" in skill:
            return "Data Analyst"

        else:
            return "IT Support Executive"

    # =================================================
    # 📊 BBA
    # =================================================
    elif education in ["bba"]:

        if "marketing" in interest:
            return "Marketing Executive"

        elif "hr" in interest or "human resource" in interest:
            return "HR Executive"

        elif "finance" in interest:
            return "Business Analyst"

        else:
            return "Management Trainee"

    # =================================================
    # 📘 BA
    # =================================================
    elif education in ["ba", "b.a", "arts"]:

        if "teaching" in interest:
            return "Teacher / Lecturer"

        elif "writing" in skill or "journalism" in interest:
            return "Content Writer / Journalist"

        elif "upsc" in interest or "civil services" in interest:
            return "Civil Services Aspirant"

        elif "social work" in interest:
            return "NGO / Social Worker"

        else:
            return "Career Counselling Required"

    # =================================================
    # 🔬 B.SC
    # =================================================
    elif education in ["b.sc", "bsc", "science"]:

        if "research" in interest:
            return "Research Analyst"

        elif "lab" in skill:
            return "Lab Technician"

        elif "data" in skill:
            return "Data Analyst"

        else:
            return "Higher Studies (M.Sc / PhD)"

    # =================================================
    # 🎓 MBA
    # =================================================
    elif education in ["mba"]:

        if "marketing" in interest:
            return "Marketing Manager"

        elif "finance" in interest:
            return "Financial Analyst"

        elif "hr" in interest:
            return "HR Manager"

        elif "operations" in interest:
            return "Operations Manager"

        else:
            return "Business Consultant"

    # =================================================
    # 🤖 FALLBACK → PURE ML MODEL
    # =================================================
    else:
        skills_enc = le_skills.transform([skill])[0]
        interest_enc = le_interest.transform([interest])[0]
        education_enc = le_education.transform([education])[0]

        X = np.array([[skills_enc, interest_enc, education_enc]])
        pred = model.predict(X)

        return le_career.inverse_transform(pred)[0]