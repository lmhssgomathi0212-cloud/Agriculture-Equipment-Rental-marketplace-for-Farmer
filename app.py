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
import streamlit as st
from models.equipment import equipment


def show_equipment():

    st.header("🔍 Find Equipment")

    search = st.text_input(
        "Search Equipment"
    )

    found = False

    for item in equipment:

        if search.lower() in item["name"].lower():

            found = True

            st.subheader(
                "🚜 " + item["name"]
            )

            st.write(
                "👨‍🌾 Owner:",
                item["owner"]
            )

            st.write(
                "📍 Location:",
                item["location"]
            )

            st.write(
                "💰 Price:",
                item["price"]
            )

            st.divider()

    if not found:

        st.info(
            "No equipment found."
        )
import streamlit as st

from models.equipment import equipment
from backend.rental_service import add_rental


def show_rental():

    st.header("📋 Rent Equipment")

    names = [
        item["name"]
        for item in equipment
    ]

    selected = st.selectbox(
        "Select Equipment",
        names
    )

    customer = st.text_input(
        "Customer Name"
    )

    days = st.number_input(
        "Number of Days",
        min_value=1,
        step=1
    )

    if st.button("Confirm Rental"):

        if customer:

            add_rental(
                selected,
                customer,
                days
            )

            st.success(
                f"✅ {selected} rented for "
                f"{days} day(s)!"
            )

        else:

            st.warning(
                "Please enter customer name."
            )
import streamlit as st


def show_profile():

    st.header("👤 Profile")

    name = st.text_input("Your Name")

    phone = st.text_input(
        "Phone Number"
    )

    location = st.text_input(
        "Your Location"
    )

    if st.button("Save Profile"):

        if name and phone and location:

            st.success(
                "✅ Profile Saved!"
            )

            st.write("Name:", name)
            st.write("Phone:", phone)
            st.write("Location:", location)

        else:

            st.warning(
                "Please fill all details."
            )
# Backend package
import sqlite3
import os

from config import DATABASE_NAME


def get_connection():

    os.makedirs(
        "database",
        exist_ok=True
    )

    return sqlite3.connect(
        DATABASE_NAME
    )


def create_tables():

    db = get_connection()

    db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS rentals(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipment TEXT,
            customer TEXT,
            days INTEGER
        )
    """)

    db.commit()
    db.close()
import sqlite3

from backend.database import get_connection


def register_user(
    name,
    email,
    password
):

    db = get_connection()

    try:

        db.execute(
            """
            INSERT INTO users
            (name, email, password)
            VALUES (?, ?, ?)
            """,
            (name, email, password)
        )

        db.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        db.close()


def login_user(
    email,
    password
):

    db = get_connection()

    user = db.execute(
        """
        SELECT * FROM users
        WHERE email = ?
        AND password = ?
        """,
        (email, password)
    ).fetchone()

    db.close()

    return user
