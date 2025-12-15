import streamlit as st


def home_page():
    st.title("Welcome to Sunbeam Infotech")
    st.write("Empowering Your Future with Professional Courses in Emerging Technologies")
    st.write("At Sunbeam Infotech, we are committed to providing top-notch professional courses that equip individuals with the skills and knowledge needed to thrive in today's rapidly evolving technological landscape. Our courses are designed to bridge the gap between academic learning and industry requirements, ensuring that our students are job-ready and prepared for the challenges of the modern workforce.")
    st.write("Join us on a transformative learning journey and unlock your potential with Sunbeam Infotech!")

def About_us():
    st.title("About Us")
    st.write("At Sunbeam we believe retaining a competitive edge is imperative for any individual in today's professional world. Companies are restructuring their organizations & reengineering their business processes. Not only have the challenges become more demanding, but also the rewards of staying at the forefront seem to be promising.")
    st.write("Sunbeam offers a wide range of professional courses in emerging technologies like Data Science, AI/ML, Cloud Computing, DevOps, Full Stack Development, etc. Our courses are designed to bridge the gap between industry requirements and academic learning. With a focus on hands-on training and real-world projects, we ensure that our students are job-ready and equipped with the skills needed to excel in their careers.")
    st.write("Our experienced faculty members bring a wealth of industry knowledge and expertise to the classroom. They are dedicated to providing personalized attention and mentorship to each student, fostering a collaborative learning environment.")
    st.write("Join Sunbeam today and embark on a transformative learning journey that will empower you to achieve your professional goals and thrive in the ever-evolving tech landscape.")

def contact_us():
    st.title("Contact Us")
    st.write("Sunbeam Infotech")
    st.write("Address: 123 Tech Avenue, Innovation City, Country")
    st.write("Phone: +1 (123) 456-7890")
    st.write("Email: xyz@sunbeam.com")


def couses_page():
    st.header("Our Courses")
    st.write("Explore our wide range of professional courses designed to equip you with the skills needed to excel in today's competitive job market. Whether you're looking to upskill, reskill, or embark on a new career path, we have the right course for you.")
    st.write("Our courses cover emerging technologies such as Data Science, AI/ML, Cloud Computing, DevOps, Full Stack Development, and more. Each course is crafted to provide hands-on training and real-world projects, ensuring that you gain practical experience alongside theoretical knowledge.")
    st.write("Join us today and take the first step towards a successful and fulfilling career in the tech industry!")


def internship_page():
    st.header("Internship Opportunities")
    st.write("At Sunbeam Infotech, we believe that practical experience is a crucial component of professional development. That's why we offer a range of internship opportunities designed to provide our students with hands-on experience in real-world projects.")
    st.write("Our internship programs are tailored to help students apply the skills and knowledge they have gained in our courses to real industry challenges. Interns will have the chance to work alongside experienced professionals, gain valuable insights into industry practices, and build a strong foundation for their future careers.")
    st.write("Join our internship program today and take the first step towards a successful career in the tech industry!")

def contact_page():
    st.header("Get in Touch with Us")
    st.write("We would love to hear from you! Whether you have questions about our courses, need assistance with enrollment, or simply want to learn more about what we offer, our team is here to help.")
    st.write("Feel free to reach out to us through any of the following channels:")

if 'page' not in st.session_state:
    st.session_state.page='home'

with st.sidebar:
    st.title("Sunbeam Infotech")
    if st.button("Home" ,width="stretch"):
        st.session_state.page='home'
    if st.button("About Us",width="stretch"):
        st.session_state.page='about_us'
    if st.button("Courses",width="stretch"):
        st.session_state.page='courses'
    if st.button("Internships",width="stretch"):
        st.session_state.page='internships'
    if st.button("Contact Us",width="stretch"):
        st.session_state.page='contact_us'

if st.session_state.page=='home':
    home_page()
elif st.session_state.page=='about_us':
    About_us()  
elif st.session_state.page=='courses':
    couses_page()
elif st.session_state.page=='internships':
    internship_page()
elif st.session_state.page=='contact_us':
    contact_page()
    