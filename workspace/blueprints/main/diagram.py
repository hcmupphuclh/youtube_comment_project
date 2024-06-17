from flask import Blueprint
from workspace.blueprints.main.attachments.endpoints.graphOfIndexEndpoint import AttachmentOfBlueprints_IndexEndpointGraph

class Main_Entry_Diagram():
    
    @property
    def progress(self) -> Blueprint:
        return self._progress
    
    @progress.setter
    def progress(self, progress: Blueprint):
        self._progress = progress
    
    def __init__(self) -> None:
        self.name = "main"
        self.import_name = "__name__"
        self.template_folder = "templates"
        
        self.progress = Blueprint(self.name, self.import_name,
                                  template_folder=self.template_folder)
        
        self.register_endpoints()
        
    def register_endpoints(self):
        indexEndpointGraph = AttachmentOfBlueprints_IndexEndpointGraph(self)
        indexEndpointGraph.endpointRegisteration()