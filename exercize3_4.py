#Name people you'd like to invite for dinner

guest_list = ['Irene Hoff', 'Elizabeth Gilbert', 'Betty Poulsen' ]
print(f"Hello, {guest_list[1]}, your writing has always inspired me. Would you care to share a drink next friday?")

declined_guest = guest_list.pop(0)
guest_list.insert(0, 'Trevor Hall')
print(f"Hello {declined_guest}, we're sorry you can't make it!")
print(f"Hello {guest_list[0]}, we're excited to see you there!")
print(f"Hello {guest_list[1]}, we're excited to see you there!")
print(f"Hello {guest_list[2]}, we're excited to see you there!")

guest_list.insert(1, 'Erin Evans')
guest_list.append('Irene Hoff')
print(guest_list)

print(len(guest_list))