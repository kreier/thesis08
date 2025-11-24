from pdfminer.high_level import extract_text

# Extract text from PDF
text = extract_text("20080124.pdf")

# Save to Diplomarbeit.txt
with open("Diplomarbeit.txt", "w", encoding="utf-8") as f:
    f.write(text)
