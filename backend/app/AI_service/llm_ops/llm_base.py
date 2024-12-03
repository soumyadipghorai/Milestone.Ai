from dotenv import main
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain.memory import ChatMessageHistory
import os 
import logging 
import json 

_ = main.load_dotenv(main.find_dotenv())
api_key, llama_model = os.getenv("GROQ_API_KEY"), os.getenv("GROQ_LLama")

class LLMBase : 
    def __init__(
            self, prompt, schema, debug: bool = False, save_history: bool = False, 
            total_history: int = 10, temperature: float = 0.0, summarize: bool = False) : 
        self.schema = schema
        self.prompt = prompt
        self.debug = debug 
        self.save_history = save_history
        self.total_history = total_history
        self.temperature = temperature
        self.summarize = summarize 
        self.llm = ChatGroq(temperature=self.temperature, model=llama_model, api_key=api_key)
        self.memory = ChatMessageHistory() if self.save_history else None 

    def summarize_text(self, text, prompt: str = "Summarize the following text briefly within 200 words"):
        self.llm.temperature = 0.5
        messages = [
            ("system", prompt), ("human", text),
        ]
        ai_msg = self.llm.invoke(messages)
        return ai_msg.content 

    def generate_output(self, **kwargs) : 
        parser = JsonOutputParser(pydantic_object = self.schema)

        if self.save_history : 
            history = self.memory.messages[-self.total_history:]
            print("history_prompt --> ", history)
        
        input_prompt = self.prompt.format(
            format_instructions = parser.get_format_instructions(), **kwargs
        )

        structured_llm = self.llm.with_structured_output(self.schema, method="json_mode")
        output = structured_llm.invoke(input_prompt) 


        if self.debug :
            logging.info(output)
            logging.debug(type(output))

        structured_output = output.model_dump()

        # ? adding tag for filtering history 
        if self.save_history : 
            tag = kwargs.get('tag', None)
            if tag : structured_output["tag"] = tag
            if self.summarize : 
                self.memory.add_ai_message(self.summarize_text(str(structured_output)))
            else : 
                self.memory.add_ai_message(json.dumps(structured_output))

        return structured_output 