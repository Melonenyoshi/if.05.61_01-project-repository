# Sea of Thieves Companion

## Introduction

We want to create a companion discord bot for the game "Sea of Thieves" which would allow the user to query the SOT (Sea of Thieves for short) [wiki](https://seaofthieves.fandom.com/wiki/Sea_of_Thieves_Wiki) for items, factions, missions, prizes, ressources, etc.. The bot would then process that query and output it's findings in a discord channel for everyone in the group to see.


## Initial Situation

Right now you would have to start your browser midgame, google the wiki, search for whatever you're looking for in the wiki and then hope for the best. This procedure has a few flaws: 

* Opening the browser midgame not only takes a lot of time but also consumes a lot of processing ressources and will lead to a big lagspike, hurting the users gaming experience.
  
* Others in the group can't see the information the user just researched unless the user sends a link via a discord channel or some other means of communication.


By using a discord bot a lot of these flaws could be eliminated: 

* Users usually already communicate via discord, meaning they wouldn't need to open another application and therefore avoiding a lagspike. Furthermore alt-tabbing to discord and then quickly entering a command like "/q Ashen Key" is much quicker than undergoing the exhausting procedure described above.
  
* Because the bot outputs it's findings to a discord channel others in the group can easily view the information as well.
  

## General Conditions and Constraints

Using the bot has to be simpler and faster than the established procedure. We weren't able to identify any constraints.


## Project Objectives and System Concepts

* A user can query the wiki by inputting a command in a discord channel.
* The output is easily readable and formatted intuitively.
* The user can then by reacting to the output get further details.
  

## Opportunities and Risks

Opportunities:
* Looking something up won't break the user's immersion.
* Using the bot is much simpler and faster than the established procedure.
  
We weren't able to identify any risks.


## Planning

### Milestones:
1. The project environment is set up and fully functional for all team members
2. The bot is running
3. The bot can process querys and output a basic description of the found article
4. The bot also sends an image of the infotable
5. The users can get further information by reacting to the bot's message
6. The bot sends screenshots of tables when appropriate
7. The bot can dynamically integrate images into it's answer

### Is there a Start Date?
No, we dont have one yet.

### Is there a End Date?
No, we dont have one yet.

### When does implementation work start?
It starts when we are done setting up our working environment.