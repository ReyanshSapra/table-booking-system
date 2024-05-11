import streamlit as st
import os

def book_table(restaurant_name, date, time, name, party_size):
    if os.path.exists(f"{restaurant_name}.txt"):
        with open(f"{restaurant_name}.txt", "r") as file:
            bookings = file.readlines()
        if f"{date} {time}" in bookings:
            st.error("Sorry, the table is already booked at that time.")
            return False
        if bookings.count(f"{date} {time}\n") >= 6:
            st.error("Sorry, the restaurant is fully booked at that time.")
            return False
        with open(f"{restaurant_name}.txt", "a") as file:
            file.write(f"{date} {time} - {name} - Party size: {party_size}\n")
        st.success("Table booked successfully!")
        return True
    else:
        st.error("Invalid restaurant name.")
        return False

def cancel_booking(restaurant_name, name):
    if os.path.exists(f"{restaurant_name}.txt"):
        with open(f"{restaurant_name}.txt", "r") as file:
            bookings = file.readlines()
        if any(name in booking for booking in bookings):
            bookings = [booking for booking in bookings if name not in booking]
            with open(f"{restaurant_name}.txt", "w") as file:
                file.writelines(bookings)
            st.success("Booking canceled successfully!")
            return True
        else:
            st.error("No booking found for that name.")
            return False
    else:
        st.error("Invalid restaurant name.")
        return False

def main():
    st.title("Restaurant Table Booking System")
    st.write("Note: This website is just a test app made for some fun. If you book a table on this website it will not go through.")

    option = st.sidebar.radio("Select an option", ["Book a table", "Cancel booking"])

    if option == "Book a table":
        restaurant_name = st.selectbox("Select a restaurant", ["Harvester", "Nandos", "Brewers Fayre", "McDonalds"])
        date = st.date_input("Select date")
        time = st.time_input("Select time")
        name = st.text_input("Your name")
        party_size = st.number_input("Party size", min_value=1, max_value=10)
        if st.button("Book"):
            book_table(restaurant_name, date, time, name, party_size)

    elif option == "Cancel booking":
        restaurant_name = st.selectbox("Select a restaurant", ["Harvester", "Nandos", "Brewers Fayre", "McDonalds"])
        name_to_cancel = st.text_input("Your name")
        if st.button("Cancel"):
            cancel_booking(restaurant_name, name_to_cancel)

if __name__ == "__main__":
    main()
