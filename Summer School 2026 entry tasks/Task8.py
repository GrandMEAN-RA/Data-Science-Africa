"""
**Question N3:**
Write a function `calculate_similarity` that takes two text strings and calculates
their similarity based on the Jaccard similarity of their word sets. Jaccard similarity
is the size of the intersection divided by the size of the union of two sets.

Formula: J(A, B) = |A ∩ B| / |A ∪ B|

Example:
- Text1: "data science africa"
- Text2: "data science kampala"
- Should return approximately 0.67 (2 common words / 3 unique words)
"""

def calculate_similarity(text1, text2):
    """
    Calculate Jaccard similarity between two text strings.

    Parameters:
    text1 (str): First text string
    text2 (str): Second text string

    Returns:
    float: Jaccard similarity score between 0 and 1
    """

    def clean_word(text):
      cleaned = []
      for w in text:
        for p in ['.',',','"',"'"]:
          w = w.strip(p)
          cleaned.append(w)
      return cleaned

    set1 = text1.lower().split(' ')
    cset1 = clean_word(set1)
    set2 = text2.lower().split(' ')
    cset2 = clean_word(set2)

    intersection = set(cset1) & set(cset2)
    print('intersection:',intersection)

    union = set(cset1).union(set(cset2))
    print('union:',union)

    similarity = len(intersection)/len(union)

    return similarity

# Test the function
text1 = "Data Science Africa 2026 Kampala Makerere University"
text2 = "Data Science Africa Kampala Makerere"
similarity = calculate_similarity(text1, text2)
print(f"Similarity: {similarity:.4f}")
