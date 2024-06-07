# Passport Generator

This project is a Flask web application that allows users to upload an image and either generate a document (DOCX) with the image or generate another type of image (this functionality is not yet implemented). Users can then download the generated document.

## Features

1. **Upload Image**: Users can upload images in PNG, JPG, JPEG, GIF, or WEBP formats.
2. **Generate Document**: The uploaded image can be placed into a Word document (DOCX) in a specific layout.
3. **Download Document**: Users can download the generated Word document.

## Requirements

- **Python 3.x**
- **Flask**
- **python-docx**
- **Werkzeug**

## Project Structure

- `main.py`: Main application file containing the Flask routes and core logic.
- `imports.py`: Contains import statements used in `main.py`.
- `templates/`: Directory containing HTML templates.
  - `index.html`: Main page where users can upload images and choose an operation.
  - `contact.html`: Contact us page.
  - `about.html`: About us page.
  - `project.html`: Project details page.
  - `error.html`: Error page.
- `static/uploads/`: Directory to store uploaded images.
- `static/documents/`: Directory to store generated documents.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

1. **Open the application**: Open your web browser and navigate to `http://127.0.0.1:5005`.
2. **Upload an Image**: On the main page, click the "Choose File" button to select an image file.
3. **Select an Operation**: Choose either "Generate Word Document" or "Generate Image" (note: the image generation feature is not implemented).
4. **Generate**: Click the "Generate" button. The application will process the image and generate the requested output.
5. **Download Document**: If you selected to generate a Word document, you can download it by clicking the "Download Word File" link.

## Code Explanation

### `main.py`

- **Configuration**:
    - `UPLOAD_FOLDER`: Directory to store uploaded images.
    - `ALLOWED_EXTENSIONS`: Set of allowed image file extensions.
    - `app`: Flask application instance.

- **Helper Functions**:
    - `allowed_file(filename)`: Checks if the uploaded file has an allowed extension.
    - `generate_document(image)`: Generates a Word document with the uploaded image.
    - `generate_image(photo)`: Placeholder function for generating an image (not implemented).
    - `generate_func_backend(photo_image, method)`: Backend function to determine which generation method to use.

- **Flask Routes**:
    - `/`: Renders the main page.
    - `/contact`: Renders the contact page.
    - `/about`: Renders the about page.
    - `/project`: Renders the project details page.
    - `/generate`: Handles the file upload and generation logic.
    - `/download_word_file`: Allows users to download the generated Word document.

### `imports.py`

Contains necessary imports for the application, including Flask, Werkzeug, and python-docx libraries.

## Note

- Ensure the directories `static/uploads` and `static/documents` exist in the project root before running the application.
- The "Generate Image" feature is currently not implemented.

## License

This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

## Author

- Developed by: [Your Name]
