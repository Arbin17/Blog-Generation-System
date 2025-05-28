from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_blog_with_prompt(topic: str, research: str) -> str:
    prompt = f"""
    Write a blog on the topic: {topic}

    Heading: {topic}

    Introduction:
    Write a short and engaging introduction.

    Content:
    Use the following research:
    {research}

    Summary:
    Summarize the key points.
    """
    output = generator(prompt, max_length=512, do_sample=True)[0]['generated_text']
    return output
