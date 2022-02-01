import streamlit as st
import random
import os

#[theme]
#backgroundColor="#fffef2"
#secondaryBackgroundColor="#fff8c4"
#textColor="#000000"
#theme = os.listdir(r"C:\Users\pc-avni\Pictures\Avni\QPG v3.0 [IN PROGRESS]\config.toml")


def generate_list_of_qs(numberOfQsInPaper, listOfQuestions):
    nos_generated = {}
    qs_generated = []
    while len(nos_generated) < numberOfQsInPaper:
        v = random.randint(0, len(listOfQuestions) - 1)
        if nos_generated.get(v):
            continue
        else:
            nos_generated[v] = v
    for i in nos_generated.keys():
        qs_generated.append(listOfQuestions[i])
    return qs_generated


st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('<h1>Hello User! Welcome to <span class="text-primary">QPG</span><br><br></h1>', unsafe_allow_html=True)
st.markdown('<h3>Thank you for choosing us!</h3><h4>Choose categories in the given below dropdowns to generate your <span class="text-primary">personalised question paper.</span> Your question paper will be <span class="text-primary">saved</span> in your device and the location to it is given at the end. <br>Feel free to contact us at <span class="text-primary">qpgteam.amity@gmail.com </span> if you are having any difficulties. </h4><h3>Happy question paper generating!<br><br></h3>', unsafe_allow_html=True)


file_list = os.listdir("d://qpgDB")


subject = st.selectbox(
     'Choose Subject',
     file_list)

st.write('Your selection:', subject)
st.markdown('<br>', unsafe_allow_html=True)
subject_path = os.path.join("d://qpgDB//", subject)
#st.write(chapter_name)

chapter_list = os.listdir(subject_path)

if (subject == "Science"):

    segment_list = os.listdir(subject_path)
    folder_name = st.selectbox(
     'Choose segment',
     segment_list)
    subject_path = os.path.join(subject_path, folder_name)
    chapter_list = os.listdir(subject_path)

chapter_name = st.selectbox(
     'Choose Chapter',
     chapter_list)

st.write('Your selection:', chapter_name)

chapter_path= os.path.join(subject_path, chapter_name)
file_chapter_list = os.listdir(chapter_path)
#st.write(file_chapter_list)
#number_of_chapters = len(file_chapter_list)

#for c in file_chapter_list:
#    st.write(c, "\n")


#number_of_questions = len(chapter_name)
number_of_questions = len(file_chapter_list)
#st.write(number_of_questions)
qs_list = range(0, number_of_questions)
no_chosen = st.selectbox(
   'Choose number of questions',
   qs_list)
st.write('Your selection:', no_chosen)



if no_chosen>0:
  st.subheader('Sure! Here Is Your Question Paper!')
  st.write("--------------------------------------------------------------------------------------------")
  answer_file_text = open("QuestionPaper.txt", "w")

question_generated = generate_list_of_qs(no_chosen, file_chapter_list)

# st.write(question_generated)

q_no = 1
for file_name in question_generated:
    full_address = os.path.join(chapter_path, file_name)
    # folder_name + "/" + folder_chapter_name + "/" + file_name

    content = open(full_address, "r")

    q = 'Q' + str(q_no) + ": " + content.read()
    qWithStyle = '<div class="alert alert-primary" role="alert">' + q + '</div>'
    st.markdown(qWithStyle, unsafe_allow_html=True)
    answer_file_text.write(q)
    q_no = q_no + 1
    st.markdown("<div class=\"alert alert-success"
                "\" role=\"alert\">Ans:<br/><br/><br/></div>", unsafe_allow_html=True)
    answer_file_text.write("""
    Ans:








       """)



if no_chosen>0:
    answer_file_text.close()
    qp_path = os.path.join(os.getcwd(), answer_file_text.name)
    st.subheader("Question Paper saved in:")
    st.subheader(qp_path)
    st.balloons()