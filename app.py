import streamlit as st

st.set_page_config(
    page_title="Crypto Volatility & Risk Analyzer",
    layout="centered"
)

st.title("Crypto Volatility and Risk Analyzer")
st.write("Analyze cryptocurrency volatility and identify risk level easily.")

crypto_name = st.text_input("Enter Cryptocurrency Name (e.g., Bitcoin)")

price_change = st.number_input(
    "Enter Daily Price Change (%)",
    min_value=0.0,
    max_value=100.0,
    step=0.1
)

if st.button("Analyze Risk"):
    if price_change > 10:
        risk = " High Risk"
    elif price_change > 5:
        risk = " Medium Risk"
    else:
        risk = " Low Risk"

    st.success(f"{crypto_name} Risk Level: {risk}")
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CVRA</title>
  <link rel="stylesheet" href="style.css">
</head>
<body img src="C:\Users\Admin\Desktop\crypto-risk-analyzer\templates\icon.png">
  
  <div class="overlay"></div>
 

  <div class="wrapper">
    <button id="getSetBtn"> GET SET</button>

    <div class="login-container" id="loginBox">
      <h2>WELCOME BOSS </h2>

      <input type="text" placeholder="Username or Email">
      <input type="password" placeholder="Password">

      <a href="#" class="forgot">Forgot password or username?</a>

      <button class="login-btn">Login</button>
    </div>
  </div>
</body>
</html>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

body {
  height: 100vh;
  no-repeat center/cover;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}


.overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.6);
}


.wrapper {
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 25px;
}

#getSetBtn {
  padding: 16px 45px;
  font-size: 18px;
  border-radius: 30px;
  border: none;
  background: linear-gradient(135deg, #00f2fe, #4facfe);
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

#getSetBtn:hover {
  transform: scale(1.1);
  box-shadow: 0 10px 30px rgba(79,172,254,0.6);
}


.login-container {
  width: 340px;
  padding: 30px;
  border-radius: 16px;
  background: rgba(255,255,255,0.15);
  backdrop-filter: blur(12px);
  color: #fff;
  text-align: center;
  transform: translateY(-400px) scale(0.8);
  opacity: 0;
  transition: all 0.9s cubic-bezier(.68,-0.55,.27,1.55);
}


.login-container.active {
  transform: translateY(0) scale(1);
  opacity: 1;
}


.login-container input {
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border-radius: 8px;
  border: none;
  outline: none;
}


.forgot {
  display: block;
  margin: 12px 0;
  font-size: 14px;
  color: #ddd;
  text-decoration: none;
}


.login-btn {
  width: 100%;
  padding: 12px;
  margin-top: 10px;
  border-radius: 25px;
  border: none;
  background: linear-gradient(135deg, #43e97b, #38f9d7);
  color: #000;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.login-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(56,249,215,0.6);
}



