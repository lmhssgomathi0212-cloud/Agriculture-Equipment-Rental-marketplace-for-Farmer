# Agriculture-Equipment-Rental-marketplace-for-Farmer
Agriculture Equipment Rental Marketplace is a platform that helps farmers rent agricultural machinery easily from equipment owners at affordable prices.
import streamlit as st
st.set_page_config(page_title="AgriRent", page_icon="🚜")
equipment = [
    {"name": "Mahindra Tractor", "type": "Tractor", "price": 1200,
     "location": "Pudukkottai"},
    {"name": "John Deere Tractor", "type": "Tractor", "price": 1500,
     "location": "Trichy"},
    {"name": "Combine Harvester", "type": "Harvester", "price": 2500,
     "location": "Thanjavur"},
    {"name": "Power Sprayer", "type": "Sprayer", "price": 700,
     "location": "Madurai"},
    {"name": "Rotavator", "type": "Rotavator", "price": 1000,
     "location": "Pudukkottai"}
]
if "bookings" not in st.session_state:
    st.session_state.bookings = []
st.title("🚜 AgriRent")
st.subheader("Agricultural Equipment Rental Marketplace")
menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Find Equipment", "Book Equipment",
     "Add Equipment", "My Bookings"]
)
