## Description
This microservice validates a CSV file sent over REST. It checks:
- Maximum file size  
- Maximum characters per cell  
- Required number of columns per row  

It returns a JSON response indicating whether the CSV is valid and, if not, what errors were found.

---

# Communication Contract

## 1. Compatibility

Requires Python 3.13 or higher.

---

## 2. Installing

pip install fastapi

## 1. How to Request Data from This Microservice

### Endpoint
```
POST /upload_csv/
```

### Required Query Parameters
| Parameter     | Type | Description |
|---------------|------|-------------|
| max_size      | int  | Maximum allowed file size in bytes |
| max_chars     | int  | Maximum allowed characters per CSV cell |
| num_columns   | int  | Required number of columns for each row |

### Required Form Data
| Field | Type | Description |
|-------|------|-------------|
| file  | file upload | CSV file to validate |

---

## 2. Example Request

```python
import requests

def main():
    url = "http://127.0.0.1:8000/upload_csv/"
    params = {
        "max_size": 10485760,
        "max_chars": 100,
        "num_columns": 5
    }

    try:
        with open("test2.csv", "rb") as f:
            files = {"file": f}

            print("Sending request to CSV microservice...")
            response = requests.post(url, params=params, files=files)

            print("Status code:", response.status_code)
            print("Raw text:", response.text)
            print("As JSON:", response.json())
    except Exception as e:
        print("Error while calling microservice:", repr(e))

if __name__ == "__main__":
    main()
```

---

## 3. Sequence Diagram

![alt text](images/seq_diagram.png)

---

# How to Run the Microservice

Start the server using:

```bash
uvicorn data_validation_group:app --reload
```

The microservice will be available at:

```
http://127.0.0.1:8000
```

---


