import datetime
import time
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Happy Birthday Archana! ✨", page_icon="🌸", layout="centered"
)

# --- CUSTOM THEME STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    h1, h2, h3, h4 {
        color: #D1477F !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.3);
    }
    .stButton>button:hover {
        background-color: #FF1493;
        color: white;
        box-shadow: 0px 6px 15px rgba(255, 20, 147, 0.4);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- TITLE AREA ---
st.title("✨ Something Special For You, Archana ✨")
st.write("A digital surprise crafted with love and code.")

# --- COUNTDOWN TIMER CONFIGURATION ---
current_year = datetime.datetime.now().year
# Sets the target to exactly 12:01 AM (00:01) on September 3rd
target_date = datetime.datetime(current_year, 9, 3, 0, 1, 0)
now = datetime.datetime.now()

if now > target_date:
    target_date = datetime.datetime(current_year + 1, 9, 3, 0, 1, 0)

time_difference = target_date - now

# REAL TIME LOCK CHECK: Automatically triggers True when now reaches or passes target date
is_birthday = now >= target_date

# --- DISPLAY LOGIC ---
if not is_birthday:
    st.subheader("Counting down the days until September 3rd...")

    col1, col2, col3 = st.columns(3)
    col1.metric("Days Left", time_difference.days)
    col2.metric("Hours Left", time_difference.seconds // 3600)
    col3.metric("Minutes Left", (time_difference.seconds % 3600) // 60)

    st.info(
        "The surprise unlocks automatically on your special day! Stay tuned. 😉"
    )

    # Keeps the timer ticking down live dynamically every second
    time.sleep(1)
    st.rerun()

else:
    st.balloons()
    st.success("🎉 HAPPY BIRTHDAY, ARCHANA! 🎉")

    # 1. Main Photo Section (Locked to size 150)
    st.subheader("📸 A Special Moment")
    try:
        st.image(
            "archana.png",
            caption="Keep shining bright!",
            width=150
        )
    except Exception:
        st.error(
            "Could not find 'archana.png'. Please make sure it is in your open folder directory!"
        )

    # 2. Interactive Note Generator
    st.subheader("💡 Click Below For A Secret Note...")
    if st.button("Click Here 👑"):
        import random

        compliments = [
           "Wishing you a year filled with achievements and boundless joy!", 
           "Ninnu college first roju chusinappude nee midha ishtam perigindhi... ✨❤️", 
        ]
        st.write(f"### 💌 *\"{random.choice(compliments)}\"*")

    # 3. Personalized Letter Section
    st.subheader("✉️ A Note For You")
    with st.expander("Click to open the message from Sai Charan"):
        st.write("""
        Hey Archana,
        
        Naku konchem unique ga wishes chepdham anipinchindhi. Thvaralo manam college lo kuda 
        matladukuntam ani anukuntunna.❤️✨
        
        Have the most beautiful birthday ever!
        
        Best wishes,  
        **Sai Charan**
        """)
