from os import name


class Event:
    def __init__(self):
        self.property = []



    def register_new_member(self, member,ms):
        self.property.append(member)
        ms.register_new_member(member)

    def sign_up(self, member,ms):

        if member in ms.member_list:
            self.property.append(member)

   
    pass


