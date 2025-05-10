from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="llama3-8b-8192")
prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader("cricket.txt",encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))
print(docs[0])
print(type(docs))

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))