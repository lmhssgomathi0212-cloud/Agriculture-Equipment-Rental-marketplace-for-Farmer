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
import streamlit as st
from models.equipment import equipment


def show_home():

    st.header("🏠 Welcome to AgriRent")

    st.write(
        "Farmers can easily find and rent "
        "agricultural equipment."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🚜 Equipment", len(equipment))

    with col2:
        st.metric(
            "👨‍🌾 Owners",
            len(equipment)
        )

    with col3:
        locations = set(
            item["location"]
            for item in equipment
        )

        st.metric(
            "📍 Locations",
            len(locations)
        )

    st.subheader("🌱 Available Equipment")

    for item in equipment:

        st.write(
            f"🚜 **{item['name']}** - "
            f"{item['price']}"
        )
import streamlit as st
from backend.auth import register_user


def show_register():

    st.header("📝 Register")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        if name and email and password:

            result = register_user(
                name,
                email,
                password
            )

            if result:
                st.success(
                    "✅ Registration Successful!"
                )
            else:
                st.error(
                    "❌ Email already exists."
                )

        else:

            st.warning(
                "Please fill all details."
            )
import streamlit as st
from backend.auth import login_user


def show_login():

    st.header("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            email,
            password
        )

        if user:

            st.session_state.logged_in = True
            st.session_state.username = user[1]

            st.success(
                f"✅ Welcome {user[1]}!"
            )

        else:

            st.error(
                "❌ Invalid email or password."
            )
import streamlit as st
from backend.auth import login_user


def show_login():

    st.header("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            email,
            password
        )

        if user:

            st.session_state.logged_in = True
            st.session_state.username = user[1]

            st.success(
                f"✅ Welcome {user[1]}!"
            )

        else:

            st.error(
                "❌ Invalid email or password."
            )
