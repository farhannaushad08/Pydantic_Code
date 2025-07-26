
# 🐍 Pydantic Tutorial – Code Examples

This repository contains step-by-step examples that explore **Pydantic**, a data validation and settings management library in Python.

These examples follow a progressive structure to help you learn key concepts like model creation, validation, nested models, computed fields, and serialization.

---

## 📁 Files & Descriptions

| File Name                | Description                                                        |
|-------------------------|--------------------------------------------------------------------|
| `1_pydantic_intro.py`    | Basic usage of Pydantic models                                     |
| `2_field_validator.py`   | Using `@field_validator` to validate individual fields             |
| `3_model_validator.py`   | Using `@model_validator` to validate the full model                |
| `4_computed_fields.py`   | Creating computed/derived fields using `@computed_field`           |
| `5_nested_models.py`     | Demonstrating nested models inside another Pydantic model          |
| `6_serialization.py`     | Serializing models using `.model_dump()` and `.model_dump_json()` |

---

## 🧰 Requirements

- Python 3.10 or higher
- Pydantic v2.x

### ✅ Install Pydantic

```bash
pip install pydantic
```

---

## 🚀 How to Run Examples

To run any of the examples, use:

```bash
python 1_pydantic_intro.py
```

You can replace the filename with any of the other files to test specific features.

---

## 📚 Learning Notes

This tutorial is based on concepts from the [Pydantic documentation](https://docs.pydantic.dev/latest/).

The code is beginner-friendly and demonstrates:
- Defining and using Pydantic models
- Type enforcement and data parsing
- Field-level validation with `@field_validator`
- Model-level validation with `@model_validator`
- Creating dynamic/computed fields
- Handling nested models
- Serializing and exporting models as dictionaries or JSON

---

## 🙌 Author

**Farhan Naushad**  
🔗 [GitHub Profile](https://github.com/farhannaushad08)

---

> ⭐ Feel free to fork, use, or contribute to this repository!
