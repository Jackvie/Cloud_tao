$(function () {


    $('#subscribe').click(function () {
        var data = {
            animate_name:$('#editable-select').find('option:selected').text().trim(),
            chapter:$('#editable-select-chapter').find('option:selected').val().trim()
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
                   // $('<img width="360px" height="2100px" src="' + value.url  +'" /><br />').appendTo($('#mydiv'))
                   $('<img src="' + value.url  +'" /><br />').appendTo($('#mydiv'))
                });
            },
            error: function (xhr, status, error) {
                alert("操作失败：" + error);
            }
        });
    });

    // 点击事件
    $('#editable-select').change(function(){
        if($('#editable-select').val()){

            var url = '/animate/chapter/';
            $.ajax({
                url: url,
                type: "get",
                dataType: 'json',
                data:{animate_id: $('#editable-select').find('option:selected').val().trim()},
                async: false,
                success: function (response) {
                    data = response.data;
                    $('#editable-select-chapter').empty();
                    data.forEach(function (value) {
                       $('<option value="'+value.chapter+'">'+value.chapter +'page</option>').appendTo($('#editable-select-chapter'))
                    });
                },
                error: function (xhr, status, error) {
                    alert("操作失败：" + error);
                }
            });
        }else{}
    });
});
