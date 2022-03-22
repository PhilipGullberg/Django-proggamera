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
    let answer_button=document.querySelector(".fill-in-answer");
    answer_button.addEventListener("click", function(){
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
    });
    let hint_button=document.querySelector(".fill-in-hint");
    hint_button.addEventListener("click", function(){
        var hint_text = document.querySelector('.hint-text');
        if(hint_text.style.display == "flex"){
            hint_text.style.display = "none";
        }
        else{
            hint_text.style.display = "flex";
        }
        
    });

    let facit_button=document.querySelector(".fill-in-facit");
    facit_button.addEventListener("click", function(){
        var facit_text = document.querySelector('.facit-text');
        if(facit_text.style.display == "flex"){
            facit_text.style.display = "none";
        }
        else{
            facit_text.style.display = "flex";
        }
        
    });
    

    
});