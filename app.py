from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv() ## load all the environment variables

##configure api key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load google gemi model and provide SQL query as response


def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt,question])
    return response.text



## function to retrieve query from the sql database


db_path= "datanerd.db"
def read_sql_query(sql,db_path):
    conn=sqlite3.connect(db_path)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


#Define prompt

prompt = """
You are an expert in converting English question to SQL query using mySQL syntax!
The SQL table's name is datanerd and has the following columns with their descriptions: 
company_name: is the name of the company, 
location: is where the job is,
job_platform: is the job board website where the job opening was posted, 
contract_type: what kind of contract they offer,
work_from_home: when it 'True' means they allow home office
salary: how much is the pay they offer, 
skills: a list of required skills for the position,
position_level: if the job is entry level senior staff manager etc
job_role: the job title,  
industry: what category of industry the job fall into healthcare technology finance etc,


Convert the questions asked into SQL query with mysql syntax,
use your knowledge of natural language to interpret the questions
And use your own knowledge of SQL to convert the questions correctly, this is very important
Use wildcards for filtering using Like, don't add data to the job_titles even if it is in the question
for example: data scientist use just scientist, data analyst just analyst and on
When using Limit always use the limit you want +1, if you want one use 2 if you want 2 use 3 
also the sql code should not have ``` in beginning or end and sql word in output
"""





#streamlit app
def main():
   

    st.set_page_config(page_title =" Talk to the DATANERD data and it will Answer")
    st.header("Talk to the DATANERD data and it will Answer")
    st.markdown("*powered by Gemini-Pro to retrieve SQL Data*")
    st.write("---")
    st.text('''The extract of the data we could access is mostly on data analyst jobs;
            because of the limited data the info provided here might not reflect the real info
            ''')
    st.text('the info here is not for profesional use or updated')
    st.text("If you asked questions about other roles you might or might not receive an answer")
    st.text("[Visit the datanerd original website](https://datanerd.tech/)")

    st.text("Ask questions like 'What is the most common job title?'")
    st.write("---")

    question = st.text_input("Input: ", key="input")

    submit= st.button("Submit the question")

    # ifsubmit is clicked,


    if submit:
        try:

            response=get_gemini_response(prompt, question)
            print(response)
            data=read_sql_query(response, db_path)

            st.subheader("the response is")
            for row in data:
                print(row)
                st.write(row)
            
            st.subheader(' SQL Code')
            st.code(response, language="SQL")
        except Exception as e:
            st.error('''I am sorry I could not get you an answer for that my data is 
                    limited to mainly data analyst jobs''')
            st.error("Rephrase or ask a different questions please")

if __name__=='__main__':
    main()
