"""
**Question N2:**
Write a function `extract_entities` that takes a text string and a list of entity keywords,
and returns a list of sentences that contain any of those keywords. This simulates basic
named entity recognition.

Example:
- Text: "Makerere University is in Kampala. Kampala is the capital of Uganda."
- Keywords: ["Makerere", "Kampala"]
- Should return: ["Makerere University is in Kampala.", "Kampala is the capital of Uganda."]
"""

def extract_entities(text, keywords):
    """
    Extract sentences containing specified keywords.

    Parameters:
    text (str): Input text string
    keywords (list): List of keywords to search for

    Returns:
    list: List of sentences containing the keywords
    """
    #Split the text into sentences using the period (.)
    sentences = text.split('.')
    matching_sentences = []

    for sentence in sentences:
      for keyword in keywords:
        if keyword in sentence.strip('.').split(' '):
          if sentence not in matching_sentences:
            matching_sentences.append(sentence)
          else:
            continue

    return matching_sentences

# Test the function
test_text = "DSA 2026 will be held at Makerere University in Kampala. Kampala is a beautiful city. Makerere University is one of the oldest universities in Africa."
keywords = ["Makerere", "Kampala", "DSA"]
result = extract_entities(test_text, keywords)
print(result)
