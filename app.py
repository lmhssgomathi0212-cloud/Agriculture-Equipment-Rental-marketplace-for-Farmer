APP_NAME = "AgriRent"

DATABASE_NAME = "database/agrirent.db"
streamlit
import streamlit as st

from backend.database import create_tables
from frontend.home import show_home
from frontend.login import show_login
from frontend.register import show_register
from frontend.equipment import show_equipment
from frontend.rental import show_rental
from frontend.profile import show_profile


st.set_page_config(
    page_title="AgriRent",
    page_icon="🚜",
    layout="wide"
)

create_tables()

st.title("🚜 AgriRent")

st.write(
    "Agriculture Equipment Rental Marketplace for Farmers"
)

st.sidebar.title("🌾 Menu")

menu = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Register",
        "Login",
        "Find Equipment",
        "Rent Equipment",
        "Profile"
    ]
)

if menu == "Home":
    show_home()

elif menu == "Register":
    show_register()

elif menu == "Login":
    show_login()

elif menu == "Find Equipment":
    show_equipment()

elif menu == "Rent Equipment":
    show_rental()

elif menu == "Profile":
    show_profile()

st.sidebar.divider()
st.sidebar.write("🌱 Helping Farmers Find Equipment")
# Frontend package
