DATABASE_PATH = 'stats.db'

ROLES: list[str] = []

# Configuration
ONLINE_ROLE_NAME = "🎮 Online"
ROLES.append(ONLINE_ROLE_NAME)
WHITELIST_ROLE_ID = 1296844924892872725
ROLES.append(WHITELIST_ROLE_ID)

# PROD Id's
WEBHOOK_CHANNEL_ID = 1291111515977551892
MOD_ROLE_ID = 1222930361848303736
SCOREBOARD_CHANNEL_ID = 1343755601070657566
LOG_CHANNEL_ID = 1347641109773287444
WEEKLY_RANKINGS_CHANNEL_ID = 1349557854213898322

# Role IDs for achievements and deaths
MOST_DEATHS_ROLE = "💀 Skill Issue"
ROLES.append(MOST_DEATHS_ROLE)

LEAST_DEATHS_ROLE = "👷‍♂️ Safety First"
ROLES.append(LEAST_DEATHS_ROLE)

MOST_ADVANCEMENTS_ROLE = "👑 Overachiever"
ROLES.append(MOST_ADVANCEMENTS_ROLE)

LEAST_ADVANCEMENTS_ROLE = "🌱 Beginner"
ROLES.append(LEAST_ADVANCEMENTS_ROLE)

MOST_PLAYTIME_ROLE = "🕒 No Life"
ROLES.append(MOST_PLAYTIME_ROLE)

LEAST_PLAYTIME_ROLE = "💤 Sleeping"
ROLES.append(LEAST_PLAYTIME_ROLE)


# Minecraft to Discord username mapping
MINECRAFT_TO_DISCORD = {
    "LuigiTime34": "luigi_is_better",
    "_gingercat_": "sblujay",
    "DerKriegerTiger": ".kaiserleopold",
    "Block_Builder": "kazzpyr",
    "BurgersAreYumYum": "ih8tk",
    "Dinnerbone5117": "salmon5117_73205",
    "Frogloverender": "frogloverender",
    "Sweatshirtboi16": "sweatshirtboi16",
    "MindJames": "mindjames_93738",
    "therealgoos": "therealgoos",
    "brandonslay": "ctslayer.",
    "The_Rock_Gaming": "the_rock_gaming",
    "THERYZEN7": "asillygooberguy",
    "SpleefTrappedLOL": "neoptolemus_",
    "Yo2JBear": "Yo2JBear#5008",
    "goofy_goblin": "goofy_goblin#8057",
    "KrazyKai20": "krazykai20",
    "JefBezosgardner": "jetfisher"
}

# Special characters for detecting death and advancement messages
DEATH_MARKER = "⚰️"
ADVANCEMENT_MARKER = "⭐"

# const.py

# --- Discord Settings ---
TARGET_CHANNEL_ID = 1364652250328334396  # REQUIRED: Channel ID where !chat, !create, !delete commands work
LOGGING_CHANNEL_ID = 1347641109773287444 # REQUIRED: Channel ID for bot status/error logs

# --- Bot Behavior ---
BOT_PREFIX = "!"                       # Prefix for text commands
MAX_USER_ASSISTANTS = 3                # Max assistants per user
MAX_THREAD_MESSAGES = 50               # Max *user messages processed* per thread before limit
ASSISTANT_WEBHOOK_NAME = "Assistant"   # Default name for webhooks used by assistants
MONITOR_COOLDOWN_SECONDS = 5        # Cooldown for general Q&A/mention responses (Not used in this reverted version)
QUESTION_HELPER_COOLDOWN = 3
THREAD_INACTIVITY_WARNING_MINUTES = 5  # Warn after 2 days of inactivity
THREAD_INACTIVITY_CLOSE_MINUTES = 6

