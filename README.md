# Comply VAT & Tax Query Assistant

A Python script that leverages **LangChain** and **Google Gemini AI** to answer tax-related questions based on a DOCX document of country-specific filing obligations.  

This project allows users to ask questions like "Is VAT return available in Comply for Australia?" and get accurate answers extracted from the document.

---

## 🔹 Features

- Loads tax/filing documents from `.docx` files.
- Uses **Google Gemini AI (Gemini 3 Flash)** for natural language understanding.
- Supports country-specific tax queries.
- Outputs clear, detailed answers directly in the terminal.
- Can be extended to multiple questions in a session.
🔹 Usage

Make sure your tax DOCX file is in the data/ folder.

Run the script:

python app.py


Enter the requested information in the terminal:

Enter your country: Australia
Enter your question: Do VAT return available in Comply?


Get the AI-generated answer from the document.

🔹 Example Output
Loaded 1 document(s)
Enter your country: Australia
Enter your question: Do VAT return available in Comply?

Answer: Based on the document provided, the VAT return (specifically the GST component of the Business Activity Statement - BAS) is available in Comply for Australia.
