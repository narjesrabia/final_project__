FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install Pillow==8.3.1  # הוספת פקודה להתקנת Pillow בנפרד
COPY . .
CMD ["python", "manage.py", "runserver"]
