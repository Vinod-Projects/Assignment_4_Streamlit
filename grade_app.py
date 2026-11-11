import streamlit as st


def get_grade(mark: int) -> str:
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


st.title("Student Grade Manager")
st.write("Add students and review their grades and class results.")

if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add_student"):
    name = st.text_input("Name")
    mark = st.number_input("Mark", min_value=0, max_value=100, value=0, step=1)
    submitted = st.form_submit_button("Add")

if submitted:
    student_name = name.strip()
    if not student_name:
        st.error("Enter a student name.")
    elif not 0 <= mark <= 100:
        st.error("Mark must be between 0 and 100.")
    else:
        st.session_state.students.append(
            {"Name": student_name, "Mark": mark, "Grade": get_grade(mark)}
        )
        st.success(f"Added {student_name}.")

students = st.session_state.students
if students:
    st.subheader("Student Results")
    st.table(students)

    marks = [student["Mark"] for student in students]
    average, highest, lowest = st.columns(3)
    average.metric("Average", f"{sum(marks) / len(marks):.1f}")
    highest.metric("Highest", max(marks))
    lowest.metric("Lowest", min(marks))
else:
    st.info("Add a student to see the class results.")
