"""
    This module contains the abstraction that needs to be implemented
"""

from typing import TypedDict

FilePath = str


InferenceResult = TypedDict('InferenceResult', {
    'data': FilePath,

    # The Media type of the data
    #   Refer to this: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types and https://www.iana.org/assignments/media-types/media-types.xhtml
    'type': str,

    # Extra information related to the result; 
    # Note: Currently ignored during implementation. Only data is currently sent as the output.
    'info': dict
})

InferenceMetadata = TypedDict('InferenceResult', {
    'input_files': list[list[str]],
    'model_artifacts': list[list[str]]
})

     
class Model:
    """
      An object that can infer or predict
      Contains every knowledge about performing the inference given an input
    """
    def infer(self, input_file_paths: list[FilePath]) -> InferenceResult:
        raise NotImplementedError()
    

class ModelBuilder:
    """
        An object that can build the inference model given a list of model artifacts
        contains every logic that it needs to build the model
    """
    def build(self, model_file_paths: list[FilePath]) -> Model:
        raise NotImplementedError()

   
