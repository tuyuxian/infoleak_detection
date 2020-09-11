jQuery(function ($) {
    $("#detect").on("click", function (e) {
        e.preventDefault();
        var textVal = $('#text-to-detect').val();
        if (textVal.trim() == "") {
            alert("請輸入條款內容！")
        } else {
            var textRequest = { 'text': textVal };
            if (textRequest !== "") {
                $.ajax({
                    url: '/detect',
                    method: 'POST',
                    header: {
                        Accept: 'application/json; charset=UTF-8'
                    },
                    contentType: 'application/json; charset=UTF-8',
                    dataType: 'json',
                    data: JSON.stringify(textRequest),
                    success: function (response) {
                        $('#detect-result').val(response.text);
                        $('#uuid').val(response.uuid);
                        $('#feedback').show();
                        $('#detect').hide();
                    },
                    beforeSend: function () {
                        $('#loadingIMG').show();
                    },
                    complete: function () {
                        $('#loadingIMG').hide();
                    }
                });
            }
        }
    });
    $("#feedback").on("click", function (e) {
        e.preventDefault();
        $('#div1').hide();
        $('#div2').show();
    });
});
