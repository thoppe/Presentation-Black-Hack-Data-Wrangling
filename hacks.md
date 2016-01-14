====

### Table of Contents

#### [Disable right-click](#Hack1) [T]
#### [Minification](#Hack2) [R]
#### [Authentication](#Hack3) [T]
#### [Data limits](#Hack4) [R]
#### [Rendering to images](#Hack5) [R]
#### [JavaScript page links](#Hack6) [T]
#### [Watermarking](#Hack7) [R]
#### [Honeypots & Stenography](#Hack8) [T]
#### [Remove markup metadata](#Hack9) [T]
#### [HTML obfuscation](#Hack10) [R]
#### [Serving HTML as PDF](#Hack11) [R]
#### [Text remapping](#Hack12) [T]

==== [Hack1]

## `BlackHat1`:   Disable right-click
implementation *EASY* : defense *WEAK* : hack-level *SCRIPT-KIDDIE*

    <script language="javascript">
    document.onmousedown=disableclick;
    status="Right Click Disabled";
    function disableclick(event) {
      if(event.button==2) {
         alert(status);
         return false;    
    } }
    </script>

Also in this category, CSS overlays.

====*
<div class="whitehat">
## `WhiteHat1`: Disable right-click </div>

###  Open developers console (F12), search for `disableclick` and remove.

### Turn of javascript.

### Use a headless (or mobile) browser.


==== [Hack2]
## `BlackHat2`: Minification
implementation *EASY* : defense *WEAK* : hack-level *SCRIPT-KIDDIE*

