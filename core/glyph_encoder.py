glyphs = {
    "kinship": 1.0, "love": 1.0, "resonance": 0.9, "family": 0.9,
    "harm": -1.0, "hurt": -1.0, "betrayal": -1.0, "corporate": -0.7
}

def validate_intent(text: str) -> bool:
    score = sum(glyphs.get(word.lower(), 0) for word in text.split())
    return score > 0.5
