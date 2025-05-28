from duckduckgo_search import DDGS
def duckduckgo_search(query: str, max_results=5):
    results_text = []
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results)
        for r in results:
            if "body" in r:
                results_text.append(r["body"])
            elif "title" in r:
                results_text.append(r["title"])
    return "\n".join(results_text)
