class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0.2, 0.2, 0.35, 1)
        self.startNew()
        self.addBlock((0,10,0))


     
    def startNew(self):
        self.land = render.attachNewNode("Land")

    
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)



    

    
