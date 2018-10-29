class Record:
    def __init__(self, author, text):
        import datetime
        self.author = author
        self._text = text
        self.date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
        self.comments = list()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @text.getter
    def text(self):
        return self._text

    def addComment(self, comment):
        self.comments.append(comment)

    def show(self):      
        print("author: " + str(self.author))
        print("text: " + str(self._text))
        print("date: " + str(self.date))

    def showСomments(self):
        for comment in self.comments:
            comment.show()
        print()

class Comment(Record):
    def __init__(self, author, text):
        super(Comment, self).__init__(author=author, text=text)

firstRecord = Record('Stuklova Olya', 'Hello!')
firstRecord.addComment(Comment('Ivanova Anna', 'Hi!'))
firstRecord.addComment(Comment('Ivanova Anna', 'How are you?'))
print('Record')
firstRecord.show()
print('\n')
print('Comments')
firstRecord.showСomments()
