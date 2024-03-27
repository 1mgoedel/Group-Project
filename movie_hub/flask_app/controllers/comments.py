from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.comment import Comment
from flask_app.models.user import User