# Black Hat
# Data Wrangling

----------
### [Travis Hoppe](http://thoppe.github.io/) / [Robert Dempsey](http://robertwdempsey.com/about-robert-dempsey/)
[@metasemantic](https://twitter.com/metasemantic) / [@rdempsey](https://twitter.com/rdempsey)
  
====

# Data Wranglers
## Want your data!
  
!(images/data_ST.gif) <<height:300px>>
!(images/fast_type.gif) <<height:300px>>

## How can you *<strike>stop</strike>* slow them?
 

====*

## Why not disconnect from the net?
Let's assume there are "laws" that you have to "comply" with...
====+
!(images/drevil2.jpg) <<height:300px>>
!(images/drevil.jpg)  <<height:300px>>
!(images/drevil3.jpg) <<height:300px>>
====+
### Black Hack Data Wrangling Rules:
You have a sizable amount of data.
This data must be made "public".
Make it as computer-unfriendly, but human readable.
Hide what you are doing to a casual user.

% images from
% https://imgflip.com/memegenerator/17089817/Dr-evil-quote
====
  
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

## WHITE HAT #1: Disable right-click
Open developers console (F12), search for `disableclick` and remove.
_or_
Turn of javascript.
_or_
Use any headless browser.
  
====



# Thanks you!