import os, os.path
from flask import Flask, render_template, url_for, Markup
from flask_talisman import Talisman

app = Flask(__name__)
if not os.path.isfile("local_dev_environment.flagfile"):
    Talisman(app)


@app.route("/")
def home():
    return main_pages("home")


@app.route("/<page>")
def main_pages(page):
    return pages(page,"content", "content", "footer_content")


@app.route("/footer-links/<page>")
def link_pages(page):
    return pages(page, "footer_content", "content", "footer_content")


def pages(page, content_folder, content_links_folder, footer_content_folder):
    pages_caption = "Not found"
    pages_content = "Sorry, no content available."
    active_link = "notfound"

    if not page_name_too_long(page):
        caption_filename = content_folder + "/" + page + "_caption.html"
        content_filename = content_folder + "/" + page + ".html"
        active_link = page

        if os.path.isfile(caption_filename):
            with open(caption_filename, 'r', encoding='utf-8') as f:
                pages_caption = Markup(f.read())

        if os.path.isfile(content_filename):
            with open(content_filename, 'r', encoding='utf-8') as f:
                pages_content = Markup(f.read())

    return render_template(
        "index.html", caption=pages_caption, content=pages_content, active_link=active_link, items=get_items(content_links_folder), footer_items=get_items(footer_content_folder)
    )


def page_name_too_long(name):
    return len(name) > 80


def get_items(name):
    files = os.listdir(name)
    result = []
    for item in files:
        if os.path.isfile(name + "/" + item) and not "_caption" in str(item):
            result.append(os.path.splitext(item)[0])
    return result
