booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "
parts = [part.strip() for part in booking.split('|')]
event_code = parts[0]
username = parts[1]
room = parts[2]
time_str = parts[3]
email = parts[4]
vip_tag = parts[5]
name_parts = username.split('_')
name = '_'.join([p.capitalize() for p in name_parts])
room_upper = room.upper()
email_domain = email.split('@')[1].lower()
vip_count = vip_tag.count('VIP')
valid_event = event_code.startswith('EVT-') and event_code[4:].isdigit()
valid_username = all(c.isalnum() or c == '_' for c in username)
valid_room = room.startswith('Room-') and room[5:].isdigit()
time_parts = time_str.split(':')
valid_time = (len(time_parts) == 2 and
              time_parts[0].isdigit() and time_parts[1].isdigit() and
              0 <= int(time_parts[0]) < 24 and 0 <= int(time_parts[1]) < 60)
valid_email = '@' in email and '.' in email.split('@')[1]
print(f"Event code: {event_code}")
print(f"Name: {name}")
print(f"Room: {room_upper}")
print(f"Time: {time_str}")
print(f"Email domain: {email_domain}")
print(f"VIP tag count: {vip_count}")
print(f"Valid event code: {valid_event}")
print(f"Valid username: {valid_username}")
print(f"Valid room: {valid_room}")
print(f"Valid time: {valid_time}")
print(f"Valid email: {valid_email}")
