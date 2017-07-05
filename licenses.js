$( document ).ready(function() {
    console.log( "ready2!" );

    $.get( "http://0.0.0.0:8000/business/by_district/", function( data ) {
        console.log(data);
        lineGraph(data);
    });

});


function lineGraph(data) {
    console.log('starting');
    var ctx = $("#myChart");

    var myChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}