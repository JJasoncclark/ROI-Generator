import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

st.title("Jason's ROI Generator")
st.divider()
col1, col2 = st.columns(2)
first = col1.button("First Year", type = "primary", use_container_width=True, on_click=set_state, args = [1])
transfer = col2.button("Transfer", type = "primary", use_container_width=True, on_click=set_state, args = [2])
st.divider()
if st.session_state.stage == 2:
    st.subheader("DAR Status")
    col1, col2 = st.columns(2)
    col1.write("Is the DAR Complete?")
    dars_complete = col2.checkbox("Complete DAR")
    col1.write("Has 105 units been reached?")
    unitmax = col2.checkbox("105 Units Reached")
    col1.write("IGETC Status")
    igetc = col2.selectbox("status", ("IGETC Complete","IGETC Pending", "No IGETC", "Partial IGETC", "Unsure"), label_visibility="collapsed")
    col1.write("")
    col1.write("AHI satisfied?")
    ahi = col2.checkbox("AHI")
    col1.write("Diversity satisfied?")
    diversity = col2.checkbox("Diversity")
    col1.write("Major")
    major = col2.selectbox("major", ("Data Theory", "Applied Math", "Math of Computation", "Math Econ", "FAM", "Business Economics"), label_visibility="collapsed")
    st.divider()
    st.subheader("Interests")
    col1, col2 = st.columns(2)
    clubs = col1.checkbox("Clubs")
    research = col2.checkbox("Research")
    rec = col1.checkbox("UCLA Rec")
    career = col2.checkbox("Career")
if st.session_state.stage == 1:
    st.subheader("DAR Status")
    col1, col2 = st.columns(2)
    col1.write("Is the DAR Complete?")
    dars_complete = col2.checkbox("Complete DAR")
    col1.write("Has 105 units been reached?")
    unitmax = col2.checkbox("105 Units Reached")
    col1.write("Major")
    major = col2.selectbox("major", ("Data Theory", "Applied Math", "Math of Computation", "Math Econ", "FAM", "Business Economics"), label_visibility="collapsed")
    st.divider()
    st.subheader("Interests")
    col1, col2 = st.columns(2)
    clubs = col1.checkbox("Clubs")
    research = col2.checkbox("Research")
    rec = col1.checkbox("UCLA Rec")
    career = col2.checkbox("Career")
