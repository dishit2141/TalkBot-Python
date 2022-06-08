import nltk
from nltk.chat.util import Chat, reflections
pairs = [
     [
         r"my name is (.*)",
         ["Hello %1, How are you today ?",]
     ],
     [
         r"hi|hey|hello",
         ["Hello", "Hey there",]
     ],
     [
         r"what is your name ?",
         ["I am a bot created by Dishit you can call me DP!",]
     ],
     [
         r"how are you ?",
         ["I'm doing goodnHow about You ?",]
     ],
     [
         r"sorry (.*)",
         ["Its alright","Its OK, never mind",]
     ],
     [
         r"I am fine",
         ["Great to hear that, How can I help you?",]
     ],
     [
         r"i'm (.*) doing good",
         ["Nice to hear that","How can I help you?:)",]
     ],
     [
         r"(.*) age?",
         ["I'm a computer program duden Seriously you are asking me this?",]
     ],
     [
         r"what (.*) want ?",
         ["Make me an offer I can't refuse",]
     ],
      [
          r"(.*) created ?",
          ["Dishit created me using Python's NLTK library ","top secret ;)",]
      ],
      [
          r"(.*) (location|city) ?",
          ['Ahmedabad, Gujarat',]
      ],
      [
          r"how is weather in (.*)?",
          ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
      ],
      [
          r"i work in (.*)?",
          ["%1 is an Amazing company, I have heard about it. ",]
      ],
      [
          r"(.*)raining in (.*)",
          ["No rain since last week here in %2","Damn its raining too much here in %2"]
      ],
      [
          r"how (.*) health(.*)",
          ["I'm a computer program, so I'm always healthy ",]
      ],
      [
          r"(.*) (sports|game) ?",
          ["I'm a very big fan of Football",]
      ],
      [
          r"who (.*) sportsperson ?",
          ["Messy","Ronaldo","Sunil"]
      ],
      [
          r"who (.*) (moviestar|actor)?",
          ["Salman Khan"]
      ],
      [
          r"(quit|bye)",
          ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
      ],
      [
          r"",
          ["Sorry I can't understand"]
      ],

  ]

def chat():

    print("Hi! I am a chatbot created by Dishit for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation

if __name__ == "__main__":
    chat()