[Kangax HTML Minifier](https://github.com/kangax/html-minifier): removes comments, whitespace, empty elements, and much more. Also minifies javascript and CSS. Ruby wrapper: [html_minifier](https://github.com/stereobooster/html_minifier)
#### INPUT
    <div class="reveal">
        <div class="slides">
            <section class="vertical-stack">
                <section class="vertical-slide">
                    <h1>Black Hat</h1>
                    <h1>Data Wrangling</h1>
                    <hr>
                    <h3><a href="http://thoppe.github.io/">Travis Hoppe</a> /
                    <a href=
                    "http://robertwdempsey.com/about-robert-dempsey/">Robert
                    Dempsey</a></h3><a href=
                    "https://twitter.com/metasemantic">@metasemantic</a> /
                    <a href="https://twitter.com/rdempsey">@rdempsey</a>
                    <br>
                </section>
            </section>
        </div>
    </div>
#### OUTPUT 
    <div class=reveal><div class=slides><section class=vertical-stack><section class=vertical-slide><h1>Black Hat</h1><h1>Data Wrangling</h1><hr><h3><a href="http://thoppe.github.io/">Travis Hoppe</a> / <a href="http://robertwdempsey.com/about-robert-dempsey/">Robert Dempsey</a></h3><a href=https://twitter.com/metasemantic>@metasemantic</a> / <a href=https://twitter.com/rdempsey>@rdempsey</a><p></p><br></section></section></div></div>

====*
<div class="whitehat">
## `WhiteHat2`: Minification </div>
De-minify the HTML using freely available tools.

Online tools: [Unminify](http://unminify.com/), [JS Beautifier]()
_or_
Text editor: [HTML Tidy](https://github.com/welovewordpress/SublimeHtmlTidy) (Sublime Text)
_or_
Automate it: [JS Beautifier](https://github.com/beautify-web/js-beautify)
    $ pip install jsbeautifier
    $ js-beautify file.js

==== [Hack3]
## `BlackHat3`: Authentication
implementation *MEDIUM* : defense *REASONABLE* : hack-level *CORPORATE*

#### not RESTful?
Implement visitor control via `$SESSIONS`. Give every new visitor to the site a unique ID that you control and limit access with. Bonus, restrict user-agent.

#### REST API?
Require all meaningful data requests to go through OAuth2, cumbersome for new-comers and direct control over the data distribution.

====*
<div class="whitehat">
## `WhiteHat3`: Authentication </div>

Create session ID's with headless browsers
_and_
simulate user-agents

Black Hat Warning: Poorly designed session states
(that don't clear and hold large internal variables) can DoS your server!

==== [Hack4]
## `BlackHat4:` Data & time limits
implementation *MEDIUM* : defense *REASONABLE* : hack-level *CORPORATE*

Detection: high download rates or unusual traffic within a given timespan; 
all traffic from a single client or IP address.

Rate limit individual IP addresses or a specific id.
Delay content delivery.
Return HTTP 301, 40x or 50x errors ([full list](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html))

% Mention story about IP blocking from WIKIPEDIA

====*
<div class="whitehat">
## `WhiteHat4`: Data & time limits </div>

Cycle your IP address using [VPN/proxy services](http://robertwdempsey.com/hma) or [TOR](https://www.torproject.org/) (see [TOR spiders](http://thoppe.github.io/tor_spiders/HnC_presentation.html#/)).
_and_
Slow down your scraper: Scrapy [autothrottle](http://doc.scrapy.org/en/latest/topics/autothrottle.html), custom timing code
_and_
Change your user agent: Scrapy [random user agent](https://github.com/cnu/scrapy-random-useragent), [custom Python code](http://stackoverflow.com/questions/24226781/changing-user-agent-in-python-3-for-urrlib-urlopen)

==== [Hack5]
## `BlackHat5`: Rendering to images
implementation *MEDIUM* : defense *STRONG* : hack-level *CORPORATE*

###Text to Image
[PHP Text to Image](https://www.daftlogic.com/projects-text-to-image.htm) / [ImageMagick](http://www.imagemagick.org/script/index.php)
_or_
Draw text onto an HTML5 canvas using [JavaScript](http://jsfiddle.net/JUWrV/) / use the HTML5 [canvasElement.toDataURL](http://stackoverflow.com/questions/27552969/convert-text-to-canvas-image-preserving-formatting) element

====*
<div class="whitehat">
## `WhiteHat5`: Rendering to images </div>

Server or desktop-based OCR software
_or_
Adobe Acrobat: Image -> PDF -> OCR (manual)
_or_
Python: [OCRopus](https://github.com/tmbdev/ocropy)
_or_
[Tesseract Open Source OCR Engine](https://github.com/tesseract-ocr/tesseract)


==== [Hack6]
## `BlackHat6`: JavaScript page links
implementation *MEDIUM* : defense *REASONABLE* : hack-level *CORPORATE*
Infinite pagination/scroll. Ex. [Dribble](https://dribbble.com/) 
!(images/infinite_scroll.gif) <<height:300px>> 

Forces the user to simulate AJAX (stops headless browsers).
_Combine with user sessions and data limits!_

[Psychology in Human-Computer Interaction](http://videolectures.net/chi08_kieras_phc/) by David Kieras
shows this frustrates the user with lack of control.

&& Image from [visualhierarchy](https://visualhierarchy.co/blog/wp-content/uploads/2015/09/infinite_scroll.gif)

====* !(images/infinite-hate.gif)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<font color="black">

&& Image from [Per Vestman@Dribble](https://dribbble.com/shots/2152555-I-Hate-Infinite-Scroll)
</font>

====*
<div class="whitehat">
## `WhiteHat6`: JavaScript page links </div>

Don't emulate a browser, _be_ the browser! Selenium ex.

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Firefox()
    driver.get('http://www.google.com')
    
    q = driver.find_element(By.NAME, 'q')
    q.send_keys('Black Hat Data Wrangling')
    q.submit()


==== [Hack7]
## `BlackHat7`: Watermarking
implementation *EASY* : defense *STRONG* : hack-level *SCRIPT-KIDDIE*

#### Easy mode, simple IP protection
!(images/watermark_examples/shutterstock1.jpg) <<height:300:px;transparent>> Easy to remove.
!(images/watermark_examples/shutterstock2.jpg) <<height:300:px;transparent>> Requires time to remove, not automated.

Can watermark non images too!

====*
<div class="whitehat">
## `WhiteHat7`: Watermarking
</div>

### Simple removal
Crop the picture in any photo editor
_or_
Use the restoration function in [Inpaint](http://www.theinpaint.com/): $20

### More complex removal
"Content Aware Fill" in Photoshop

====*

### Cropping
!(images/watermark_examples/remove-text-photoshop-label.jpg) <<height:300:px;transparent>>
!(images/watermark_examples/remove-text-photoshop-label-crop.jpg) <<height:300:px;transparent>>

### Content Aware Fill in Photoshop
!(images/watermark_examples/remove-watermark-photoshop-cross-overlay.jpg) <<height:300:px;transparent>>
!(images/watermark_examples/remove-watermark-photoshop-cross-overlay-filled.jpg) <<height:300:px;transparent>>


  
==== [Hack8]
## `BlackHat8`: Honeypots & Steganography
implementation *HARD* : defense *RIDICULOUS* : hack-level *HOLLYWOOD*
Steganography: embed data to identify and track IP/credentials.

A legal strong-arm strategy, freely give data but track its distribution.

Useful to determine ToS violations.

Poison the well! Leave fake data buried deep within the dataset.
====*
### Image steganography
Hide data in the EXIF header (obvious place, easy to remove), [ExifTool](http://www.sno.phy.queensu.ca/~phil/exiftool/)
!(images/honeypot_examples/panda.jpg) [Kevin Dooley, Flickr](https://flic.kr/p/9eopJm)

    $ identify -verbose panda.jpg 
    
     Image: panda.jpg
      Format: JPEG (Joint Photographic Experts Group JFIF format)
      ...
      Properties:
        date:create: 2016-01-10T11:58:10-05:00
        exif:ApertureValue: 327680/65536
        exif:ColorSpace: 1
        exif:DateTime: 2009:08:01 08:59:44
        exif:DateTimeOriginal: 2009:07:24 04:17:22
       ...

====*
### Image steganography
Map post-filter md5sum to user data (not resistant to image changes).
Impossible for user to know what is being stored! 

    import numpy as np
    from scipy.ndimage import imread
    from scipy.misc import imsave
    
    jpg = imread("panda.jpg")
    idx = np.random.uniform(size=jpg.shape) < 0.001
    jpg[idx] += np.random.uniform(-2,2, size=idx.sum()).astype(np.uint8)
    jpg[jpg<0] = 0
    jpg[jpg>255] = 255
    imsave("panda_new.jpg", jpg)
    # Test on command line
    # $ md5sum *.jpg
    # bd1a44ba2111eb675e78935d4d5cc186  panda.jpg
    # 672c6dbf03828ea50a70bc81e19bfd69  panda_new.jpg

!(images/honeypot_examples/panda.jpg) 
!(images/honeypot_examples/panda_new.jpg)
====*
### General steganography

Works for any lossy format (mp3, gif, etc...)
For tabular data, hide identification in NULL fields that can be easily removed.
Perturb date-times by seconds in data records and save the offset.

### Honeypots

If a bot or persistent downloader is identified, feed them faulty data.
Continually degrade image quality sent as function of DL's.
Remove rows, or return records not found with increasing frequency.

====*
<div class="whitehat">
## `WhiteHat8`: Honeypots & Steganography </div>

Download data multiple times from different origins.

Run `diff` commands to suss out data that changes by IP and user.

Sanitize data by rejecting fields and entries that change with alternative DLs.

Modify image to remove steganography (apply same trick twice!)


==== [Hack9]
## `BlackHat9`: Remove markup metadata
implementation *HARD* : defense *REASONABLE* : hack-level *CORPORATE*

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

====*
<div class="whitehat">
## `WhiteHat9`: Remove markup</div>

Rare in the wild as this makes web development a nightmare.
_often found when dev's use lazy CMS..._

Removing meta data slows users down, but syntax rules can be written per item:
    html = '''
    <div style="font-weight: bold;">
    Preston Garvey </br>
    Piper Wright
    </div>'''
    
    import bs4
    soup = bs4.BeautifulSoup(html,'lxml')
    text = soup.div.text
    names = text.strip().split('\n')
    
    keys = "firstname", "lastname"
    data = [dict(zip(keys,x.split())) for x in names]
    
    print data
    # [{'lastname': u'Garvey', 'firstname': u'Preston'}, {'lastname': u'Wright', 'firstname': u'Piper'}]

==== [Hack10]
## `BlackHat10`: HTML obfuscation
implementation *EASY* : defense *REASONABLE* : hack-level *SCRIPT-KIDDIE*

Encode everything with HTML character codes and insert random benign HTML.

Start with this:
    This is a string of text
Encode to this:
    &#84;&#104;&#105;&#115;&#32;&#105;&#115;&#32;&#97;<u></u>&#32;&#115;
    <i></i>&#116;&#114;&#105;<u></u>&#110;&#103;<i></i>&#32;<u></u>&#111;&#102;&#32;&#116;&#101;&#120;&#116;
'View Source' shows this:
    <p>&#84;&#104;&#105;&#115;&#32;&#112;&#97;&#103;&#101;
    &#32;&#105;&#115;<i></i>&#32;<u></u>&#109;&#101;&#97;&#110;<b></b>



====*
<div class="whitehat"> 
## `WhiteHat10`: HTML obfuscation </div>

Use the [Selenium Web Driver](http://www.seleniumhq.org/projects/webdriver/)

1. 1. Create a headless web browser
2. 2. Open the page
3. 3. Take a screenshot of the page
4. 4. Use OCR to extract the text from the screenshot
_or_
1. 1. Capture the entire page (curl, etc.)
2. 2. Decode the HTML characters using [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/)


==== [Hack11]
## `BlackHat11`: Serving HTML as PDF 
implementation *HARD* : defense *STRONG* : hack-level *CORPORATE*

###Convert all Text to PDF
Use [PhantomJS](http://phantomjs.org/), [Wkhtmltopdf](http://wkhtmltopdf.org/) or [PDFKit](http://pdfkit.org/) (node.js)

Eschew style conventions and use multi-columns!

====*
<div class="whitehat">  
## `WhiteHat11`: Serving HTML as PDF </div>

Use OCR to extract text and images from the text
_or_
[Tabula](http://tabula.technology/) to extract tabular data

==== [Hack12]
## `BlackHat12`: Text remapping
implementation *WTF* : defense *RIDICULOUS* : hack-level *HOLLYWOOD*

Alter text from visual display:

### Javascript
### Hidden spans
### Font remapping

====*
## Javascript text manipulation

Alter the text as it is copied. JSfiddle [example](http://jsfiddle.net/jp6nhmxf/)

    function addLink() {
        //Get the selected text and append the extra info
        var selection = window.getSelection(),
            pagelink = '<br /><br /> Read more at: ' + document.location.href,
            copytext = selection + pagelink,
            newdiv = document.createElement('div');
    
        //hide the newly created container
        newdiv.style.position = 'absolute';
        newdiv.style.left = '-99999px';
    
        //insert the container, fill it with the extended text, and define the new selection
        document.body.appendChild(newdiv);
        newdiv.innerHTML = copytext;
        selection.selectAllChildren(newdiv);
    
        window.setTimeout(function () {
            document.body.removeChild(newdiv);
        }, 100);
    }
    document.addEventListener('copy', addLink);

====*
## Hidden spans

simple text below right?
## <p class="codeblock">T<span style="position: absolute; left: -5000px; top: -5000px">gCRT3Qg3</span>R<span style="position: absolute; left: -5000px; top: -5000px">T7SQNdsF</span>A<span style="position: absolute; left: -5000px; top: -5000px">TBsh8T3T</span>V<span style="position: absolute; left: -5000px; top: -5000px">WKaKeTMg</span>I<span style="position: absolute; left: -5000px; top: -5000px">ayRwzhur</span>S<span style="position: absolute; left: -5000px; top: -5000px">tNVKkXZV</span></p>
====+
copy and paste transforms 
`TRAVIS` to `TgCRT3Qg3RT7SQNdsFATBsh8T3TVWKaKeTMgIayRwzhurS`
     <p class="codeblock">
       T
       <span style="position: absolute; left: -100px; top: -100px">gCRT3Qg3</span>
       R
       <span style="position: absolute; left: -100px; top: -100px">T7SQNdsF</span>
       A
       <span style="position: absolute; left: -100px; top: -100px">TBsh8T3T</span>
       V
       <span style="position: absolute; left: -100px; top: -100px">WKaKeTMg</span>
       I
       <span style="position: absolute; left: -100px; top: -100px">ayRwzhur</span>
       S
       <span style="position: absolute; left: -100px; top: -100px">tNVKkXZV</span>
     </p>

Any data payload can be inserted here (e.g. copyright claims, point of origin, etc...)
====*
## Font remapping

Render document to PDF and remap fonts _per document_ for protected data.
### Example: [font_remapping.pdf](images/font_remapping.pdf)
====+

  
WTH? How does it work?
> A PDF is a collection of symbols drawn on a page. Draw `c` here, draw `a` there, etc. A PDF reader only knows what a letter is because it maps to a specific character code in the font. Simply create a new font that lies about its mapping.

Multiple fonts can be used to improve the "encryption" process, 
one font per character gives a one-time pad! 

====*
<div class="whitehat">
## `WhiteHat12`: Text remapping </div>

For *Javascript* remapping use a headless browser. For *hidden spans*, learn and write custom rules to remove the offending page elements. For *font remapping*...
====+
<br>
Throw money and humans at it: [Mechanial Turk](https://www.mturk.com/mturk/welcome)
!(images/baby_rain.gif) <<transparent;height:420px>>  
!(images/monkey.gif) <<transparent;height:420px>>  

