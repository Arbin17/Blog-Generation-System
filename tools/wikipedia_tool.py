import wikipedia

def wikipedia_search(topic: str) -> str:
    try:
        summary = wikipedia.summary(topic, sentences=5)
    except wikipedia.DisambiguationError as e:
        summary = f"Topic is ambiguous. Suggestions: {e.options[:5]}"
    except Exception as e:
        summary = f"Error fetching from Wikipedia: {str(e)}"
    return summary
