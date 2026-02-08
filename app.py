import streamlit as st


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Crypto Validator Login",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# Load background image
# -----------------------------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64("login img.png")

# -----------------------------
# CSS (Glass + Blur + Neon Glow)
# -----------------------------
st.markdown(f"""
<style>
/* Background */
.stApp {{
    background-image: url("data:image/png;base64,{bg_img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* Glassmorphism Card */
.login-card {{
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 35px;
    width: 380px;
    margin: auto;
    box-shadow: 0 0 40px rgba(0, 255, 255, 0.25);
    border: 1px solid rgba(255,255,255,0.25);
}}

/* Neon Animated Title */
.login-title {{
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 25px;
    color: #00f7ff;
    animation: glow 2s infinite alternate;
}}

@keyframes glow {{
    from {{
        text-shadow:
            0 0 5px #00f7ff,
            0 0 10px #00f7ff,
            0 0 20px #00f7ff;
    }}
    to {{
        text-shadow:
            0 0 10px #00f7ff,
            0 0 20px #00f7ff,
            0 0 40px #00f7ff;
    }}
}}

/* Inputs */
.stTextInput > div > div > input {{
    border-radius: 10px;
    background: rgba(255,255,255,0.85);
}}

/* Button */
.stButton button {{
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(90deg, #00f7ff, #0072ff);
    color: white;
}}

.stButton button:hover {{
    transform: scale(1.03);
    transition: 0.3s ease;
}}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Fake users
# -----------------------------
USERS = {
    "admin": "admin123",
    "user": "user123"
}

# -----------------------------
# Session
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# Auth
# -----------------------------
def authenticate(username, password):
    return USERS.get(username) == password

# -----------------------------
# UI
# -----------------------------
if not st.session_state.logged_in:

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="login-title">CRYPTO VALIDATOR</div>',
        unsafe_allow_html=True
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid username or password ❌")

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.success("🚀 Welcome to Crypto Validator & Risk Analyzer")
    st.write("Dashboard loading soon...")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()




