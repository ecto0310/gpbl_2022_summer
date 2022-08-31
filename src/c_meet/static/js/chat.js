function reload() {
    $.ajax({
        url: location.href,
        type: "GET",
        dataType: "html",
    }).done(function (data) {
        log = $(data).find('#chat_log');
        console.log(log);
        $('#chat_log').html(log);
    });
}

$(document).ready(function () {
    setInterval(reload, 2000);
});
