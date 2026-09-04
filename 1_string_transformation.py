booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

######### EXPECTED OUTPUT #########
""" Event code: EVT-2026
Name: Alice_Wong
Room: ROOM-305
Time: 14:30
Email domain: unimail.edu
VIP tag count: 2
Valid event code: True
Valid username: True
Valid room: True
Valid time: True
Valid email: True """


cleaned = booking.strip()
parts = cleaned.split(" | ")

event_code = parts[0]
raw_name = parts[1]
raw_room = parts[2]
time_str = parts[3]
email = parts[4]
vip_part = parts[5]

name_parts = raw_name.split("_")
first_name = name_parts[0]
last_name = name_parts[1]
name = first_name.capitalize() + "_" + last_name.capitalize()

room = raw_room.upper()

email_parts = email.split("@")
email_domain = email_parts[1].lower()

vip_tag_count = vip_part.count("VIP")

valid_event_code = event_code.startswith("EVT-")
valid_username = "_" in raw_name
valid_room = raw_room.lower().startswith("room-")
valid_time = ":" in time_str
valid_email = "@" in email

print(f"""Event code: {event_code}
Name: {name}
Room: {room}
Time: {time_str}
Email domain: {email_domain}
VIP tag count: {vip_tag_count}
Valid event code: {valid_event_code}
Valid username: {valid_username}
Valid room: {valid_room}
Valid time: {valid_time}
Valid email: {valid_email}""")
