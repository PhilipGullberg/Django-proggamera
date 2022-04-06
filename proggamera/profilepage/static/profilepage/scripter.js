$(document).ready( function () {
    
   
    
    let codetext = document.querySelectorAll('.code-text');
    
    codetext.forEach((el) => {
        el.classList.add("language-python");
        hljs.highlightElement(el);

        
        
    });
    
    let hasfilldata = document.querySelectorAll("#hasquiz");
    for(let j=0; j<=hasfilldata.length-1;j++){
        for(let i=0; i<=3; i++){
            let curr_element= hasfilldata[j].nextElementSibling;
            console.log(curr_element);
            curr_element.remove();
            
        }

    }
    let hasscriptdata = document.querySelectorAll("#hasfill");
    for(let j=0; j<=hasscriptdata.length-1;j++){
        let curr_element= hasscriptdata[j].nextElementSibling;
        curr_element.remove();
         
        

    }

    let table=$('.table').DataTable(  
        {
        scrollX:true,
        "order": [[ 0, "asc" ]],
        "autoWidth": false,
    }
    );
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