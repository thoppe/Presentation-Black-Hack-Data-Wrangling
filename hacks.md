## BLACK HAT #1:
## Disable right-click
implementation *EASY* : defense *TRIVIAL* : hack-level *AMATEUR*

    <script language="javascript">
    document.onmousedown=disableclick;
    status="Right Click Disabled";
    function disableclick(event) {
      if(event.button==2) {
         alert(status);
         return false;    
    } }
    </script>

====*

## WHITE HAT #1: Disable right-click

###  Open developers console (F12), search for `disableclick` and remove.

### Turn of javascript.

### Use any headless browser.

====
## BLACK HAT #2: Minification
implementation *EASY* : defense *TRIVIAL* : hack-level *AMATEUR*

[Kangax HTML Minifier](https://github.com/kangax/html-minifier): removes comments, whitespace, empty elements, and much more. Also minifies javascript and CSS.

Ruby wrapper: [html_minifier](https://github.com/stereobooster/html_minifier)


====*

## WHITE HAT #2: Minification
De-minify the HTML using freely available tools.

Online tools: [Unminify](http://unminify.com/), [JS Beautifier]()
_or_
Text editor: [HTML Tidy](https://github.com/welovewordpress/SublimeHtmlTidy) (Sublime Text)
_or_
Automate it: [JS Beautifier](https://github.com/beautify-web/js-beautify)
    $ pip install jsbeautifier
    $ js-beautify file.js

====
## BLACK HAT #3: Cookies/OAuth2
implementation *EASY* : defense *TRIVIAL* : hack-level *NEW HIRE*

====
## BLACK HAT #4:
## Data limits & time delays
implementation *MEDIUM* : defense *MEDIUM* : hack-level *ENTRY-LEVEL*

Detection: high download rates or unusual traffic within a given timespan; all traffic from a single client or IP address.

Rate limit individual IP addresses or a specific id.
Delay content delivery.
Return HTTP 301, 40x or 50x errors ([full list](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html))


====*

## WHITE HAT #4:
## Data limits & time delays
Frequently change your IP address using [VPN/proxy services](http://robertwdempsey.com/hma) or [TOR](https://www.torproject.org/).
_and_
Slow down your scraper: Scrapy [autothrottle](http://doc.scrapy.org/en/latest/topics/autothrottle.html), custom timing code
_and_
Change your user agent: Scrapy [random user agent](https://github.com/cnu/scrapy-random-useragent), [custom Python code](http://stackoverflow.com/questions/24226781/changing-user-agent-in-python-3-for-urrlib-urlopen)

====
## BLACK HAT #5:
## Rendering to images / PDF
implementation *NON TRIVAL* : defense *PRETTY GOOD* : hack-level *JUNIOR-LEVEL*

###Text to Image
[PHP Text to Image](https://www.daftlogic.com/projects-text-to-image.htm) / [ImageMagick](http://www.imagemagick.org/script/index.php)
_or_
Draw text onto an HTML5 canvas using [JavaScript](http://jsfiddle.net/JUWrV/) / use the HTML5 [canvasElement.toDataURL](http://stackoverflow.com/questions/27552969/convert-text-to-canvas-image-preserving-formatting) element

###Text to PDF
[PhantomJS](http://phantomjs.org/), [Wkhtmltopdf](http://wkhtmltopdf.org/) or [PDFKit](http://pdfkit.org/)  (node.js)

====*

## WHITE HAT #5
## Rending to images / PDF

Server or desktop-based OCR software
_or_
Adobe Acrobat: Image -> PDF -> OCR (manual)
_or_
Python: [OCRopus](https://github.com/tmbdev/ocropy)
_or_
[Tesseract Open Source OCR Engine](https://github.com/tesseract-ocr/tesseract)


====
## BLACK HAT #6:
## JavaScript page links
implementation *STANDARD* : defense *MEDIUM* : hack-level *JUNIOR-LEVEL*


====*

## WHITE HAT #6:
## JavaScript page links

====
## BLACK HAT #7:
## Watermarking & Honeypots
implementation *HARD* : defense *SUBTLE* : hack-level *SECURITY ANALYST*

====
## BLACK HAT #8:
## Remove markup metadata
implementation *XXXX* : defense *XXXX* : hack-level *MASOCHIST*

### Two ways:
#### 1. Break the standard UX design.
#### 2. Remove proper HTML/CSS markup.

Organized webpage = Organized data = Easy rip
  
====*

Eschew all user design and layer components dynamically.
Example: [http://arngren.net/](http://arngren.net/)
!(images/badUX_arngren.png)
  
====*

Remove markup. You can't rip what you can't see.

    <div class="author">
        <div class="firstname">Preston </div>
        <div class="lastname"> Garvey  </div>
    <div>
    
    <div class="author">
        <div class="firstname">Piper </div> 
        <div class="lastname"> Wright  </div>
    <div>
  
    <!-- Remove all class and id labels, like this --> 
    <div style="font-weight: bold;">
    Preston Garvey </br>
    Piper Wright
    </div>

====
## BLACK HAT #9: IP limits
implementation *EASY TO MESS UP* : defense *MEDIUM* : hack-level *XXXX*

====
## BLACK HAT #10: HTML obfuscation
implementation *XXXX* : defense *XXXX* : hack-level *COMPU-JOCK*

====
## BLACK HAT #11: Random naming conventions for page elements 
implementation *SANITY-REDUCING* : defense *EXECELLENT* : hack-level *CTHULHU*

====
## BLACK HAT #12: Font remapping
implementation *WTF* : defense *RIDICULOUS* : hack-level *MITNICK*

