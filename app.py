from flask import Flask, render_template, url_for, Markup

app = Flask(__name__)


@app.route("/")
def home():
    home_caption = "Free database migration tool"
    home_content = (
        """
        Felix-db-migration-tool is a java based tool we provide for easiely migrating data from one database to another. 
        In the current version we try to offer a simple API especially for encapsulating data reads and writes from and to a MySQL. 
        Our goal is to provide a simple and efficient converting mechanism from database 
        specific formats into a generic format while covering a large variety of database systems. In the current 
        version we only support MySQL and MongoDB. Our plan is to enhance functionality and gradually increase the number of supported 
        database systems. While the free version will continue to receive important updates we'll start to ship an 
        advanced version of our software which can be purchased. This Version will include advanced functionality, 
        stable and experimental API and other special features. If you have any questions or want to suggest something 
        we should include in future updates, feel free do contact us at lpke.flx@gmail.com. 
        The tool can be downloaded """
        + Markup(
            '<a target="_blank" href="https://github.com/flikkes/felix-db-migration-tool/releases">here</a>'
        )
        + """.
    """
    )
    return render_template(
        "index.html", home_caption=home_caption, home_content=home_content
    )


@app.route("/products")
def products():
    products_caption = "Free database migration tool"
    products_content = (
        """
        Felix-db-migration-tool is a java based tool we provide for easiely migrating data from one database to another. 
        In the current version we try to offer a simple API especially for encapsulating data reads and writes from and to a MySQL. 
        Our goal is to provide a simple and efficient converting mechanism from database 
        specific formats into a generic format while covering a large variety of database systems. In the current 
        version we only support MySQL and MongoDB. Our plan is to enhance functionality and gradually increase the number of supported 
        database systems. While the free version will continue to receive important updates we'll start to ship an 
        advanced version of our software which can be purchased. This Version will include advanced functionality, 
        stable and experimental API and other special features. If you have any questions or want to suggest something 
        we should include in future updates, feel free do contact us at lpke.flx@gmail.com. 
        The tool can be downloaded """
        + Markup(
            '<a target="_blank" href="https://github.com/flikkes/felix-db-migration-tool/releases">here</a>'
        )
        + """.
    """
    )
    return render_template(
        "index.html", home_caption=products_caption, home_content=products_content
    )
