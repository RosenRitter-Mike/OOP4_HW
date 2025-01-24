from user import User
from errors import *
from datetime import datetime, timedelta

eof: bool = False
while not eof:
    try:
        users = [
            ("Loki Laufeyson", 'LoKi@jutun.ygd', 'JurM0ng@n$', '31-12-1000'),  # Should work properly
            ("Ra", 'SunGod@sky.eg', 'RaMa^Jan@', datetime.now() - timedelta(days=365 * 100)),  # Name too short
            ("100101001", 'od2001@jupiter.gov', '!Q2w#E4r', '04-03-1968'),  # Name non-char
            ("Gilgamesh", 'king_of_Uruk', 'Enkidu$$$', datetime.now() - timedelta(days=365 * 100)),  # Illegal email
            ("Dionysus", 'party_guy@olympus.gr', 'ouzo_for_everyone', '01/01/0001'),  # Illegal password
            ("CSM-101", 'Shwatz@Cyberdine.com', 'IlBeB@&k', '01.04.2030'),  # Illegal birthday
            ("Photon", 'here@now.co.uk', '1a@S3d$F', datetime.now()),  # Too young
        ]

        for name, email, password, birthday in users:
            try:
                user = User(name, email, password, birthday)
                print(f"Successfully created user: {name}\n")
            except UserNameTooShortError as e:
                print(f"User name is too short!!!\n{e}")
            except NameNonCharError as e:
                print(f"User name does not contain any letters!!!\n{e}Are you a rogue AI?\n")
            except IllegalEmailFormatError as e:
                print(f"User email cannot exist!!!\n{e}")
            except IllegalPasswordFormatError as e:
                print(
                    f"User password must contain upper case and lower case letters, and a special character!!!\n{e}")
            except IllegalBirthdayError as e:
                print(f"Incorrect birth day!!! \nNo time travelers are allowed!!!\n{e}")
            except UserTooYoungError as e:
                print(f"User is too young!!!\n{e}Return in a few years when you are older!\n")

    finally:
        print("End Of File")
        eof = True