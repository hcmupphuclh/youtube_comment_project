from workspace.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from workspace.abstractions.endpoints import AbstractionOfEndpoints

class AttachmentOfBlueprints_IndexEndpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/"
        self.endpoint = "index"
        self.callback_function = self.index
        self.methods = ["GET"]
        
    def index(self):
        return "Greetings From Index Phrase of Current Application"