import pathlib
from .abstraction import FilePath, InferenceResult
from .abstraction import Model, ModelBuilder

MODULE_DIR = pathlib.Path(__file__).parent
SAMPLE_IMAGE_PATH = MODULE_DIR / 'assets' / 'sample-image.png'



class ModelImplementation(Model):

    def infer(self, input_file_paths: list[str]) -> InferenceResult:
        return {
            'data': str(SAMPLE_IMAGE_PATH),
            'info': {},
            'type': 'image/png'
        }



class ModelBuilderImplementation(ModelBuilder):

    def build(self, model_file_paths: list[str]) -> Model:
        return ModelImplementation()
    



inference_metadata = {
    'input_files': [ ['application/zip'] ],
    'model_artifacts': [[]]
}