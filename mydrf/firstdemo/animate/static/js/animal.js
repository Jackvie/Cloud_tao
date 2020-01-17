$(function () {


    $('#subscribe').click(function () {
        var data = {
            animate_name:$('#animate_name').val(),
            chapter:$('#chapter').val()
        };
        var url = '/animate/';
        $.ajax({
            url: url,
            type: "post",
            dataType: 'JSON',
            data:data,
            async: true,
            success: function (response) {
                data = response.data;
                // console.info(data);
                $('#mydiv').empty();
                data.forEach(function (value) {
                   console.log(value.url);
                   $('<img src="' + value.url  +'" /><br />').appendTo($('#mydiv'))
                });
            },
            error: function (xhr, status, error) {
                alert("操作失败：" + error);
            }
        });
    })


})
