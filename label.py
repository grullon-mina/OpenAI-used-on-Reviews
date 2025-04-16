from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    Analyzes a list of customer reviews and classifies them as either positive, negative, neutral or irrelevant.

    Args:
    A list of strings.

    Returns:
    A list of strings.

    """
    # protects code if you receive an empty list
    if len(text) == 0:
        return "Wrong input. text must be an array of strings."
    # if you get the wrong data type --> check if the data type is a string using type()
    # if not a string, return "Wrong input. text must be an array of strings."
    if not isinstance(text[0], str):
         return "Wrong input. text must be an array of strings."
    
    system_prompt = """
    It is May. You are highly skilled in recognizing and interpreting sentiment from people of all cultural backgrounds. You know how to analyze customer reviews and classify them as positive, negative, neutral, or irrelevant based on your knowledge. You use tone, keywords and context to draw your conclusions. If a review has mixed sentiments, use the sentiment that is dominant.
    Positive: A review that expresses satisfaction with the product/service.
        Example: "I absolutely love this product! It works perfectly and exceeded my expectations."
                 "Great customer service! They resolved my issue quickly."
    Negative: A review that expresses complaints and dissatisfaction of the product/service.
        Example: "This is the worst purchase I've made. It broke within a week."
                 "Terrible experience. The support team never responded to my issue."
    Irrelevant: A review that is off-topic, nonsensical, or does not provide any meaningful feedback.
        Example: "I like pizza more than this."
                 "asdfjkl; amazing!"
                 "Check out my YouTube channel for cool content!"

    
    """

    prompt = f"""
    Can you please analyze a list of reviews? Thank you.
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.
    
    Return only a list with exactly one word per review, in the same order.
    Do not include explanations, numbering, or additional comments. 
    Use only a one-word response per line. Do not include any numbers. 
    {text}
    """
    client = OpenAI()
    #print(len(text))
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    output = completion.choices[0].message.content.strip().splitlines()

    output_list = []

    for item in output:
        output_list.append(item.strip())

    #print(len(output_list))
    
    return output_list
    
