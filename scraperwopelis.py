#encoding: utf-8
import mechanize
import cookielib
from bs4 import BeautifulSoup
import re
import time

class ScrapperWopelis():
    def __init__(self,cookies_path):
        self.br = mechanize.Browser()
        self.cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cj)
        self.cj.load(cookies_path)

        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; es-VE; rv:1.9.0.1)Gecko/2008071615 Debian/6.0 Firefox/9')]
        self.br.addheaders = [('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
        self.br.open('http://www.wopelis.com')

    def getAllLinks(self,html):
        links = []    
        soup = BeautifulSoup(html,'html.parser')
        title = soup.findAll('h1', {'class': 'titulop'})[0].text.replace("Viendo enlaces de: ","")
        if title != '?????':
            for x in soup.find_all('a'):    # will give you all a tag
                try:
                    if re.match('redir',x['onclick']):    # if onclick attribute exist, it will match for searchDB, if success will print
                        j = x['onclick'][6:-2].split(',')
                        links.append(j[0].replace("'", ""))        # here you can do your stuff instead of print
                except:pass
        pretifyToHtml(title, links)


    def getHtml(self,url):
        try:
            return self.br.open(url).read()
        except:
            print "Error in "+url

    def showLinks(self,url):
        
        self.getAllLinks(self.getHtml(url))
        

    def getFullSerie(self,url):
        start_time = time.time()
        soup = BeautifulSoup(getHtml(url),'html.parser')
        caps = soup.findAll('a', {'target': '_blank'})
        for cap in caps:
            try:
                self.showLinks("http://www.wopelis.com" +cap['href'].replace("..", ""))
            except:
                print "Problem in " + cap['href']

        elapsed_time = time.time() - start_time
        print elapsed_time


    def pretifyToHtml(self,title, links):
        html = ''
        foo= '''<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="../../favicon.ico"><title>'''

        html = html + foo + title

        foo = '''</title>

        <!-- Bootstrap core CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <!-- Bootstrap theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <link href="../../assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

        <!-- Custom styles for this template -->
        <link href="theme.css" rel="stylesheet">

        <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
        <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
        <script src="../../assets/js/ie-emulation-modes-warning.js"></script>

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>

      <body>

        <!-- Fixed navbar -->
        <nav class="navbar navbar-inverse navbar-fixed-top">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">Bootstrap theme</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="#">Action</a></li>
                    <li><a href="#">Another action</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li role="separator" class="divider"></li>
                    <li class="dropdown-header">Nav header</li>
                    <li><a href="#">Separated link</a></li>
                    <li><a href="#">One more separated link</a></li>
                  </ul>
                </li>
              </ul>
            </div><!--/.nav-collapse -->
          </div>
        </nav>

        <div class="container theme-showcase" role="main">

          <!-- Main jumbotron for a primary marketing message or call to action -->
          <div class="jumbotron">
              <center>
            <h1>'''
        
        html = html + foo + title

        foo = '''</h1>
                    </center>
          </div>



          <div class="page-header">
            <h1>Enlaces</h1>
          </div>
          <div class="row">
              
            <div class="col-sm-12">
              <div class="list-group">'''

        html = html + foo


        for link in links:
            if 'powvideo' in link:
                html = html + '<a href="' + link + '" class="list-group-item"><img border="0" alt="Powvideo" src="http://www.wopelis.com/hosts/powvideo.png" width="100"></a>'
            elif 'flashx' in link:
                html = html + '<a href="' + link + '" class="list-group-item"><img border="0" alt="Powvideo" src="http://www.wopelis.com/hosts/flasht.JPG" width="100"></a>'
            elif 'gamovideo' in link:
                html = html + '<a href="' + link + '" class="list-group-item"><img border="0" alt="Powvideo" src="http://www.wopelis.com/hosts/gamovideo.png" width="100"></a>'

        foo = '''</div>
            </div><!-- /.col-sm-4 -->         


        </div> <!-- /container -->


        <!-- Bootstrap core JavaScript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
        <!-- Latest compiled and minified CSS -->


    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
      </body>
    </html>'''
        html = html + foo
        f = open(title.replace(' ','_') + '.html','w')
        f.write( html )
        f.close()

