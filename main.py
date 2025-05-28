from tools.wikipedia_tool import wikipedia_search
from tools.web_search_tool import duckduckgo_search
from generator.blog_writer import generate_blog_with_prompt

def generate_blog(topic: str):
    print(f"🔍 Researching topic: {topic}")
    wiki_data = wikipedia_search(topic)
    web_data = duckduckgo_search(topic)
    combined_research = f"{wiki_data}\n\nAdditional Info:\n{web_data}"
    
    print("✍️ Generating blog...\n")
    blog = generate_blog_with_prompt(topic, combined_research)
    print(blog)

if __name__ == "__main__":
    topic = input("Enter your blog topic: ")
    generate_blog(topic)
