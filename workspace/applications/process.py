from flask import Flask
from workspace.blueprints.main.document import ProgressOfMain

class Process():
    
    @property
    def process(self) -> Flask:
        return self._process
    
    @process.setter
    def process(self, process: Flask):
        self._process = process
        
    def __init__(self) -> None:
        self.process = Flask(__name__)
        
        main = ProgressOfMain()
        self.process.register_blueprint(main.progress)
        
    def run(self, *args, **kwargs):
        self.process.run(*args, **kwargs)