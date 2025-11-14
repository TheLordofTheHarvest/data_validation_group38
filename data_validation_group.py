from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from io import StringIO
import csv

app = FastAPI()

def validate_csv(file, max_size, max_chars, num_columns):
    file_like = StringIO(file.decode()) # Create fileish object for CSV reading
    reader = csv.reader(file_like)
    
    errors = []
    size = len(file)
    

    if size > max_size:    # Check file size
        errors.append(f"File size exceeds the limit of {max_size} bytes.")
    
    row_count = 0
    for row in reader:
        row_count += 1
        # Check the number of columns in the row
        if len(row) != num_columns:
            errors.append(f"Row {row_count} does not have {num_columns} columns.")
        
        # Check each cell for character limit
        for col_index, cell in enumerate(row):
            if len(cell) > max_chars:
                errors.append(f"Cell {col_index+1} in row {row_count} exceeds {max_chars} characters.")
    
    return errors

@app.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...), max_size: int = 10485760, max_chars: int = 100, num_columns: int = 5):
    # Read file data
    file_data = await file.read()

    # Validate the file
    errors = validate_csv(file_data, max_size, max_chars, num_columns)
    
    if errors:
        return JSONResponse(content={"valid": False, "errors": errors}, status_code=400)
    return {"valid": True, "message": "CSV is valid"}
