import os.path
from flask import Flask, render_template, url_for, Markup
from flask_talisman import Talisman

app = Flask(__name__)
if not os.path.isfile("local_dev_environment.flagfile"):
    Talisman(app)


@app.route("/")
def home():
    active_link = "home"
    home_caption = "Felix Development and Consulting"
    home_content = Markup(
        """
        Hi there,<br><br>
        my name is Felix. I'm a software engineer from Germany who is passionate about building software which is simple, 
        straightforward and useful for solving a specific problem. Also I'm highly interested in creating new sources of 
        knowledge for those who haven't been in touch with the topic of software creation and would like to learn something about it.<br><br>
        Right now I'm working on two projects which I'd like to turn into actual products within the next months. One being a 
        java based database migration tool. My second project is a low-threshold programming course which contains fundamentals of 
        programming, software engineering and creating and deploying your first application.<br><br>
        For more information, visit <a href="/products">Products</a> and <a href="/courses">Courses</a>. 
        """
    )
    return render_template(
        "index.html", home_caption=home_caption, home_content=home_content, active_link=active_link
    )


@app.route("/courses")
def courses():
    active_link = "courses"
    courses_caption = "Felix' software development course"
    courses_content = Markup(
        """
        A free version of my software development course will be available soon. It will give you a taste of how the content is 
        structured as well as how things are explained. Be sure to check it out - it's free! 
        """
    )
    return render_template(
        "index.html", home_caption=courses_caption, home_content=courses_content, active_link=active_link
    )


@app.route("/products")
def products():
    active_link = "products"
    products_caption = "Free database migration tool"
    products_content = Markup(
        """
        Felix-db-migration-tool is a java based tool for easily migrating data from one database to another. 
        In the current version I try to offer a simple API especially for encapsulating data reads and writes from and to a MySQL database. <br><br>
        My goal is to provide a simple and efficient converting mechanism from database 
        specific formats into a generic format while covering a large variety of database systems. 
        In the current version only MySQL and MongoDB are supported. My plan is to enhance functionality and gradually increase the number of supported 
        database systems. <br><br>
        While the standard open source version will continue to receive important updates I'll start to develop an 
        advanced version of the software which will be available soon. This Version will include advanced functionality, 
        stable and experimental API and other special features. <br><br>
        If you have any questions or want to suggest something 
        I should include in future updates, feel free to contact me at <a href="mailto:lpke.flx@gmail.com">lpke.flx@gmail.com</a>. 
        <h3><a target="_blank" href="https://github.com/flikkes/felix-db-migration-tool/releases">Download the tool here.</a></h3>
        """
    )
    return render_template(
        "index.html", home_caption=products_caption, home_content=products_content, active_link=active_link
    )
