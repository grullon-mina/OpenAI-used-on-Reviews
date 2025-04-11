import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Creates a bar graph that represents the classifications of different sentiments in a list.

    Args:
    A list of strings.

    Returns:
    A bar graph.
    """
    # create a dictionary containing the different classifications as keys, and occurences as values
    # set each key default value to 0
    
    sentiments_dic = {
        "positive": 0,
        "neutral": 0,
        "negative": 0,
        "irrelevant": 0
    }
    # loop over the list
    # if the current word matches one of the keys, increment that key's value
    for word in sentiments:
        sentiments_dic[word] += 1
    
    # make lists from the key and values and save to variables to use for plotting
    x_values = list(sentiments_dic.keys())
    y_values = list(sentiments_dic.values())

    # create the bar graph
    fig, ax = plt.subplots()

    ax.bar(x_values, y_values)
    ax.set_title("Sentiments of Reviews")
    
    fig.savefig("images/classifications.png")
