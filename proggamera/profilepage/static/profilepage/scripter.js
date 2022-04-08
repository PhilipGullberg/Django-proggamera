$(document).ready( function () {
    

    



    let videoelement=document.querySelectorAll('.video-data');

    for (let i =0; i <videoelement.length; i++){
        if (videoelement[i].childElementCount>1){
            videoelement[i].lastElementChild.remove();
        }
    }
   
    
    let codetext = document.querySelectorAll('.code-text');
    
    codetext.forEach((el) => {
        el.classList.add("language-python");
        hljs.highlightElement(el);

        
        
    });
    
    /* If element has quiz, removes all other childs */
    let hasquizdata = document.querySelectorAll("#hasquiz");
    for(let j=0; j<=hasquizdata.length-1;j++){
        for(let i=0; i<=3; i++){
            let curr_element= hasquizdata[j].nextElementSibling;
            curr_element.remove();
            
        }

    }
    /* If element has fill, removes all other childs */
    let hasfilldata = document.querySelectorAll("#hasfill");
    for(let j=0; j<=hasfilldata.length-1;j++){
        let curr_element= hasfilldata[j].nextElementSibling;
        curr_element.remove();
         
        

    }

    let table=$('.table').DataTable(  
        {
        scrollX:true,
        "order": [[ 0, "asc" ]],

        }
    );
    $('button[data-bs-toggle="tab"]').on( 'shown.bs.tab', function (e) {
        console.log("changed tab")
        $($.fn.dataTable.tables( true ) ).css('width', '100%');
        $($.fn.dataTable.tables( true ) ).DataTable().columns.adjust().draw();
    } );
    const data = {
        labels: [
            'Red',
            'Green',
            'Yellow'
        ],
        datasets: [{
            label: 'My First Dataset',
            data: [20, 150, 100],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'green',
                'rgb(255, 205, 86)'
            ],
            hoverOffset: 4
        }]
    };

    const config = {
        type: 'doughnut',
        data: data,
        options: {}
    };
    const myChart = new Chart(
        document.getElementById('myChart'),
        config
    );
    

});