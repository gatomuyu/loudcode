import streamlit as st

st.set_page_config(
    page_title = "Learn More",
    page_icon = "📄")


tab1, tab2, tab3 = st.tabs(["About Website", "Why Made", "Thanks"])

with tab1:
    st.title("About")
    st.write("**This is A Great Way To Join A Python Job And So We Thank You With Your Support Because Of You :)**")
    st.write("**(This Web Is Still Under Construction So DONT Expect Anything To Work)**")
    st.write("**In Reality, Im The Only One Working On This Website**")
    st.write("**This Project Is Using Streamlit, So I Am Very Limited To Whatever I Can Do**")
    st.header("**How Does The Website Work?**")
    st.write("**When You Open The Page, You Are Sent To The Home Page**")
    st.write("**There Are Four Tabs On The Right [Home Page, Register, Learn More, Settings]**")
    st.header("**Home Page**")
    st.write("""**The Home Page is the Main Page, In Which You Start At, Theres Not Much To Do There But A Couple Things
             And So Its Basically Just AThe Section In Which You Just Chill In, But We Are Modifying It Right Now, We Will
             Add More Things to The Home Page, Such As A Chat Feature With Other Users, And Friend Adding :)**""")
    st.header("**Register Page**")
    st.write("**The Register Page Is The Page That You Create An Account, So You Must Answer A Couple Questions**")
    st.write("**The First Three Questions Is To Set up An Account, Put A Username (Dont Put Your Real Name), Make A Password And Then Confirm your Password**")
    st.write("**Most Of The Other Questions Are Up To You**")
    st.write("**But There is An Other Questions That Ask's For Your App Password**")
    st.header("**What Is An App Password?**")
    st.write("""**An App Password Is A Unique, Randomly Generated 16 Digit Passcode
             That Allows Less Secure Apps Or Devices To Access Your Account
             (Like A Google Or Microsoft Account) When They Don't Support Two Factor Authentication**""")

    st.write("""**To Access Your App Password, go to 'MyGoogleAccount' And Then Go To Security And Then Do The Two-Step Verification And
             Then turn It On, Then Scroll Down An Then Make An App-Password By Giving It A Name And It Will Give You A Code, Use That Code
             And Put It In The App Password Question, If It Doesnt Work, Try Putting It Manually, We Need This information To Send You An Email**""")

    st.header("**Learn More**")
    st.write("""**The Learn More Section Is To understand The Concept Of The Website And Fully Understanding It, The Learn More Section Is
             Is A Huge Chunk Of Words That Explain Every Single Tab An So You Can Understand How to Use This Website, Funny Enough
             You Are Reading It Right Now**""")

    st.header("**Settings**")
    st.write("""**The Settings Tab is A Tab In Where You Can Customize Your Experience With This Website, And So There Are Many Types Of
             Things You Can Change, Such As The Bg Color, Sounds Or Not, And More...**""")

    st.write("**To Learn More About Streamlit, Please Go To (https://streamlit.io)**")
