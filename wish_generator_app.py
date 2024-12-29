import streamlit as st
import sys
import urllib.parse

st.title("🎉 New Year Wishes Generator 🎉")

# Fetch query parameters
name = st.text_input("Enter Recipient's Name:", value=sys.argv[1] if len(sys.argv) > 1 else "")
wish_type = st.selectbox(
    "Choose Wish Type:",
    ["Heartfelt", "Flirty", "Funny"],
    index=sys.argv[2] if len(sys.argv) > 2 else 0
)

# Display the wish if the button is clicked
if st.button("Generate Wish"):
    if not name:
        st.warning("Please enter the recipient's name.")
    else:
        if wish_type == "Heartfelt":
            wish = f"Happy New Year, {name}! 🌟 May 2024 bring you endless joy, success, and beautiful moments."
        elif wish_type == "Flirty":
            wish = f"Happy New Year, {name}! 😉 Just a little wish from me to you—may your 2024 be as amazing as your smile."
        elif wish_type == "Funny":
            wish = f"Hey {name}, Happy New Year! 🎉 Here's to a 2024 where your resolutions last longer than your Wi-Fi signal."
        st.success(wish)

# Generate URL for sharing
if st.button("Get Shareable Link"):
    if name:
        encoded_name = urllib.parse.quote(name)
        encoded_wish_type = urllib.parse.quote(str(wish_type))
        url = f"https://your-app-name.streamlit.app/?name={encoded_name}&wish_type={encoded_wish_type}"
        st.success(f"Share this link: {url}")
    else:
        st.warning("Please generate a wish first.")
