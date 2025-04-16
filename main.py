from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Creates a bar graph analyzing reviews given a json data file and classifys them as positive, negative, neutral, or irrelevant.

    Args:
    A json file.

    Returns:
    A list of sentiments.
    """
    # open the json object
    with open(filepath) as j:
        obj = json.load(j)
    
    # extract the reviews from the json file
    results = obj['results']

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(results)
    
    # plot a visualization expressing sentiment ratio
    visualization = make_plot(sentiments)

    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
