# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# import all methods and classes from the tkinter
from tkinter import *


# Function for clearing the contents of all entry boxes and text area.
def clearAll():
    # deleting the content from the entry box
    negativeField.delete(0, END)
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    overallField.delete(0, END)
    quoteField.delete(0, END)

    # whole content of text area  is deleted
    textArea.delete(1.0, END)


# function to print sentiments of the sentence.
def detect_sentiment():
    # get a whole input content from text box
    sentence = textArea.get("1.0", "end")

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    string = str(sentiment_dict['neg'] * 100) + "% Negative"
    negativeField.insert(10, string)

    string = str(sentiment_dict['neu'] * 100) + "% Neutral"
    neutralField.insert(10, string)

    string = str(sentiment_dict['pos'] * 100) + "% Positive"
    positiveField.insert(10, string)

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        string = "Positive!!"
        quoteField.insert(10, "You're doing Great!!")
    elif sentiment_dict['compound'] <= - 0.05:
        string = "Negative!!"
        quoteField.insert(10, "Don't worry!! You'll be fine.")
    else:
        string = "Neutral!!"
        quoteField.insert(10, "You can have some fun once in a while!")

    overallField.insert(10, string)


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background="light blue")

    # set the name of tkinter GUI window
    gui.title("How you doin? - Sentiment Analysis App")

    # Set the configuration of GUI window
    gui.geometry("600x600")

    # create a label : Enter Your Task
    enterTitle = Label(gui, text="Analysing your texts", bg="light pink")

    # create a label : Enter Your Task
    enterText = Label(gui, text="How have you been?", bg="light pink")

    # create a text area for the root
    # with lucida 13 font
    # text area is for writing the content
    textArea = Text(gui, height=5, width=25, font="lucida 13")

    # create a Submit Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed
    check = Button(gui, text="Check Sentiment", fg="Black", bg="light yellow", command=detect_sentiment)

    # Create a negative : label
    negative = Label(gui, text="You seem to be: ", bg="light blue")

    # Create a neutral : label
    neutral = Label(gui, text="You seem to be: ", bg="light blue")

    # Create a positive : label
    positive = Label(gui, text="You seem to be: ", bg="light blue")

    # Create a overall : label
    overall = Label(gui, text="But you are: ", bg="light blue")

    # create a text entry box
    negativeField = Entry(gui, justify='center')

    # create a text entry box
    neutralField = Entry(gui, justify='center')

    # create a text entry box
    positiveField = Entry(gui, justify='center')

    # create a text entry box
    overallField = Entry(gui, justify='center')

    # create a text entry box
    quoteField = Entry(gui, justify='center')

    # create a Clear Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed .
    clear = Button(gui, text="Clear", fg="Black", bg="light yellow", command=clearAll)

    # create a Exit Button and place into the root window
    # when user press the button, the command or
    # function affiliated to that button is executed .
    Exit = Button(gui, text="Exit", fg="Black", bg="light yellow", command=exit)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.

    enterTitle.grid(row=0, column=2, pady=10, padx=20)

    enterText.grid(row=1, column=3, pady=10)

    textArea.grid(row=2, column=3, padx=10, sticky=W)

    check.grid(row=3, column=3, pady=10)

    negative.grid(row=4, column=3)

    neutral.grid(row=6, column=3)

    positive.grid(row=8, column=3)

    overall.grid(row=10, column=3)

    negativeField.grid(row=5, column=3, ipadx=10, ipady=2.5)

    neutralField.grid(row=7, column=3, ipadx=10, ipady=2.5)

    positiveField.grid(row=9, column=3, ipadx=10, ipady=2.5)

    overallField.grid(row=11, column=3, ipadx=10, ipady=10, pady=5)

    quoteField.grid(row=13, column=3, ipadx=60, ipady=25, padx=5, pady=5)

    clear.grid(row=16, column=3, padx=5, pady=5)

    Exit.grid(row=17, column=3, padx=5, pady=5)

    # start the GUI
    gui.mainloop()
