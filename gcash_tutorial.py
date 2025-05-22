import streamlit as st

# Steps data
steps = [
    {
        "title": "Step 1: Open the GCash App",
        "content": "Ensure the GCash app is installed on your smartphone. Log in using your registered mobile number and 4-digit MPIN.",
        "image": "images/step1.png"
    },
    {
        "title": "Step 2: Access the 'Send Money' Feature",
        "content": "On the app’s home screen, tap on the ‘Send’ or ‘Send Money’ button.",
        "image": "images/step2.png"
    },
    {
        "title": "Step 3: Choose Express Send",
        "content": "GCash offers several options for sending money:\n- **Express Send**\n- **Send via QR**\n- **Send to Bank**",
        "image": "images/step3.png"
    },
    {
        "title": "Step 4: Enter the Recipient's GCash Mobile Number",
        "content": "For Express Send: Input the recipient’s GCash mobile number.\nFor Send via QR: Scan a QR code.\nFor Send to Bank: Provide bank details.",
        "image": "images/step4.png"
    },
    {
        "title": "Step 5: Review Transaction Details",
        "content": "Verify recipient details, amount, and service fees before confirming.",
        "image": "images/step5.png"
    },
    {
        "title": "Step 6: Transaction Confirmation",
        "content": "You will be prompted to enter your 6-digit code to authenticate the transaction.",
        "image": "images/step6.png"
    },
    {
        "title": "Step 7: Authentication Code",
        "content": "You'll receive a text message from GCash containing the authentication code.",
        "image": "images/step7.png"
    },
    {
        "title": "Step 8: Save/Share the Receipt",
        "content": "You can screenshot or download the receipt for your records.",
        "image": "images/step8.png"
    },
]

# Display the selected step
def display_step(step_index):
    step = steps[step_index]
    st.header(step["title"])
    st.write(step["content"])
    st.image(step["image"], use_column_width=True)

# Main app function
def app():
    st.title("GCash Transaction Tutorial")

    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0

    display_step(st.session_state.current_step)

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.current_step > 0:
            if st.button("Previous"):
                st.session_state.current_step -= 1

    with col2:
        if st.session_state.current_step < len(steps) - 1:
            if st.button("Next"):
                st.session_state.current_step += 1
        else:
            if st.button("Finish"):
                st.success("You have completed the tutorial!")
                st.session_state.current_step = 0

    st.markdown(f"**Step {st.session_state.current_step + 1} of {len(steps)}**")

if __name__ == "__main__":
    app()
