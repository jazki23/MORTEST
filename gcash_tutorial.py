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
        "content": "Gcash offers several options but for this tutorial we will choose Send Money",
        "image": "images/step3.png"
    },
    {
        "title": "Step 4: Choose Express Send",
        "content": "For Express Send: Input the recipient’s GCash mobile number.",
        "image": "images/step4.png"
    },
    {
        "title": "Step 5: Enter the recipients register Gcash number",
        "content": "Verify recipient details, amount, and service fees before confirming.",
        "image": "images/step5.png"
    },
    {
        "title": "Step 6: Confirm the Details",
        "content": "Double check the Recipients Mobile number and Correct Amount",
        "image": "images/step6.png"
    },
    {
        "title": "Step 7: Tap the Confirmation Button and Send",
        "content": "Tap the Confirmation button so that you can the Money",
        "image": "images/step7.png"
    },
    {
        "title": "Step 8: Enterthe Authentication Code",
        "content": "GCASH will send you the Authentication Code via SMS",
        "image": "images/step8.png"
    },
    {
        "title": "Step 9: Download to Save the E-Receipt",
        "content": "For transparency purposes",
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

    # Initialize step state
    if "current_step" not in st.session_state:
        st.session_state.current_step = 0

    display_step(st.session_state.current_step)

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Previous") and st.session_state.current_step > 0:
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
