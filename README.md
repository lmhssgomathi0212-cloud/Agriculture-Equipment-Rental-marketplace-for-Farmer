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
{
        "name": "Seed Drill",
        "category": "Sowing Equipment",
        "owner": "Suresh",
        "location": "Madurai",
        "price": "₹800/day"
    },
    {
        "name": "Power Weeder",
        "category": "Weeding Equipment",
        "owner": "Arun",
        "location": "Salem",
        "price": "₹700/day"
    },
    {
        "name": "Harvester",
        "category": "Harvesting Equipment",
        "owner": "Mani",
        "location": "Trichy",
        "price": "₹2,500/day"
    },
    {
        "name": "Sprayer",
        "category": "Spraying Equipment",
        "owner": "Vijay",
        "location": "Erode",
        "price": "₹500/day"
    }
]
st.sidebar.title("🌾 Menu")

menu = st.sidebar.radio(
    "Select an option",
    ["🏠 Home", "🔍 Find Equipment", "👤 Profile"],
    key="main_menu"
)
if menu == "🏠 Home":
    st.header("Welcome to Agri Equipment Rental 🌱")
    st.write(
        "Our platform helps farmers find agricultural equipment "
        "available for rental."
    )
col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🚜 Equipment", len(equipment))
    with col2:
        st.metric(
            "👨‍🌾 Owners",
            len(set(item["owner"] for item in equipment))
        )
    with col3:
        st.metric(
            "📍 Locations",
            len(set(item["location"] for item in equipment))
        )
