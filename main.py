from imports import *

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
IMAGE_LOCATION = ''
WORD_FILE_LOCATION = ''
PASSPORT_IMAGE_LOCATION = ''
TO_GENERATE_IMAGE = False
TO_GENERATE_DOCX = False

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def generate_document(image):
    global IMAGE_LOCATION, WORD_FILE_LOCATION
    image_path = f'static/uploads/{image}'
    IMAGE_LOCATION = image_path
    doc = Document()

    section = doc.sections[0]
    section.orientation = WD_ORIENTATION.LANDSCAPE
    section.page_width = Cm(15)
    section.page_height = Cm(10)
    section.top_margin = Cm(0.75)
    section.bottom_margin = Cm(0.75)
    section.left_margin = Cm(0.75)
    section.right_margin = Cm(0.75)

    image_width_cm = 2.9718
    image_height_cm = 3.9624

    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    for i in range(8):
        run = paragraph.add_run()
        run.add_picture(image_path, width=Cm(image_width_cm), height=Cm(image_height_cm))

        paragraph.space_before = Pt(0)
        paragraph.space_after = Pt(0)

    output_doc_name = image.split('.')[0] + '.docx'
    output_path = f"static/documents/{output_doc_name}"
    WORD_FILE_LOCATION = output_path
    doc.save(output_path)
    # print(f'{output_doc_name} is generated')


def generate_image(photo):
    # print(f' this func is under the process! it may take a while to complete {photo} ')
    ...


def generate_func_backend(photo_image, method):
    global TO_GENERATE_DOCX
    # print(f' the image is {photo_image} and method is {method}')

    if method == 'word':
        generate_document(photo_image)
        TO_GENERATE_DOCX = True

    elif method == 'img':
        generate_image(photo_image)

    else:
        render_template('error.html')

    # print(TO_GENERATE_DOCX)
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact_us():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        file = request.files['img_file']
        filename = secure_filename(file.filename)
        operation = request.form.get('flexRadioDefault')

        if file.filename == '':
            return 'No selected file, Please select a file'

        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            generate_func_backend(filename, operation)
            return render_template("index.html")

        # print(operation)

        if operation == 'word':
            # print(1)
            generate_document(file)

        elif operation == 'img':
            # print(2)
            generate_image(file)

        elif operation == 'None':
            # print(2.5)
            ...

        else:
            # print(3)
            return render_template('error.html')

        return render_template('index.html', image_file=filename)


@app.route('/download_word_file')
def download_word_file():
    global WORD_FILE_LOCATION
    if WORD_FILE_LOCATION:
        return send_file(WORD_FILE_LOCATION, as_attachment=True)
    else:
        return "No Word file generated yet."


app.run(debug=True, port=5005)
