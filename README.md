# fall22finalpreposal
Video URL: https://temple.zoom.us/rec/share/bcJj2D14L3rFG1Ns1zg27WP5NthFjFPGEw98iF3N7mPdlw9mn-8d21kcvRGPXe2o.dRH8IHXXfF0Hpb0m

I feel incredibly proud to say I accomplished all I set out to do with this project. I had 3 main difficulties that I worked through as I went through the project, but all ended up solved in the end.

Difficulty 1: .env File
The first difficulty I had was in setting up a .env file. While it turns out it's a pretty simple concept- a plain text file to safely store your sensitive information in variables- it was kind of difficult to find an article online that fully explained what it was and how to make it. I ended up making it right but messed up the file path by working on a python file in the wrong folder, so once I moved it to the right place everything worked fine.

Difficulty 2: Message Content Permissions
The main articles I was following to set up the bot were out of date, and since their publications Discord has added security for permissions and intents. My bot was recognizing that messages were being sent in chat but reading them as empty strings, so I concluded I must not have set permissions right. I needed to turn on intents in the Discord developer portal and set the intents I wanted in my code as well, as default intents do not allow reading of message content.

Difficulty 3: Command Response
The last main difficulty I had was in getting my bot to respond to commands. Once I fixed the intents, the bot could read the messages fine, but even though my syntax to set up the commands was correct none of them were triggering. The issue I found was that since i had an on_message event defined, it would only apply the on_message code and not check to see if the message was a command. To fix this I had to add a line stating "await bot.process_commands(message)" at the end of the on_message block.

Hitting these roadblocks was frustrating and took a lot of research and trial and error to solve but I am proud of myself for sticking with it and creating a bot that works the way I intended it to. Maybe next I'll hook it up to a raspberry pi so my friends and I can use the bot without me running the code on my computer!

Another part I feel proud of myself for is the errors I handled to send a specific error message depending on the scenario. The different messages really give the bot a more complete and polished feel.
