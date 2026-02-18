import os
from dotenv import load_dotenv
from langchain_community.document_loaders import Docx2txtLoader
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

loader = Docx2txtLoader("data/CountryFilingObligationssupportedinComply (1) (2).docx")
documents = loader.load()
print(f"Loaded {len(documents)} document(s)")

document_text = "\n\n".join([doc.page_content for doc in documents])

country = input("Enter your country: ")
question = input("Enter your question: ")

prompt = f"""
You are a tax expert. Answer the question based only on the document below.

Document:
{document_text}

Country: {country}
Question: {question}
"""
response = llm.invoke(prompt) 

content = response.content
if isinstance(content, list):
    answer = "".join(part["text"] for part in content if part.get("type") == "text")
else:
    answer = content
print("\nAnswer:", answer)


