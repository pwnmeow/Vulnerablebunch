import ftplib
from flask import (
    Blueprint,
    render_template,
    request
)
from lxml import etree
import html

bp = Blueprint(
    "a3", __name__,
    template_folder='templates',
    static_folder='static'
)

# @bp.route("/A3", methods = ['POST', 'GET'])
# def a3():
#     ### Is this really necessary? FTP is a cleartext protocol
#     try:
#         connection = ftplib.FTP("ftp.example.com")
#     except:
#         pass
#     return render_template("a3.html")



# payload 

# <?xml version="1.0" ?>
# <!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
# <note>
# <to>Alice</to>
# <from>Bob</from>
# <header>Sync Meeting</header>
# <time>1200</time>
# <body>Meeting time changed &xxe;</body>
# </note>


@bp.route('/A3', methods = ['POST', 'GET'])
def xml():
    parsed_xml = None
    if request.method == 'POST':
        # xml = request.form['xml']
        with open('sitemap.xml','r') as f:
            xml = f.read()
        parser = etree.XMLParser(no_network=False, dtd_validation=False, load_dtd=True, huge_tree=True)
        #try:
        doc = etree.fromstring(xml.encode(), parser)
        parsed_xml = etree.tostring(doc).decode('utf8')
        #except:
            #pass
    return html.escape(parsed_xml)
    return """
       <html>
          <body>""" + "Result:\n<br>\n" + html.escape(parsed_xml) if parsed_xml else "" + """
             <form action = "/A3" method = "POST">
                <p><h3>Enter xml to parse</h3></p>
                <textarea class="input" name="xml" cols="40" rows="5"></textarea>
                <p><input type = 'submit' value = 'Parse'/></p>
             </form>
          </body>
       </html>
       """

