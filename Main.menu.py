import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# SESSION STATE
# -------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# -------------------------------
# LOGIN FUNCTION
# -------------------------------
def check_login(username, password):
    return username == "admin" and password == "1234"

# -------------------------------
# DASHBOARD FUNCTION
# -------------------------------
def show_dashboard():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "weak_credentials.csv")
    df = pd.read_csv(data_path)

    # Risk scoring logic
    def compute_risk(row):
        score = 0
        if row["password_length"] < 8:
            score += 20
        if row["reused"] == "yes":
            score += 25
        if row["default_password"] == "yes":
            score += 30
        if row["last_changed_days"] > 180:
            score += 20
        score += row["failed_logins"] * 2
        if row["role"] == "admin":
            score += 10
        return max(100 - score, 0)

    df["risk_score"] = df.apply(compute_risk, axis=1)

    def risk_label(score):
        if score >= 70:
            return "Low"
        elif score >= 40:
            return "Medium"
        return "High"

    df["risk_level"] = df["risk_score"].apply(risk_label)

    # Dashboard layout
    st.sidebar.header("Application Menu")
    st.sidebar.write("You are signed in!")

    st.title("🔐 Credential Hygiene Risk Scoreboard")
    st.divider()

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Accounts", len(df))
    m2.metric("High-Risk Accounts", (df["risk_level"] == "High").sum())
    m3.metric("Average Risk Score", round(df["risk_score"].mean(), 1))

    st.subheader("Credential Risk Level Distribution")
    risk_counts = df["risk_level"].value_counts().reindex(["Low", "Medium", "High"])
    fig, ax = plt.subplots()
    risk_counts.plot(kind="bar", ax=ax, color=["green","orange","red"])
    st.pyplot(fig)

    st.subheader("High-Risk Accounts")
    high_risk_df = df[df["risk_level"]=="High"]
    st.dataframe(high_risk_df)

# -------------------------------
# MAIN APP
# -------------------------------
if not st.session_state.authenticated:
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login(username, password):
            st.session_state.authenticated = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")
else:
    show_dashboard()
