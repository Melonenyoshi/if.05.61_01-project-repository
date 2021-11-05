# Sea of Thieves Companion

## Introduction

We want to create a companion discord bot for the game "Sea of Thieves" which would allow the user to query the SOT (Sea of Thieves for short) [wiki](https://seaofthieves.fandom.com/wiki/Sea_of_Thieves_Wiki) for items, factions, missions, prizes, ressources, etc.. The bot would then process that query and output it's findings in a discord channel for everyone in the group to see.


## Initial Situation
Right now Sea of Thieves is a game where very few things get explained to. Basically the user have to figure everything out by themselves. This can be challgenging sometimes, so the internet helped with a fandom wiki. This helps alot, but has a few flaws:
* The user have to start their browser mid game, causing a lag spike and hurting the game experience.

* The Wiki Search tool is not really efficient as it gives the user way too much articels for one search attempt. 99% of the time the first article is the one the user is searching.
![](eyeofreach.png)
as shown in the example, the first article is the right one and the others are just cosmetic items and give no relevant, quick information about the weapon itself

* Most wiki pages contain a lot of unnesesary information

    * Example: 
    ![](ghostFleetWiki1.PNG)
    This is what the user gets when they search for informations about the ghost fleet - world event
    ![](ghostFleetWiki2.PNG)
    And for the relevant loot drop - information the user would have to scroll through half the article.
    which is not very efficient.
  
* Others in the group can not see the information the user just researched unless the user sends a link via a discord channel or some other means of communication.

## Problem
In Sea of Thieves the players objective is to be the fastest and the smartest in the battle. But sometimes the player lacks one small piece of information, that would be battledeciding. Looking it up in the wiki is very time inefficient as we saw before.

## By using a discord bot a lot of these flaws could be eliminated: 
* Users mostly play in groups and commmunicate via Discord. If users could research in that app they would not have to open a browser.
* A discord bot could handle quick researches very fast and eliminate all the time inefficiencies by giving the user the first search result in the wiki and trimming all unnecessary information away. 

* Because the bot outputs it's findings to a discord channel others in the group can easily view the information as well.
  

## General Conditions and Constraints

Using the bot has to be simpler and faster than the established procedure.
The ouptput has to be printed in a way in a way where the user can gather the information quicker than googling it.
![](slouch_hat.png)


## Project Objectives and System Concepts

* A user can query the wiki by inputting a command in a discord channel.
* The output is easily readable and formatted intuitively.
* The user can then by reacting to the output get further details.
  

## Opportunities and Risks

Opportunities:
* Looking something up will not break the user's immersion.
* Using the bot is much simpler and faster than the established procedure.
* We make an established bot for the community that everyone uses
* We take over the world
  
Risks:
* If it really takes off and we have the bot running on a small server, it will not be able to meet demand and will crash. Lots of downtime will cost alot of users. 
* If it really has alot of downtime we will rent a server that can handle demand. unfortunately we have no idea to finance that, other than out of our pockets


## Planning






### Milestones:
| Milestone                                                                    	| Status      	| Finish Date 	|
|------------------------------------------------------------------------------	|-------------	|-------------	|
| the project environment is set up and fully functional for all team members  	| Not Started 	|6.1.2022      	|
| the bot is running                                                           	| Not Started 	|10.2.2022     	|
| the bot can process querys and output basic description for searched article 	| Not Started 	|             	|
| the bot sends the image of an infotable                                      	| Not Started 	|             	|
| the users get further information by reacting to the bots message            	| Not Started 	|             	|
| the bot can dynamically integrate pictures into its messages                 	| Not Started 	|             	|

### Is there a Start Date?
January 2022
### Is there a End Date?
No, we dont have one yet.

### When does implementation work start?
It starts when we are done setting up our working environment.