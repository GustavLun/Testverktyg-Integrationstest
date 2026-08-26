class Event:
    def __init__(self, member, ):
        self.property = []
        self.member = member

    def register_new_member(self, member,ms):
        self.property.append(member)
        ms.register_member(member)

   
    pass


