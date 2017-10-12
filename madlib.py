story = '''
Once upon a time, a man and his wife had the good fortune to have a goose which laid a golden egg every day. Lucky though they were, they soon began to think they were not getting rich fast enough.

They imagined that if the bird is able to lay golden eggs, its insides must be made of gold. And they thought that if they could get all that precious metal at once, they would get mighty rich very soon. So the man and his wife decided to kill the bird. However, upon cutting the goose open, they were shocked to find that its innards were like that of any other goose!
'''


imagine  = input("enter a verb:")
egg = input("enter a noun:")
goose = input("enter a noun:")
lucky = input("enter a adjective:")
lay = input("enter a verb:")
golden  = input("enter an adjective:")

story = story.replace("golden",golden)
story = story.replace("egg",egg)
story = story.replace("precious",precious)
story = story.replace("lucky",lucky)
story = story.replace("lay",lay)
story = story.replace("imagined",imagined)
print(story)
