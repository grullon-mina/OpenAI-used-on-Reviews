from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    INSERT DOCSTRING HERE
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
