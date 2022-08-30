$(document).ready(function() {
    $("#avatar").click(function() {
        $("input[id='my_file']").click();
    });
    
    var readURL = function(input) {
        if (input.files && input.files[0]) {
            new Promise(function(resolve, reject) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#avatar').attr('src', e.target.result);
                resolve(e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
            reader.onerror = reject;
            })
            .then(processFileContent)
            .catch(function(err) {
            console.log(err)
            });
        }
    }

    function processFileContent(data) {
        var list = data.split('\n');
        $('#image').val(list);
    }
    

    $("#my_file").on('change', function(){
        readURL(this);
    });

    $('#update_button').click(function(){
        $('#user_form').submit();
    });
     
     
    $('#delete_hobby').click(function(){
        $('#hobby_form').attr('action', '/user/me/delete_hobby');
        $('#hobby_form').submit()
    });

    $('.add_new').click(function(e) {
        if ($('#hobby').val()) {
            $('#hobby_form').submit()
        } else {
            alert('趣味を選択してください。')
        }
    })

    //doughnut chart
    var ctxD = $("#doughnutChart");
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