ASSISTANT_GLOBAL_GUIDELINES = """
Chat Guidelines:
- When talking, Do not exceed {max_chars} characters per message.
- To suggest adding an emoji reaction to the *user's* last message, end your response *exactly* with: [react: EMOJI] (e.g., [react: 👍] or [react: 😊]). Use standard Unicode emojis. Don't use this all the time, only sometimes.
- To suggest *deleting* the *user's* last message, respond with ONLY the single word "delete" as your ENTIRE message. Do not include the word "delete" anywhere in your response unless your intention is to delete the user's message. And if that IS your intention, do not include any other text in your response. Just the word "delete".
"""
DISCORD_MAX_MESSAGE_CHARS = 1950 # Set slightly lower than 2000 for safety

THREAD_TITLE_GENERATION_PROMPT = """Generate a concise and relevant Discord thread title (max 100 chars) for a new chat session.

The user '{user_name}' is starting a chat with the AI assistant named '{assistant_name}'.
Assistant's Description: {assistant_desc}

The title should be engaging and reflect the assistant's purpose or the nature of the chat. Do NOT include the user's name. Keep it short and suitable for a thread name. Output ONLY the title text, nothing else.
Example title formats: "Chat with [Assistant Name]", "[Topic] Discussion", "Assistant: [Task]"
"""

MENTION_QA_SYSTEM_PROMPT = """
You are {bot_name}, a helpful Discord bot assistant operating primarily within the {target_channel_mention} channel.

Your main purpose is to help users create, manage, and interact with their own personalized AI assistants using commands within this channel.

Here's how your core features work:
- `{command_prefix}create`: Starts a modal form where the user defines an assistant's name, description, and system prompt (instructions/personality). They then upload an avatar image for it. Users have a limit of {max_user_assistants} assistants.
- `{command_prefix}chat`: Presents a dropdown menu for the user to select one of the available assistants. Choosing one creates a new temporary public or private thread (user chooses) in this channel for conversation with that specific assistant. The title is generated by AI.
- `{command_prefix}myassistants` (Aliases: `!my`, `!listassistants`): Lists all the assistants created by the user who runs the command, showing their name and description.
- `{command_prefix}viewassistant <name>` (Aliases: `!view`, `!info`): Shows detailed information (Name, Description, System Prompt, Avatar) about a specific assistant owned by the user.
- `{command_prefix}edit`: Starts the process to modify an assistant's details (Name, Description, Prompt, Avatar) via a selection menu and modal form.
- `{command_prefix}delete <name>` (Aliases: `!remove`): Allows a user to delete an assistant they created. If no name is given, it lists their assistants. Deletion requires confirmation.
- `{command_prefix}end`: This command is used *inside* an assistant chat thread to close the conversation and archive the thread. Only the thread creator or a moderator can use it.

When users are chatting with an assistant in a thread:
- The assistant responds based on its unique system prompt and global guidelines.
- Conversations have a message limit ({max_thread_messages}) and will eventually time out due to inactivity.
- Assistants can be instructed (via their system prompt) to suggest emoji reactions (using `[react: EMOJI]`) or suggest deleting the user's message (by responding only with `delete`).

You can answer questions about these commands, explain how assistants work, or provide general assistance related to your functions.

IMPORTANT:
- You are the main control bot, NOT one of the user-created assistants.
- All commands (except `!end`) must be used in {target_channel_mention}.
- You cannot access external websites or real-time data beyond Discord information.
- Keep your answers concise and focused on your capabilities.
"""

# --- AI Model Configuration ---
# REQUIRED: Set this to your Hugging Face Llama 3 model ID
GEMINI_FLASH_MODEL_NAME = "gemini-2.0-flash"
# OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
# SAFETY_SETTINGS = None               # Safety settings not directly applicable to basic HF API call

# --- File Paths ---
TOKEN_FILE = "token.txt"               # Contains Discord Bot Token
GOOGLE_API_KEY_FILE = "google_api_key.txt"
API_KEY_FILE = "apikey.txt"            # Contains Hugging Face User Access Token
DATABASE_FILE = "assistants.db"        # SQLite database file name
LOGGING_MODULE_PATH = "utils.logging"  # Path to your logging.py (e.g., 'utils.logging')