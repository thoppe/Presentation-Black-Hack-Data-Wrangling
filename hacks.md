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

====
## BLACK HAT #3: Cookies/OAuth2
implementation *EASY* : defense *TRIVIAL* : hack-level *NEW HIRE*

====
## BLACK HAT #4: Data limits & time delays
implementation *MEDIUM* : defense *MEDIUM* : hack-level *ENTRY-LEVEL*

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

