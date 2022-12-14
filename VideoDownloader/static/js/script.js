websites = document.querySelectorAll('label');
chosen_website = document.getElementById('chosen_website');
url_input = document.querySelector('input[type=text]');
download_button = document.getElementById('download_button');

yt = websites[0];
yt.addEventListener('click', function(){
    url_input.placeholder = 'URL: https://www.youtube.com/watch? ...';
    chosen_website.src = 'static/img/ytcomplete.png';
    download_button.className = 'btn yt';
})

ig = websites[1];
ig.addEventListener('click', function(){
    url_input.placeholder = 'URL: https://www.instagram.com/watch? ...';
    chosen_website.src = "static/img/igcomplete.png";
    download_button.className = 'btn ig';
})

tw = websites[2];
tw.addEventListener('click', function(){
    url_input.placeholder = 'URL: https://www.twitter.com/watch? ...';
    chosen_website.src = 'static/img/twcomplete.png';
    download_button.className = 'btn tw';
})

pin = websites[3];
pin.addEventListener('click', function(){
    url_input.placeholder = 'URL: https://www.pinterest.com/watch? ...';
    chosen_website.src = 'static/img/pincomplete.png';
    download_button.className = 'btn pin';
})

rd = websites[4];
rd.addEventListener('click', function(){
    url_input.placeholder = 'URL: https://www.reddit.com/watch? ...';
    chosen_website.src = 'static/img/rdcomplete.png';
    download_button.className = 'btn rd';
})