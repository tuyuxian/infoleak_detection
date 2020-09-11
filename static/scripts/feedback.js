jQuery(function ($) {
    $("#push").on("click", function (e) {
        e.preventDefault();
        var uuid = $('#uuid').val();
        var accuracy = $('#accuracy').val();
        var point = $('#point').val();
        var nexttime = $('#nexttime').val();
        var suggestion = $('#suggestion').val();
        var data = {
            'uuid': uuid,
            'accuracy': accuracy,
            'point': point,
            'nexttime': nexttime,
            'suggestion': suggestion,
        }
        send(data);
    });
    function send(data) {
        $.ajax({
            type: 'get',
            url: 'https://script.google.com/macros/s/AKfycbxYPquqCWMTR9ut_jY7zmbAiDljLtJNkAM30Xcb9COzJQjIEPQ/exec',
            data: data,
            dataType: "json",
            success: function (response) {
                console.log(response)
                alert('提交成功！');
            }
        })
    }
});