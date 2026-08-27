import streamlit as st
st.set_page_config(
    page_title="Agri Equipment Rental",
    page_icon="🚜",
    layout="wide"
)
st.title("🚜 Agri Equipment Rental")
st.write("Farmers can easily find and rent agricultural equipment.")
st.markdown(
    "### 🌐 [Open Agri Equipment Rental Website](http://localhost:8501)"
)
equipment = [
    {
        "name": "Tractor",
        "category": "Tractor",
        "owner": "Ramesh",
        "location": "Chennai",
        "price": "₹1,500/day"
    },
{
        "name": "Rotavator",
        "category": "Tillage Equipment",
        "owner": "Kumar",
        "location": "Coimbatore",
        "price": "₹1,000/day"
    },