st.divider()
col1, col2, col3 = st.columns(3)
generate = col2.button("Generate ROI", use_container_width=True)
if generate == True and st.session_state.stage == 2:
    if dars_complete == True:
        st.caption("All work is posted on the DAR")
        st.caption(" ")
    if unitmax == True:
        st.caption("UCLA limits students to 105 lower division units outside of the University of California. Units earned for AP, IB, or GCE A-level are not counted in the 105 limit. Please consult your Degree Audit Report (DAR) in the Fall Quarter to see the specific deductions for your incoming units. Transferable courses may still receive subject credit and satisfy degree requirement even if they do not earn unit credit.")
        st.caption(" ")
    if ahi != True:
        st.caption("Student has not completed their American History and Institutions Requirement. Reminded that they have until graduation to do so and can satisfy the requirement by taking a course from the approved list of courses on the Degree Audit Report (DAR). ")
        st.caption(" ")
    if diversity != True:
        st.caption("Student has not yet satisfied their Diversity Requirement. Reminded student that they have until graduation to do so and can satisfy the requirement by taking a course from the approved list of courses (see the DAR).")
        st.caption(" ")
    if igetc == "IGETC Pending":
        st.caption("Student reports that they have completed IGETC. Advised student to follow up with their community college to certify and send verification to UCLA. Advised student that if they don't do this, they will be held to UCLA's College/School requirements.")
        st.caption(" ")
    if igetc == "Patial IGETC":
        st.caption("Student has reported they have completed partial IGETC. Advised student to follow up with their academic counseling unit XXX put in appropriate info here XXX to determine what class to take at UCLA to complete IGETC. Advised student that if they don't do this, they will be held to UCLA's College requirements.")
        st.caption(" ")
    if igetc == "Unsure":
        st.caption("Student's DAR is reflecting that IGETC is pending and student is unsure if they completed it. Advised student to follow up with their community college to verify and send certification to UCLA. If IGETC is not complete, student will be held to UCLA’s College/School requirements and advised to follow up with their academic advising unit XXX put in appropriate info here XXX to determine what still needs to be completed.")
        st.caption(" ")
    if major == "Data Theory":
        st.caption("Student is a Pre Data Theory major, referred them to the Mathematics Department for major advising, https://ww3.math.ucla.edu/. Moreover, advised student that they have until the end of the summer after their first year at UCLA in order to complete the prep courses for the major. Finally, advised the student that they should plan to meet with the department in the Fall in order to plan out their next two years in order to stay on track.")
        st.caption(" ")
    if major == "Applied Math":
        st.caption("Student is a Pre Applied Mathematics major, referred them to the Mathematics Department for major advising, https://ww3.math.ucla.edu/. Moreover, advised student that they have until the end of the summer after their first year at UCLA in order to complete the prep courses for the major.")
        st.caption(" ")
    if major ==  "Business Economics":
        st.caption("Student is a Business Economics major, referred them to the Economics Department for major advising, https://economics.ucla.edu/.")
        st.caption(" ")
    if clubs == True:
        st.caption("Student shared that they are interested in clubs, advised them to check out the Enormous Activities Fair (EAF) in the Fall and UCLA Student Organizations, Leadership & Engagement (SOLE) at https://sole.ucla.edu/ to see if there are any organizations they are interested in being apart of.")
        st.caption(" ")
    if research == True:
        st.caption("Student shared they were interested in research opportunities, advised them to check out the Undergraduate Research Center, https://sciences.ugresearch.ucla.edu/.")
        st.caption(" ")
    if rec == True:
        st.caption("Student shared that they are interested in staying active and intramural sports, advised them to check out UCLA Recreation and the facilities and programs offered there at https://recreation.ucla.edu/.")
        st.caption(" ")
    if career == True:
        st.caption("Student shared they are interested in internships and career development, advised them to check out the resources available at the Career Center at https://career.ucla.edu/.")
        st.caption(" ")
    st.caption("Student is a transfer student, thus advised to check out the Transfer Student Center at Kerckhoff Hall 128 or https://transfers.ucla.edu/. Moreover the student can find more transfer student related resources at UCLA Student Organizations, Leadership & Engagement (SOLE) at 105 Kerckhoff Hall or https://sole.ucla.edu/.")
    st.caption(" ")
    st.caption("Moreover, since the student is a transfer student, advised them about quick deadlines that arise in the fall surrounding minor and major deadlines and applying for on campus jobs and positions.")
    st.caption(" ")
    st.caption("Had student run their DAR and add a class to class planner. Reviewed major courses and gave course recommendations.")
if generate == True and st.session_state.stage == 1:
    if dars_complete == True:
        st.caption("All work is posted on the DAR")
        st.caption(" ")
    if unitmax == True:
        st.caption("UCLA limits students to 105 lower division units outside of the University of California. Units earned for AP, IB, or GCE A-level are not counted in the 105 limit. Please consult your Degree Audit Report (DAR) in the Fall Quarter to see the specific deductions for your incoming units. Transferable courses may still receive subject credit and satisfy degree requirement even if they do not earn unit credit.")
        st.caption(" ")
    if major == "Data Theory":
        st.caption("Student is a Pre Data Theory major, referred them to the Mathematics Department for major advising, https://ww3.math.ucla.edu/.")
        st.caption(" ")
    if major == "Applied Math":
        st.caption("Student is a Pre Applied Mathematics major, referred them to the Mathematics Department for major advising, https://ww3.math.ucla.edu/.")
        st.caption(" ")
    if major ==  "Business Economics":
        st.caption("Student is a Business Economics major, referred them to the Economics Department for major advising, https://economics.ucla.edu/.")
        st.caption(" ")
    if clubs == True:
        st.caption("Student shared that they are interested in clubs, advised them to check out the Enormous Activities Fair (EAF) in the Fall and UCLA Student Organizations, Leadership & Engagement (SOLE) at https://sole.ucla.edu/ to see if there are any organizations they are interested in being apart of.")
        st.caption(" ")
    if research == True:
        st.caption("Student shared they were interested in research opportunities, advised them to check out the Undergraduate Research Center, https://sciences.ugresearch.ucla.edu/.")
        st.caption(" ")
    if rec == True:
        st.caption("Student shared that they are interested in staying active and intramural sports, advised them to check out UCLA Recreation and the facilities and programs offered there at https://recreation.ucla.edu/.")
        st.caption(" ")
    if career == True:
        st.caption("Student shared they are interested in internships and career development, advised them to check out the resources available at the Career Center at https://career.ucla.edu/.")
        st.caption(" ")
    st.caption("Had student run their DAR and add a class to class planner. Went over university, college, and GE requirements that the student has satisfied and those that they have not and advised certain deadlines and requirements for each. Reviewed major prep courses and gave course recommendations.")
    
