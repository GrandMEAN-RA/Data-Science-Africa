"""
## Natural Language Processing and Large Language Models
**Question N1:**
Write a function `count_words` that takes a text string as input and returns a dictionary
where keys are unique words (lowercased) and values are their frequencies. Ignore punctuation
and split on whitespace.

Example: `count_words("Hello world hello")` should return `{'hello': 2, 'world': 1}`
"""

def count_words(text):
    """
    Count word frequencies in a text string.

    Parameters:
    text (str): Input text string

    Returns:
    dict: Dictionary with words as keys and frequencies as values
    """
    words = text.lower().split(' ')
    word_counts = {}
    seen = []
    for w in words:
      for p in ['.',',','"',"'"]:
        w = w.strip(p)
      if w in seen:
        word_counts[w] += 1
      else:
        word_counts[w] = 1
        seen.append(w)

    return word_counts

# Test the function
test_text = "Data Science Africa 2026 is happening in Kampala at Makerere University. Makerere University, is' a great place for learning."
result = count_words(test_text)
print(result)

