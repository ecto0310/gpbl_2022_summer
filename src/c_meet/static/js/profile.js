$(document).ready(function() {
    $("#avatar").click(function() {
        $("input[id='my_file']").click();
    });
    
    var readURL = function(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#avatar').attr('src', e.target.result);
            }
    
            reader.readAsDataURL(input.files[0]);
        }
    }
    

    $("#my_file").on('change', function(){
        readURL(this);
    });

    //doughnut chart
    var ctxD = $("#doughnutChart");
    console.log(ctxD);
    var myLineChart = new Chart(ctxD, {
        type: 'doughnut',
        data: {
        labels: ["Red", "Green", "Yellow", "Grey", "Dark Grey"],
        datasets: [{
            data: [300, 50, 100, 40, 120],
            backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C", "#949FB1", "#4D5360"],
            hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870", "#A8B3C5", "#616774"]
        }]
        },
        options: {
        responsive: true
        }
    });
});
