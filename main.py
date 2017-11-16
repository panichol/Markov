## A program written for CS@Mines by Patrick Nichols
## It contains a Markov generator trained on various peices of text
## With a GUI Wrapper for ease-of-use

from Markov import MarkovMap
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        ## Uncomment when you actually want to run
        ## Building the maps takes about thirty seconds
        self.bibleMap = MarkovMap("Data/Bible.txt",order = 7)
        self.aliceMap = MarkovMap("Data/Alice.txt",order = 7)
        self.republicMap = MarkovMap("Data/Republic.txt", order = 8)
        self.warMap = MarkovMap("Data/War.txt", order = 7)

        self.outputMessage = tk.StringVar()
        
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.output = tk.Label(self,
                               wraplength = 1000,
                               text = "HELP",
                               font = ("Courier",16))
        self.output.pack(side = "bottom")

        self.help = tk.Button(self)
        self.help["text"] = "Click me for help"
        self.help["command"] = self.getHelp
        self.help.pack(side = "top")

        self.alice = tk.Button(self)
        self.alice["text"] = "Alice in Wonderland by Lewis Carol"
        self.alice["command"] = self.alicePressed
        self.alice.pack(side="top")
        
        self.bible = tk.Button(self)
        self.bible["text"] = "The Bible (King James version)"
        self.bible["command"] = self.biblePressed
        self.bible.pack(side="top")
        
        self.republic = tk.Button(self)
        self.republic["text"] = "The Republic by Plato"
        self.republic["command"] = self.republicPressed
        self.republic.pack(side="top")

        self.war = tk.Button(self)
        self.war["text"] = "The Art of War by Sun Tzu"
        self.war["command"] = self.warPressed
        self.war.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        self.output.config(text = "Press a button to randomly generate text based on that book!")

    def getHelp(self):
        self.output.config(text = """
        Thanks for coming to Mines!

        This program randomly generates text based off of certain books.
        Simply click any of the book titles and this text should be replaced
        with about a paragraph of text in the style of that book.

        If you want to know more about how this program works, feel free to
        ask one of the students at this booth!

        """)

    def alicePressed(self):
        try:
            self.output.config(text = self.aliceMap.Generate(1000))
        except TypeError:
            self.alicePressed()
            
    def warPressed(self):
        self.output.config(text = self.warMap.Generate(1000))
        
    def biblePressed(self):
        self.output.config(text = self.bibleMap.Generate(1000))
        
    def republicPressed(self):
        self.output.config(text = self.republicMap.Generate(1000))

root = tk.Tk(screenName = "CS@Mines")
app = Application(master=root)
app.mainloop()

