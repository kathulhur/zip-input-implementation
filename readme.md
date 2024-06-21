# Inference Service Software Abstraction (Inference Module Abstraction)

## Overview

The Inference Service Software Abstraction enables a clear separation of responsibilities between AI Engineers and web developers. This significantly reduces friction in development and facilitates faster integration between the two domains without needing to know specific details about each other’s roles, leading to faster development and deployment of inferencing functionalities.

The Inference Server Software Abstraction consists of:
- **Web Server Module Abstraction**
- **Inference Module Abstraction**

## This repository contains the Inference Module Abstraction

## Data Types

| Data Types   | Python type | Note                                                         |
|--------------|--------------|--------------------------------------------------------------|
| FilePath     | `str`        | Absolute path of the file                                    |
| Mime         | `str`        | MIME types (IANA media types) - [HTTP](https://www.iana.org/assignments/media-types/media-types.xhtml) | [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) |

### InferenceResult

```python
{
    'data': FilePath,
    'info': dict[str, str],
    'type': Mime
}
```
- **data**: The file path of the output of the inference.
- **info**: Any info related to the inference that the model wants to send.
- **type**: The MIME type of the `data`.

## Inference Module Abstraction (for AI Engineers)

### ModelBuilder Class

An object that can build the inference model given a list of model artifacts. It contains all the logic needed to build the model.

```python
class ModelBuilder:
    def build(model_file_paths: list[FilePath]) -> Model:
        raise NotImplementedError()
```

### Model Class

An object that can infer or predict. It contains all the knowledge about performing the inference given an input.

```python
class Model:
    def infer(input_file_paths: list[FilePath]) -> InferenceResult:
        raise NotImplementedError()
```

## Packaging Model Inference Implementation

After implementing the abstraction, it should be wrapped in a Python package (a folder that has an `__init__.py` inside it) named `implementation`. This package should export:
- `model_builder_class`: Holds a reference to the `ModelBuilder` class implementation.
- `inference_metadata`: Describes the input requirements of the model.

Additionally, a `requirements.in` file must be included containing the dependencies of the implementation. This package then needs to be stored in an accessible repository for integration and automation (e.g., GitHub).

### Example Directory Structure

```
implementation/
    __init__.py
    abstraction.py
    model_implementation.py
    inference_metadata.py
inference_metadata.py
requirements.in
```

### Example `__init__.py`

```python
from .model_implementation import ModelBuilder
from .inference_metadata import inference_metadata

model_builder_class = ModelBuilder
```

### Example `requirements.in`

```
# List your package dependencies here
numpy
pandas
tensorflow
```

## How to Use

1. Implement the `ModelBuilder` and `Model` classes as per the abstractions defined above.
2. Create a Python package named `implementation` with an `__init__.py` file.
3. Ensure `implementation` exports:
   - `model_builder_class`: Reference to your `ModelBuilder` class.
   - `inference_metadata`: Metadata describing your model's input requirements.
4. Include a `requirements.in` file listing the dependencies.
5. Store the package in an accessible repository (e.g., GitHub) for integration and automation.

By following these steps, you ensure a smooth and efficient development and deployment process for AI inferencing functionalities.