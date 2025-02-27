import fitz  # PyMuPDF
import nltk
from collections import Counter
from nltk.corpus import stopwords
import string

# Ensure NLTK stopwords are downloaded
nltk.download("stopwords")

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + " "
    return text

def clean_and_count_words(text):
    """Removes stopwords/punctuation and counts word frequency."""
    words = text.lower().split()
    words = [word.strip(string.punctuation) for word in words]
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words and word.isalpha()]
    return Counter(filtered_words).most_common(20)  # Get 20 most common words

# Example usage (replace with your actual PDF file)
pdf_file = "your_job_posting.pdf"
text = extract_text_from_pdf(pdf_file)
common_words = clean_and_count_words(text)

print("Most common keywords in job posting:")
for word, count in common_words:
    print(f"{word}: {count}")
