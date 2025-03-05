# GBot- Discord Bot

GBot is a Discord bot that utilizes the Gemini API to respond to user messages and manage reminders within a Discord server. Users can set, delete, and modify reminders by sending messages in a specific format.

## Features

- Message Responses: GBot can respond to user messages using the Gemini API.It can also initiate private chats

- Reminder Management: Users can create, delete, and modify reminders.Reminds on-time when the task is due.

- Flexible Reminder Format: Users can set reminders by sending messages with the date and time in a specific format.
- 
## Functions 
#### !help

- A command that provides a list of available commands and their descriptions.

- Sends an embedded message to the channel where the command was invoked.

#### !unloadGemini

- A command to unload the GeminiAgent cog from the bot.
- Restricted to a specific user (presumably the bot owner) using a check.

#### !reloadGemini

- A command to reload the GeminiAgent cog.
- Also restricted to a specific user.

#### !set_reminder

- A command to set a reminder.
- Takes a date and time string and a reminder text.


#### !delete_reminder

- A command to delete a reminder based on its text.
- Filters the reminders list to remove the specified reminder and confirms deletion.

#### !list_reminders

- A command to list all currently set reminders.
- Sends a message with the details of each reminder or indicates if no reminders are set.

### Background Tasks
#### check_reminders():
- A background task that runs every 60 seconds.
- Checks the current time against the stored reminders.
- If a reminder's time has been reached, it sends a message in the specified channel and removes the reminder from the list.

- I want to add more features in the future, such as the ability to create polls, voice and audio channels, automatically remove expired reminders, and AI-generated summaries. 

## Lessons Learned

I learnt how to create AI-powered responses for users by integrating Gemini Generative AI with Discord.


## 🚀 About Me
I'm a first year BTech CSE student passionate about technology, coding, and problem-solving. I’m currently exploring different programming languages, development tools, and working on beginner-level projects to enhance my skills.

