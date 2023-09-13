def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(attendees):
    return [badge_maker(name) for name in attendees]

def assign_rooms(attendees):
    room_assignments = []
    for index, name in enumerate(attendees, start=1):
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {index}!")
    return room_assignments

def printer(attendees):
    badges = batch_badge_creator(attendees)
    room_assignments = assign_rooms(attendees)
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)

