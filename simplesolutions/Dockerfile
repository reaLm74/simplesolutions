FROM python:3.9-slim
WORKDIR /simplesolutions
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV YOUR_DOMAIN='http://127.0.0.1:8000'
ENV STRIPE_PUBLIC_KEY='pk_test_51OI8jWGEyMhG5AdmggBTmWFsZczRGi84CrnJiB4HUyx1FJ9z7re8niL4eu50fVnoIlw1m16Cub2e3mCxylmeDi6s00Xj82A0UM'
ENV STRIPE_SECRET_KEY='sk_test_51OI8jWGEyMhG5AdmLOuUM75eDjE3gJlH9Gjj8wjDRvHe8Lzpo4CtBDxHgigAPTWcl3UCshTbUtAxiTjHrif3DnZA00lOVaDLo5'
CMD ["python3", "manage.py", "runserver", "0:8000"]

