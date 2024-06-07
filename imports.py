from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.section import WD_ORIENTATION
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import os
import webbrowser
