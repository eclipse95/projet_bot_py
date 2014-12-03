class node():
    def __init__(self,owner=0,radius=None,pos=[],offsize=None,defsize=None,prod=1):
        self.owner=owner
        self.radius=radius
        self.pos=pos
        self.offsize=offsize
        self.defsize=defsize
        self.prod=prod
    def update(self,owner,offsize,defsize):
        self.owner=owner
        self.offsize=offsize
        self.defsize=defsize
