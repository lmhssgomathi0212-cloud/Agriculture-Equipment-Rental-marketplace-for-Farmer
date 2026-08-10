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
if menu == "Home":
    st.write("### 🌾 Welcome Farmers!")
    st.write("Rent agricultural equipment at affordable prices.")
    st.info("Farmers can rent machines from nearby equipment owners.")
    st.success("Save money by renting instead of buying machinery.")
elif menu == "Find Equipment":
    st.header("🔍 Find Equipment")
    location = st.text_input("Enter your location")
    kind = st.selectbox(
        "Equipment Type",
        ["All", "Tractor", "Harvester",
         "Sprayer", "Rotavator"]
    )
    for item in equipment:
        if ((kind == "All" or item["type"] == kind) and
                (not location or
                 location.lower() in item["location"].lower())):
            st.write(f"### 🚜 {item['name']}")
            st.write(f"Type: {item['type']}")
            st.write(f"Location: {item['location']}")
            st.write(f"Rent: ₹{item['price']} / day")
            st.divider()
elif menu == "Book Equipment":
    st.header("📅 Book Equipment")
    names = [x["name"] for x in equipment]
    selected = st.selectbox("Select Equipment", names)
    days = st.number_input("Number of Days", 1, 30, 1)
    farmer = st.text_input("Farmer Name")
    if st.button("Confirm Booking"):
        item = next(x for x in equipment
                    if x["name"] == selected)
        total = item["price"] * days
        st.session_state.bookings.append(
            {"farmer": farmer,
             "equipment": selected,
             "days": days,
             "total": total}
        )
        st.success(f"Booking confirmed! Total: ₹{total}")
elif menu == "Add Equipment":
    st.header("➕ Add Equipment")
    name = st.text_input("Equipment Name")
    typ = st.selectbox(
        "Type",
        ["Tractor", "Harvester",
         "Sprayer", "Rotavator"]
    )
    price = st.number_input("Daily Rent", 100, 10000)
    loc = st.text_input("Location")
    if st.button("Add Listing"):
        equipment.append({
            "name": name,
            "type": typ,
            "price": price,
            "location": loc
        })
        st.success("Equipment listed successfully!")
elif menu == "My Bookings":
    st.header("📋 My Bookings")
    if not st.session_state.bookings:
        st.warning("No bookings available.")
    else:
        for booking in st.session_state.bookings:
            st.write(f"👨‍🌾 Farmer: {booking['farmer']}")
            st.write(f"🚜 Equipment: {booking['equipment']}")
            st.write(f"📅 Days: {booking['days']}")
            st.write(f"💰 Total: ₹{booking['total']}")
            st.divider()
