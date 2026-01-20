# مرحله 1: پایه
FROM python:3.11-slim

# تنظیم working directory
WORKDIR /app

# کپی requirements و نصب پکیج‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی بقیه کد
COPY . .

# expose port
EXPOSE 8000

# دستور اجرای اپ
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

