import streamlit as st
import os

# Step data
steps = [
    {
        "title": "Step 1: Open the GCash App",
        "content": "Ensure the GCash app is installed on your smartphone. Log in using your registered mobile number and 4-digit MPIN.",
        "image": "images/step1.png"
    },
    {
        "title": "Step 2: Login using your MPIN",
        "content": "Type the MPIN of your GCash Account.",
        "image": "images/step2.png"
    },
    {
        "title": "Step 3: Tap Send Money",
        "content": "GCash offers several options but for this tutorial, we will choose Send Money.",
        "image": "images/step3.png"
    },
    {
        "title": "Step 4: Choose Express Send",
        "content": "For Express Send: Input the recipient’s GCash mobile number.",
        "image": "images/step4.png"
    },
    {
        "title": "Step 5: Enter the recipient's registered GCash number",
        "content": "Verify recipient details, amount, and service fees before confirming.",
        "image": "images/step5.png"
    },
    {
        "title": "Step 6: Confirm the Details",
        "content": "Double check the recipient's mobile number and amount.",
        "image": "images/step6.png"
    },
    {
        "title": "Step 7: Tap the Confirmation Button and Send",
        "content": "Tap the Confirmation button to send the money.",
        "image": "images/step7.png"
    },
    {
        "title": "Step 8: Enter the Authentication Code",
        "content": "GCash will send you the authentication code via SMS.",
        "image": "images/step8.png"
    },
    {
        "title": "Step 9: Download or Save the E-Receipt",
        "content": "Save the receipt for transparency and recordkeeping.",
        "image": "images/step9.png"
    },
]

def display_step(index):
    step = steps[index]
    st.header(step["title"])
    st.write(step["content"])
    if os.path.exists(step["image"]):
        st.image(step["image"], use_column_width=True)
    else:
        st.warning(f"Image not found: {step['image']}")

def app():
    st.title("GCash Transaction Tutorial")

    if "current_step" not in st.session_state:
        st.session_state.current_step = 0

    display_step(st.session_state.current_step)

    st.markdown(f"**Step {st.session_state.current_step + 1} of {len(steps)}**")

    # Navigation buttons inside a form to prevent double reruns
    with st.form("navigation"):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            prev = st.form_submit_button("Previous")
        with col2:
            next = st.form_submit_button("Next")
        with col3:
            finish = st.form_submit_button("Finish")

        if prev and st.session_state.current_step > 0:
            st.session_state.current_step -= 1
        elif next and st.session_state.current_step < len(steps) - 1:
            st.session_state.current_step += 1
        elif finish:
            st.success("You have completed the tutorial!")
            st.session_state.current_step = 0

if __name__ == "__main__":
    app()
