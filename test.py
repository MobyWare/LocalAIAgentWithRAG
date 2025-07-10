#%%
from langchain_ollama.llms import OllamaLLM

#%%
llm = OllamaLLM(model="llama2")

#%%
response = llm.invoke("What are the top rated pizza restaurants in the Pittsburgh area?")
print(response)
# %%
