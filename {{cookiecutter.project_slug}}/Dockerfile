FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .

EXPOSE 8000
CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "8000", "{{ cookiecutter.package_name }}.server:app"]
