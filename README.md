# Predicting Board Game Complexity
## By Q Leedham

# Problem Statement
With platforms like Kickstarter, anyone with an idea can easily make and produce a board game on their own. But while it's easy to produce a game, it's hard to know how how complicated the game will be for players. There is a complexity, or weight, rating on [Board Game Geek](http://boardgamegeek.com), though it relies on community voting. Is it possible to predict that rating knowing what a creator would know at the start of their project? 

Is there a correlation between the mechanics and features of a board game and the game's complexity rating, or weight, on Board Game Geek?

I will use classification models for the project and judge them by their accuracy.

## Data Dictionary

|Feature|Type|Description|
|---|---|---|
|name|Object|The title of the board game|
|yearpublished|Int|The year the game was published|
|minplayers|Int|The minimum number of players required to play the game|
|maxplayers|Int|The maximum number of players who can play the game|
|minplaytime|Int|The average minimum amount of time needed to play the game|
|maxplaytime|Int|The average maximum amount of time needed to play the game|
|minage|Int|The recommended minmum age of players|
|languagedependence|Int|On a scale of 1 to 5, how dependent on language the game is (for example, how much text is on each card)|
|boardgamecategory_cnt|Int|The number of categories the game belongs in|
|boardgamemechanic_cnt|Int|The number of mechanics a game has|
|boardgamecategory|Object|A list of the categories the game belongs in|
|boardgamemechanic|Object|A list of mechanics the board game has|
|description|Object|The written description of the game|
|avgweight|Int|Target. The weight, or complexity rating, of the game|


# Executive Summary
The goal of this project is to determine if there is a correlation between a board game's mechanics, the category of the game, and stats such as the minimum number of players or language dependency and the game's complexity, or weight, on Board Game Geek. The idea is to make it possible for designers to predict how complex their board game is for players when they're still early on in the development process. Even in play testing it can be hard to know how complicated players will find a game when the designer isn't sitting with them explaining how to play it.

The data for this project was found on Kaggle, and contained information for 20,000 games listed on Board Game Geek. The full data dictionary for the comeplete data can be found [here](https://www.kaggle.com/extralime/20000-boardgames-dataset), while the data dictionary above contains all the features I used in this project.

A base model for this project would be about 44% accurate if it just guessed medium light complexity for all games in the dataset. Using a Voting Classifier model I was able to find a model that is 66% accurate. Overall, there was not as much correlation between the mechanics or categories of a game and its complexity. The models did produce some interesting results in terms of their coefficients, however.

![light complexity chart](/images/light-complexity.png)

I found that mature or adult games were most likely to be lightly complex, or the simplest of all the classes in the dataset. This is likely because these games are made to be played in more social settings where players may be impaired or are otherwise not focused entirely on the game at hand. Games like Cards Against Humanity are a good example of this, where the goal of the game is simply to make the best somewhat-offensive, somewhat-adult jokes with the cards given.

![heavy complexity chart](/images/heavy-complexity.png)

Through the project I also found that, unsurprisingly, war games are among the most complex games available. This makes sense as many war games involve complicated math for combat and complicated rules for how to move individual units. That's on top of a large number of rulebooks, expansions, and miniatures that players need to buy, and in the case of the miniatures, paint, in order to play those games.

# Conclusion
While there is some correlation between the mechanics and categories of board games and their complexity, there isn't enough of a correlation to have a significantly accurate model. Even the best model I was able to build only had an accuracy of about 66%. Information that seemed like it might have a big impact on the reults like the suggested minimum age of players or the language dependency of the game didn't seem to have much of an impact on the accuracy of the models. My idea that these things would make it easy for a designer to find out how complex a game they're designing is didn't work out as planned.

It turns out there's much more to a board game's complexity than just the easily quantifiable stats about them. Board Game Geek's website suggests that the weight rating can include things like the amount of luck involved in a game, how much technical skill is involved, or how thick or complex is the rulebook. These are qualites that aren't easily quantifiable, or are at least not easily obtained without surveying players for each game.

# Recommendations
Given more compute power, I would be interested in doing natural language processing on the description of board games and add it to the model, to see how that impacts the results. I tried to do that as part of this project, but the models ended up taking up far too much memory and ultimately crashed my computer. It might even be interesting to use just natural language processing on the descriptions with nothing else to see how that impacts the results. It could be that descriptions are better at predicting the complexity.

It would also be interested to somehow obtain more data about each board game like the number of pieces or the length of the rulebook to see how that impacts the weight rating.

Another possible idea would be to use image recognition on images of a game board to see if that can impact complexity. Veteran board game players can typically tell how complicated a board game is going to be by just looking at the board, and it'd be interested to see if a nueral network can be trained to do the same thing.