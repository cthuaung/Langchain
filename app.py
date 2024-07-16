from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAI


template = "You are a naming consultant for new companies. What is a good name for a {company} that make {product}"
prompt = PromptTemplate.from_template(template)
llm = OpenAI(temperature=0.9)

chain = prompt | llm

print("Test:",prompt.format(company="VAV Startup", product="colorful socks"))

result = chain.invoke({"company":"VAV Startup","product":"Colourful socks"})
print(result)
