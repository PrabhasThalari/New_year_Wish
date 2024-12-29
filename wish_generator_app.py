import streamlit as st

# App title
st.title("🎉 New Year Wishes Generator 🎉")

# Input fields
name = st.text_input("Enter Recipient's Name:")
wish_type = st.selectbox(
    "Choose Wish Type:",
    ["Heartfelt", "Flirty", "Funny"]
)

# Generate button
if st.button("Generate Wish"):
    if not name:
        st.warning("Please enter the recipient's name.")
    else:
        if wish_type == "Heartfelt":
            wish = f"Happy New Year, {name}! 🌟 May 2024 bring you endless joy, success, and beautiful moments. You're truly special, and I wish you all the happiness in the world!"
        elif wish_type == "Flirty":
            wish = f"Happy New Year, {name}! 😉 Just a little wish from me to you—may your 2024 be as amazing as your smile. Here's to a year full of surprises (hopefully including me)!"
        elif wish_type == "Funny":
            wish = f"Hey {name}, Happy New Year! 🎉 Here's to a 2024 where your resolutions last longer than your Wi-Fi signal. 😉 Stay awesome!"
        st.success(wish)

# Optional: Save the wish
if st.button("Save Wish to File"):
    if not name:
        st.warning("Generate a wish first!")
    else:
        with open("new_year_wish.txt", "w") as file:
            file.write(wish)
        st.info("Wish saved to new_year_wish.txt!")
