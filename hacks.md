====

### Table of Contents

#### [Disable right-click](#Hack1) [T, drafted]
#### [Minification](#Hack2) [R, drafted]
#### [Authentication](#Hack3) [T, drafted]
#### [Data Limits](#Hack4) [R, drafted]
#### [Rendering to Images](#Hack5) [R, drafted]
#### [JavaScript page links](#Hack6) [T, drafted]
#### [Watermarking](#Hack7) [R, partially drafted]
#### [Honeypots & Stenography](#Hack8) [T, drafted]
#### [Remove markup metadata](#Hack9) [T, drafted]
#### [HTML obfuscation](#Hack10) [R, drafted]
#### [Serving as PDF](#Hack11) [R]
#### [Font remapping](#Hack12) [T]

==== [Hack1]

## `BlackHat1`:   Disable right-click
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

% mention CSS overlays?

====*
<div class="whitehat">
## `WhiteHat1`: Disable right-click

###  Open developers console (F12), search for `disableclick` and remove.

### Turn of javascript.

### Use a headless (or mobile) browser.
</div>

==== [Hack2]
## `BlackHat2`: Minification
implementation *EASY* : defense *TRIVIAL* : hack-level *AMATEUR*

[Kangax HTML Minifier](https://github.com/kangax/html-minifier): removes comments, whitespace, empty elements, and much more. Also minifies javascript and CSS.

Ruby wrapper: [html_minifier](https://github.com/stereobooster/html_minifier)


====*

## `WhiteHat2`: Minification
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
implementation *EASY* : defense *MEDIUM* : hack-level *NEW HIRE*

#### not RESTful?
Implement vistor control via `$SESSONS`. Give every new visitor to the site a unique ID that you control and limit access with. Bonus, restrict user-agent.

#### REST API?
Require all meaningful data requests to go through OAuth2, cumbersome for new-comers and direct control over the data distribution.

====*
## `WhiteHat3`: Authentication

Create session ID's with headless browsers
_and_
simulate user-agents

Poorly designed session states (that don't clear and hold
large internal variables) can DoS your server!

==== [Hack4]
## `BlackHat4:` Data & time limits
implementation *MEDIUM* : defense *MEDIUM* : hack-level *ENTRY-LEVEL*

Detection: high download rates or unusual traffic within a given timespan; 
all traffic from a single client or IP address.

Rate limit individual IP addresses or a specific id.
Delay content delivery.
Return HTTP 301, 40x or 50x errors ([full list](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html))

% Mention story about IP blocking from WIKIPEDIA

====*

## `WhiteHat4`: Data & time limits

Frequently change your IP address using [VPN/proxy services](http://robertwdempsey.com/hma) or [TOR](https://www.torproject.org/).
_and_
Slow down your scraper: Scrapy [autothrottle](http://doc.scrapy.org/en/latest/topics/autothrottle.html), custom timing code
_and_
Change your user agent: Scrapy [random user agent](https://github.com/cnu/scrapy-random-useragent), [custom Python code](http://stackoverflow.com/questions/24226781/changing-user-agent-in-python-3-for-urrlib-urlopen)

==== [Hack5]
## `BlackHat5`: Rendering to images
implementation *NON TRIVAL* : defense *PRETTY GOOD* : hack-level *JUNIOR-LEVEL*

###Text to Image
[PHP Text to Image](https://www.daftlogic.com/projects-text-to-image.htm) / [ImageMagick](http://www.imagemagick.org/script/index.php)
_or_
Draw text onto an HTML5 canvas using [JavaScript](http://jsfiddle.net/JUWrV/) / use the HTML5 [canvasElement.toDataURL](http://stackoverflow.com/questions/27552969/convert-text-to-canvas-image-preserving-formatting) element

====*

## `WhiteHat5`: Rendering to images

Server or desktop-based OCR software
_or_
Adobe Acrobat: Image -> PDF -> OCR (manual)
_or_
Python: [OCRopus](https://github.com/tmbdev/ocropy)
_or_
[Tesseract Open Source OCR Engine](https://github.com/tesseract-ocr/tesseract)


==== [Hack6]
## `BlackHat6`: JavaScript page links
implementation *STANDARD* : defense *MEDIUM* : hack-level *JUNIOR-LEVEL*
Infinite pagnation/scroll. Ex. [Dribble](https://dribbble.com/) 
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

## `WhiteHat6`: JavaScript page links

Stateful browser can slowly pull the data like a real user.

SHOW EXAMPLE:

==== [Hack7]
## `BlackHat7`: Watermarking
implementation *EASY* : defense *ROBUST* : hack-level *SCRIPT-KIDDIE*

#### Easy mode, simple IP protection
!(images/watermark_examples/shutterstock1.jpg) <<height:300:px;transparent>> Easy to remove.
!(images/watermark_examples/shutterstock2.jpg) <<height:300:px;transparent>> Requires time to remove, not automated.

Can watermark non images too! SHOW EXAMPLE.

==== [Hack8]
## `BlackHat8`: Honeypots & Stenography
implementation *NON TRIVIAL* : defense *SUBTLE* : hack-level *COVERT-OPS*
Steganography: embed data to identify and track IP/credentials.

A legal strong-arm strategy, freely give data but track its distribution.

Useful to determine ToS violations!

Poison the well! Leave fake data buried deep within the dataset!
====*
### Image stenography
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
### Image stenography
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
### General stenography

Works for any lossy format (mp3, gif, etc...)
For tabular data, hide identification in NULL fields that can be easily removed.
Perturb date-times by seconds in data records and save the offset.

### Honeypots

If a bot or persistant downloader is idenified, feed them faulty data... ex.
Continually degrade image quality sent as function of DL's
Remove rows, or return records not found with increasing frequency.

====*
## `WhiteHat9`: Honeypots & Stenography

Download data multiple times from different sources.

Run `diff` commands to suss out data that changes by IP and user.

Sanitize data by rejecting fields and entries that change with alternative DLs.

Modify image to remove stenography (apply same trick twice!)


==== [Hack9]
## `BlackHat9`: Remove markup metadata
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

==== [Hack10]
## `BlackHat10`: HTML obfuscation
implementation *EASY* : defense *SANITY-REDUCING* : hack-level *SCRIPT-KIDDIE*

Encode everything with HTML character codes and insert random benign HTML.

Start with this:

    This is a string of text

Encode to this:

    &#84;&#104;&#105;&#115;&#32;&#105;&#115;&#32;&#97;<u></u>&#32;&#115;<i></i>&#116;&#114;&#105;<u></u>&#110;&#103;<i></i>&#32;<u></u>&#111;&#102;&#32;&#116;&#101;&#120;&#116;

'View Source' shows this:
    <p>
    &#84;&#104;&#105;&#115;&#32;&#112;&#97;&#103;&#101;&#32;&#105;&#115;<i></i>&#32;<u></u>&#109;&#101;&#97;&#110;<b></b>



====*
## `WhiteHat10`: HTML obfuscation

Use the [Selenium Web Driver](http://www.seleniumhq.org/projects/webdriver/)
* Create a headless web browser
* Open the page
* Use OCR to extract the text

_or_

* Capture the entire page (curl, etc.)
* Decode the HTML characters using [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/)


==== [Hack11]
## `BlackHat11`: Serving as PDF 
implementation *XXXX* : defense *EXECELLENT* : hack-level *XXXX*

###Text to PDF
[PhantomJS](http://phantomjs.org/), [Wkhtmltopdf](http://wkhtmltopdf.org/) or [PDFKit](http://pdfkit.org/)  (node.js)


==== [Hack12]
## `BlackHat12`: Font remapping
implementation *WTF* : defense *RIDICULOUS* : hack-level *MITNICK*
