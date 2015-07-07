# Duke Delts Website V2

Second version of Duke Delta Tau Delta website, now with Django backend. Project is temporarily located at 
<a href="test.dukedelts.com">test.dukedelts.com</a>


<b>Backend</b>

Website is built on Django backend to allow for users, forms, and news stories. Python-social-auth library is used to allow
brothers to sign in to the brothers-only section of the website. Executive Board members can create news stories on the admin
page with a title, pubdate, and image, to display in the new "News" section.

The main views, urls, and static files are located within the dukedelts app. Backend user configuration is in the core app.
News stories are in the news app.

<b>Frontend</b>

Frontend is done using Twitter Bootstrap and custom html/css/javascript. It was completely redone from scratch from the last
version of the website for a new custom and personalized layout.
