import getopt, sys
from getopt import GetoptError

argsList = sys.argv[1:]

options = "n:t:T:s:r:g:e:h"
long_options = ["Event_Name=", "Timestamp=", "Generate_Timestamp=", "Server=", "Room=", "Giveaways=", "Extra_Details=", "Help"]

event_name = "<name-text-event>"
timestamp = "000000000"
server_name = "<server-name>"
room_name = "<room-name>"
giveaways_text = "**Nitro giveaway** if we hit 25+ online. **Gamenights**, **Minecraft giveaways** at 20+."
extra_details = []

def make_dm_file() -> None:
    with open("./dm-message.txt", "w") as dm_file:

        TEXT2 = f"```Hi there! Our **{event_name}** event is starting up right now! (<t:{timestamp}:R>) \n\
\n\
Make sure to log in your CPAB account https://play.cpabattleground.com/ , join  https://discord.com/channels/705902481896636499/973666390768762941 and check <#921414786942656522> main-chat for faster tactics and commands! \n\
\n\
> Server: **{server_name}**\n\
> Room:  **{room_name}**\n\
\n\
- Do `!army WV` once you log in.\n"

        if len(extra_details) != 0:
            for dtail in extra_details:
                TEXT2 = TEXT2 + "- " + dtail + "\n"


        TEXT2 = TEXT2 + f"- Link: https://play.cpabattleground.com/\n\
\n\
{giveaways_text}\n\
```"

        dm_file.write(TEXT2)


class OptionError(GetoptError):

    def __init__(self, msg: str, opt: str = "") -> None:
        super().__init__("Option in developt, please give a specific timestamp using -t/--Timestamp argument.", opt)


try:
    arguments, values = getopt.getopt(argsList, options, long_options)

    make_file = False

    for opt, arg in arguments:

        # Event Name
        if opt in (f"-{options[0]}", f"--{long_options[0]}"):
        #if opt in ("-n", "--Event_Name"):
            event_name = arg
            make_file = True
        
        # Timestamp
        elif opt in (f"-{options[2]}", f"--{long_options[1]}"):
        #elif opt in ("-t", "--Timestamp"):
            timestamp = arg
            make_file = True

        # Generate a Timestamp - (functionality in develop)
        elif opt in (f"-{options[4]}", f"--{long_options[2]}"):
        #elif opt in ("-T", "--Generate_Timestamp"):
            raise OptionError("Option in developt, please give a specific timestamp using -t/--Timestamp argument.")

        # Server
        elif opt in (f"-{options[6]}", f"--{long_options[3]}"):
        #elif opt in ("-s", "--Server"):
            server_name = arg
            make_file = True

        # Room
        elif opt in (f"-{options[8]}", f"--{long_options[4]}"):
        #elif opt in ("-r", "--Room"):
            room_name = arg
            make_file = True

        # Giveaways
        elif opt in (f"-{options[10]}", f"--{long_options[5]}"):
        #elif opt in ("-g", "--Giveaways"):
            giveaways_text = arg
            make_file = True

        # Extra Details
        elif opt in (f"-{options[12]}", f"--{long_options[6]}"):
        #elif opt in ("-e", "--Extra_Details"):
            extra_details.append(arg.replace('@', '`'))
            make_file = True
        
        # Help
        elif opt in (f"-{options[14]}", f"--{long_options[7]}"):
            print("\nProgram that makes a DM message remind.\n\
Usage:\n\
dm-organicer.py [-<options> <arguments>]\n\
\n\
-n  --Event_Name             Set the Name event. Default=<name-text-event>\n\
\n\
-t  --Timestamp              Set the date and hour that event will start.\n\
                             Default=000000000\n\
\n\
-T  --Generate_Timestamp     OPTION IN DEVELOPMENT, DON'T USE IT NOW.\n\
                             Optional. Generate a timestamp from text format date.\n\
                             The format is 'dd/MM/yyyy hh:mm'.\n\
                             It's good if you don't have time to search the timestamp.\n\
\n\
-s  --Server                 Set the CPA server that event will occur.\n\
                             Default=<server-name>\n\
\n\
-r  --Room                   Set the CPA room that event will occur.\n\
                             Default=<room-name>\n\
\n\
-g  --Giveaways              Set the text for giveaways.\n\
                             Default=**Nitro giveaway** if we hit 25+ online. **Gamenights**, **Minecraft giveaways** at 20+.\n\
\n\
-h  --Help                   Optional. Display this help message.\n\
\n\
-e  --Extra_Details          Optional. Multivalue. Set all extra details into - palce. You can set more than 1 -e that you want for extra details.")
        

    if (make_file):
        make_dm_file()
except getopt.error as err:
    print("Argumentos error.")
    print(err.msg)
except Exception as err:
    print("Ha ocurrido un error inseperado, por favor envie el error para poder arreglarlo.")
    print(err)

