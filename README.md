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
st.subheader("Available Equipment")
    for item in equipment:
        st.subheader("🚜 " + item["name"])
        st.write("Category:", item["category"])
        st.write("Owner:", item["owner"])
        st.write("Location:", item["location"])
        st.write("Rental Price:", item["price"])
        st.divider()
elif menu == "🔍 Find Equipment":
    st.header("🔍 Find Agricultural Equipment")
    search = st.text_input(
        "Search equipment",
        placeholder="Example: Tractor, Harvester...",
        key="equipment_search"
    )
    category = st.selectbox(
        "Select Category",
        [
            "All",
            "Tractor",
            "Tillage Equipment",
            "Sowing Equipment",
            "Weeding Equipment",
            "Harvesting Equipment",
            "Spraying Equipment"
        ],
        key="equipment_category"
    )
results = []
    for item in equipment:
        search_match = (
            search.lower() in item["name"].lower()
            or search.lower() in item["category"].lower()
            or search.lower() in item["location"].lower()
        )
        category_match = (
            category == "All"
            or item["category"] == category
        )
        if search_match and category_match:
            results.append(item)
            if results:
        st.success(f"{len(results)} equipment found.")
        for item in results:
            st.subheader("🚜 " + item["name"])
            col1, col2 = st.columns(2)
            with col1:
                st.write("Category:", item["category"])
                st.write("Owner:", item["owner"])
            with col2:
                st.write("Location:", item["location"])
                st.write("Rental Price:", item["price"])
if st.button(
                "Rent Equipment",
                key=f"rent_{item['name']}"
            ):
                st.success(
                    f"You selected {item['name']} for rental."
                )
            st.divider()
    else:
        st.warning("No equipment found.")
elif menu == "👤 Profile":
    st.header("👤 Profile")
    name = st.text_input(
        "Your Name",
        key="profile_name"
    )
    phone = st.text_input(
        "Phone Number",
        key="profile_phone"
    )
    location = st.text_input(
        "Your Location",
        key="profile_location"
    )
if st.button(
        "Save Profile",
        key="save_profile"
    ):
        if name and phone and location:
            st.success("✅ Profile saved successfully!")
            st.write("Name:", name)
            st.write("Phone:", phone)
            st.write("Location:", location)
        else:
            st.warning("Please fill in all the fields.")
