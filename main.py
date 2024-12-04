import streamlit as st
from utils.langchain_helper import CodeAssistant
from dotenv import load_dotenv
import os

load_dotenv()

##setup streamlit App
st.set_page_config(page_title="Multi-Language Code Assistant",page_icon="🦜")
st.title("Multi-Language Code Assistant")

##Sidebar for model selection
st.sidebar.subheader("Model Selection")
model_selected= st.sidebar.selectbox("Choose a model", ["Gemma2","Gemma","Llama3.2", "Llama3","Mistral"])

## initialize code assistant
groq_api_key=os.getenv('GROQ_API_KEY')
code_assistant= CodeAssistant(api_key=groq_api_key)
model_name=str(code_assistant.get_model(default_model=model_selected))
code_assistant.set_model(model_name=model_name)

## sidebar for task selection
st.sidebar.header("Features")
task= st.sidebar.selectbox(
    "Select Task",
    ["Generate code","Debug Code","Optimize Code","Explain Code","Refactor Code","Convert Code","Convert Code to Diagram","Generate Documentation"]
)
language_list= ["Python","Java","JavaScript","C++","C#","Go","TypeScript"]

## sidebar for programming language selection
language= st.sidebar.selectbox("Select Programming Language",language_list,key="language")

# Filter target languages dynamically


## download output
def download_output(result: str, task_name: str,):
    file_extension = "txt"
    file_name = f"{task_name.replace(' ', '_').lower()}.{file_extension}"
    st.download_button(
        label="Download Output",
        data=result,
        file_name=file_name,
        mime="text/plain",
    )

if task =="Generate code":
    st.subheader(f"Generate Code in {language}")
    description= st.text_area("Describe the code you want to generate:")
    if st.button("Generate Code"):
        with st.spinner(f"Generating {language} code..."):
             result = code_assistant.generate_code(description,language)
        st.success("Success!")
        st.code(result, language=language.lower())
        download_output(result, task)

elif task == "Debug Code":
    st.subheader(f"Debug {language} Code")
    code_snippet = st.text_area("Paste your code here:")
    if st.button("Debug Code"):
        with st.spinner(f"Debugging {language} code..."):
            result = code_assistant.debug_code(code_snippet, language)
        st.success("Code processed successfully!")
        st.text_area("Debugging Report:", result, height=300)
        download_output(result, task)

elif task == "Optimize Code":
    st.subheader(f"Optimize {language} Code")
    code_snippet = st.text_area("Paste your code here:")
    if st.button("Optimize Code"):
        with st.spinner(f"Optimizing {language} code..."):
            result = code_assistant.optimize_code(code_snippet, language)
        st.success("Code processed successfully!")
        st.text_area("Optimized Code:", result, height=300)
        download_output(result, task)

elif task == "Explain Code":
    st.subheader(f"Explain {language} Code")
    code_snippet = st.text_area("Paste your code here:")
    if st.button("Explain Code"):
        with st.spinner(f"Explaining {language} code..."):
            result = code_assistant.explain_code(code_snippet, language)
        st.success("Code processed successfully!")
        st.text_area("Code Explanation:", result, height=300)
        download_output(result, task)

elif task == "Convert Code to Diagram":
    st.subheader(f"Convert Code to Diagram")
    code_snippet = st.text_area("Paste your code here to convert into a diagram:")
    if st.button("Generate Diagram"):
        with st.spinner(f"Converting {language} code..."):
            flowchart_description  = code_assistant.convert_code_to_diagram(code_snippet, language)
        if flowchart_description.startswith("Error"):
            st.error(flowchart_description)
        else:
             st.success("Flowchart generated successfully!")
             st.subheader("Flowchart Description")
             st.code(flowchart_description, language="plaintext")
             st.subheader("ASCII Art Representation")
             ascii_art = code_assistant.generate_ascii_art_flowchart(flowchart_description)
             st.code(ascii_art)
             download_output(ascii_art, task)
   
elif task == "Generate Documentation":
    st.subheader(f"Generate Documentation for {language} Code")
    code_snippet = st.text_area("Paste your code here:")
    if st.button("Generate Documentaion"):
        with st.spinner(f"Processing {language} code..."):
            result = code_assistant.generate_documentation(code_snippet, language)
        st.success("Documentaion generated successfully!")
        st.text_area("Documentation:", result, height=600)
        download_output(result, task)
   
elif task == "Explain Errors":
    st.subheader(f"Explain Errors for {language} Code")
    code_snippet = st.text_area("Paste your code here:")
    if st.button("Explain Errors"):
        with st.spinner(f"Processing {language} code..."):
            result = code_assistant.explain_errors(code_snippet, language)
        st.success("Code processed successfully!")
        st.text_area("Analysis:", result, height=300)
        download_output(result, task)

elif task == "Refactor Code":
    st.subheader(f"Refactor Code for {language} Code")
    code_snippet = st.text_area("Paste your code here:")
    if st.button("Refactor Code"):
        with st.spinner(f"Refactoring {language} code..."):
            result = code_assistant.refactor_code(code_snippet, language)
        st.success("Code processed successfully!")
        st.text_area("Refactored code:", result, height=300)
        download_output(result, task)

elif task == "Convert Code":
    st.subheader("Convert Code from One Language to Another")
    code_snippet = st.text_area("Paste your code here:")
    # Select the target language
    st.text(f"Selected Source language: {language}")
    available_target_langs = [lang for lang in language_list if lang != language]
    print(available_target_langs)
    target_lang = st.selectbox("Target Language", available_target_langs, key="target_lang")
    if st.button("Convert Code"):
        with st.spinner(f"Converting code..."):
            result = code_assistant.convert_code(code_snippet, language, target_lang)
        st.success("Conversion Successful!")
        st.text_area("Converted code:", result,height=300)
        download_output(result, task)

else:
    st.error("Please provide input!")