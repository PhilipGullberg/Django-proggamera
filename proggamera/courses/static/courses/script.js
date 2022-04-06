$(document).ready(function () {
    
    $("pre").css({
        "font-size": "14px",
        "font-family": "Helvetica",
        "letter-spacing": "2px",
        "border-radius": "5px",
        "filter": "drop-shadow(0 0 0.3rem grey)"
    });
    $("code").css({
        "padding-left": "20px",
        "padding-top": "10px",
        "padding-bottom": "5px",
        "border-radius": "7px",
        "filter": "drop-shadow(0 0 0.3rem grey)"
    });
    $('.content').css({
        "margin-left": "0px"
    });
    $('#sidebarCollapse').on('click', function () {
        console.log("hello")
        $('.content').css({
            "margin-left": "0px"
        });
        $('#sidebar').toggleClass('close');
        $('#sidebar').removeClass('open');
    });
    $('#sidebarOpen').on('click', function () {
        if ($('#sidebar').hasClass('close')) {
            $('.content').css({
                "margin-left": "100px"
            });
            $('#sidebar').toggleClass('open');
            $('#sidebar').removeClass('close');
        } else {
            $('.content').css({
                "margin-left": "0px"
            });
            $('#sidebar').toggleClass('close');
            $('#sidebar').removeClass('open');
        }

    });
    hljs.configure({useBR: true});
    let codetext = document.querySelectorAll('.code-text');
    
    codetext.forEach((el) => {
        el.classList.add("language-python");
        hljs.highlightElement(el);

        
        
    });
    let answer_button=document.querySelector("#input-field");
    if(answer_button!=null){
        answer_button.addEventListener("keyup", function(e){
            if (e.key === 'Enter') {
                var input_value = document.getElementById("fill-in-1").value;
                var answer_value=document.getElementById("answer").value;
                if(input_value==answer_value){
                    let congrats_vid = document.querySelector(".congrats");
                    congrats_vid.style.display="block";
                    let vid = document.querySelector(".player");
                    vid.play();
                    setTimeout(function(){
                        congrats_vid.style.display="none";
                    
                    },1500);
                    
                }
            }
        });
    }
    
    let hint_button=document.querySelector(".fill-in-hint");
    if(hint_button!=null){
        hint_button.addEventListener("click", function(){
            var hint_text = document.querySelector('.hint-text');
            if(hint_text.style.display == "flex"){
                hint_text.style.display = "none";
            }
            else{
                hint_text.style.display = "flex";
            }
            
        });
    }

    let facit_button=document.querySelector(".fill-in-facit");
    if(facit_button!=null){
    facit_button.addEventListener("click", function(){
        var facit_text = document.querySelector('.facit-text');
        if(facit_text.style.display == "flex"){
            facit_text.style.display = "none";
        }
        else{
            facit_text.style.display = "flex";
        }
        
    });
    }
    function youtube_parser(url){
        var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
        var match = url.match(regExp);
        return (match&&match[7].length==11)? match[7] : false;
    }
    var timer = document.querySelector("#timer");
    let timerform = document.querySelector(".timerform");
    let timerformsubmit=document.querySelector("#timerformsubmit");
    var iframen=document.querySelector("iframe");
    iframen.id="videoplayer";
    iframe_videoID=youtube_parser(iframen.src);
    console.log(iframe_videoID);
    var tag = document.createElement('script');
    tag.id = 'iframe-demo';
    tag.src = 'https://www.youtube.com/iframe_api';
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    var player;
    function onYouTubeIframeAPIReady() {
      player = new YT.Player('player', 
      {
        videoId: iframe_videoID,
        height: '350',
        width: '450',
        events: {
          'onReady': onPlayerReady,
          'onStateChange': onPlayerStateChange,
          
        }
      });
    }
    function onPlayerReady(event) {
       
        console.log("Player ready")
    }
    let timewatched=0;
    function onPlayerStateChange(event) {

        if(event.data==1){
            startTime = new Date();

        }
        else if(event.data==2){
            endTime = new Date();
            timed=endTime-startTime;
            timed=timed/1000;
            timewatched= timewatched + Math.round(timed);
            timer.value=timewatched;
            timerformsubmit.click();
        }
    }
   
    onYouTubeIframeAPIReady()
});