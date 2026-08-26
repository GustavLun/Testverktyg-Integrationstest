class MemberService:
    def __init__(self):
        self.members_list = []

    def register_new_member(self,member):
        self.members_list.append(member)

    def get_member_list(self):
        return self.members_list