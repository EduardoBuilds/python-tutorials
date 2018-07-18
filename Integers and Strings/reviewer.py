outputText = """Yesterday I went to see {0}.
To be honest, I thought it was pretty good.
It's a good effort by {1}.
I hadn't seen a plot move quite as fluidly as it did in {0},
but {1} does have a good hand for it."""


print('What movie are we reviewing')
movie = input().title()

print('And who directs it?')
director = input().title()


print( outputText.format(movie,director) )


