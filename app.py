import streamlit as st

st.set_page_config(
    page_title="Crypto Volatility & Risk Analyzer",
    layout="centered"
)

st.title("📊 Crypto Volatility and Risk Analyzer")
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
        risk = "🔴 High Risk"
    elif price_change > 5:
        risk = "🟡 Medium Risk"
    else:
        risk = "🟢 Low Risk"

    st.success(f"{crypto_name} Risk Level: {risk}")
