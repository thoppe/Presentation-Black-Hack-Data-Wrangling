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

## White-hat data wrangler
Working hard to make your data accessible to others.
!(images/dcdw_logo.jpg) <<height:500px; transparent>>

_But what if you don't want people to have your data...?_
%_and for one reason or another you have to put it out there for all to see...?_

====*

## Black-hat data wrangler
Working hard to make your data as inaccessible as possible.

% Maybe this? http://giphy.com/gifs/evil-aladdin-jafar-8XaceDrB8kYY8

What kind of data?

Corporate finance data.
Dontations.
Regulations (can't track it if you can't see it)
Anti-FOIA
Digital Marketer

====*

## Why not disconnect from the net?
Let's assume there are "laws" that you have to "comply" with...

!(images/drevil2.jpg) <<height:300px>>
!(images/drevil.jpg)  <<height:300px>>
!(images/drevil3.jpg) <<height:300px>>
====*
### Black Hack Data Wrangling Rules:
You have a sizable amount of data.
This data must be made "public".
Make it as computer-unfriendly, but human readable.
Hide what you are doing to a casual user.

% images from
% https://imgflip.com/memegenerator/17089817/Dr-evil-quote
====

% slide explaining the levels...

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

====*

## WHITE HAT #1: Disable right-click
Open developers console (F12), search for `disableclick` and remove.
_or_
Turn of javascript.
_or_
Use any headless browser.
  
====



# Thanks you!