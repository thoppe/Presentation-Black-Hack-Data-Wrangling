## BLACK HAT #1: Disable right-click
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
Open developers console (F12), search for `disableclick` and remove.
_or_
Turn of javascript.
_or_
Use any headless browser.

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
## BLACK HAT #4: Data limits & time delays
implementation *MEDIUM* : defense *MEDIUM* : hack-level *ENTRY-LEVEL*

Detection: high download rates or unusual traffic within a given timespan; all traffic from a single client or IP address.

Rate limit individual IP addresses or a specific id.
Delay content delivery.
Return HTTP 301, 40x or 50x errors ([full list](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html))


====*

## WHITE HAT #4: Data limits & time delays
Frequently change your IP address using [VPN/proxy services](http://robertwdempsey.com/hma) or [TOR](https://www.torproject.org/).
_and_
Slow down your scraper: Scrapy [autothrottle](http://doc.scrapy.org/en/latest/topics/autothrottle.html), custom timing code
_and_
Change your user agent: Scrapy [random user agent](https://github.com/cnu/scrapy-random-useragent), [custom Python code](http://stackoverflow.com/questions/24226781/changing-user-agent-in-python-3-for-urrlib-urlopen)

====
## BLACK HAT #5: Rendering to images / PDF
implementation *NON TRIVAL* : defense *PRETTY GOOD* : hack-level *JUNIOR-LEVEL*

====
## BLACK HAT #6: JavaScript links to loop through pages
implementation *STANDARD* : defense *MEDIUM* : hack-level *JUNIOR-LEVEL*

====
## BLACK HAT #7: Watermarking & Honeypots
implementation *HARD* : defense *SUBTLE* : hack-level *SECURITY ANALYST*

====
## BLACK HAT #8: Lack of proper HTML/CSS markup 
implementation *XXXX* : defense *XXXX* : hack-level *EXTREME APATHY*

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

