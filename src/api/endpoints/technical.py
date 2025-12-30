import io
import csv

from fastapi import APIRouter, Request, UploadFile, File, HTTPException
from pydantic import BaseModel

technical_router = APIRouter(tags=["Technical"])

class UpdateStatusResponse(BaseModel):
    update_cv_progress: str

@technical_router.post(
    "/upload-grades",
    summary="Обновить статус резюме",
    description="Изменяет статус резюме по его ID."
)
async def update_cv_status(request: Request, file: UploadFile = File(...)):
    if file.content_type not in {"text/csv"}:
        raise HTTPException(status_code=415, detail="Unsupported file type.")

    try:
        content = await file.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {e}")
    finally:
        await file.close()
    
    decoded_content = content.decode('utf-8')
    text = io.StringIO(decoded_content)
    reader = csv.DictReader(text)

    if not reader.fieldnames == ['full_name', 'subject', 'grade']:
        raise HTTPException(status_code=500, detail=f"Uncorrect field names. Correct are: name, subject, grade")

    request.app.state.db.dump_to_db(reader)

    text.seek(0)
    reader = csv.DictReader(text)
    n_students = len({row['full_name'] for row in reader})
    
    return {
        "status": "ok",
        "records_loaded": reader.line_num,
        "students": n_students
    }
    