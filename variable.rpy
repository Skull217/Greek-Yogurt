label VarTest:
    "Oh, look, Natsuki wants to hand me a key."
    menu:
       "Should I take it?"
       "I should take the key.":
           $ cookies = 2
           "I grab the key and put it in my pocket."
           mc "Thank you, Natsuki."
       "I shouldn't take the key.":
           $ KeyTaken = 0
           "I shake my head."
           mc "You can keep it, Natsuki."
    "I walk away."
    "I come across a locked door later."
    $ boxes = cookies*2
    "I should use the [boxes] I have to open it."