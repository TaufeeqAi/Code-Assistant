from langchain_groq import ChatGroq
from .prompts import prompts 
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class CodeAssistant:
    def __init__(self,api_key):
        self.llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=api_key,)

    def get_model(self,default_model):
        if default_model == "Llama3.2":
            model_name="llama-3.2-90b-vision-preview"
            return model_name
        elif default_model == "Gemma2":
            model_name="Gemma2-9b-It"
            return model_name
        elif default_model == "Gemma":
            model_name="Gemma-7b-It"
            return model_name
        elif default_model == "Llama3":
            model_name="Llama3-70b-8192"
            return model_name
        elif default_model == "Mistral":
            model_name="Mixtral-8x7b-32768"
            return model_name

    def set_model(self, model_name):
        self.llm = ChatGroq(model_name=model_name, temperature=0.7)

    def _get_combined_prompt(self, task_prompt):
        return ChatPromptTemplate.from_messages(
            [prompts["system_prompt"], task_prompt]
        )

    def generate_code(self,description,language):
        """Generate code in the specified language"""
        combined_prompt = self._get_combined_prompt(prompts["generate_code_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"description": description, "language":language})
    
    def debug_code(self,code_snippet,language):
        """Debug code in the specified language  """
        combined_prompt = self._get_combined_prompt(prompts["debug_code_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"code_snippet":code_snippet,"language":language})
    
    def optimize_code(self, code_snippet, language):
        """Optmize code in the specified language """
        combined_prompt = self._get_combined_prompt(prompts["optimize_code_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"code_snippet":code_snippet,"language":language})
    
    def explain_code(self, code_snippet, language):
        """Explain the code in the specified language."""
        combined_prompt = self._get_combined_prompt(prompts["explain_code_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"code_snippet": code_snippet, "language": language})
    
    def generate_documentation(self, code: str, language: str) -> str:
        """
        Generate documentation for the provided code.
        """
        combined_prompt = self._get_combined_prompt(prompts["generate_documentation_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"code": code, "language": language})
    
    def convert_code(self, code_snippet, source_lang, target_lang) -> str:

        combined_prompt = self._get_combined_prompt(prompts["convert_code_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"code_snippet": code_snippet, "source_lang": source_lang,"target_lang":target_lang})

    def refactor_code(self, code: str, language: str) -> str:
        combined_prompt = self._get_combined_prompt(prompts["refactor_code_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"code": code, "language": language})
    
    def convert_code_to_diagram(self, code:str,language:str):
        combined_prompt = self._get_combined_prompt(prompts["code_to_diagram_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"code": code, "language":language}).strip()
    
    def generate_ascii_art_flowchart(self, flowchart_description: str) -> str:
        combined_prompt = self._get_combined_prompt(prompts["diagram_ascii_prompt"])
        output_parser=StrOutputParser()
        chain=combined_prompt|self.llm|output_parser
        return chain.invoke({"flowchart_description": flowchart_description}).strip()
    

