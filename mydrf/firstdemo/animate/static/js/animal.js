$(function () {


    // $('#subscribe').click(function () {
    //     var data = {
    //         animate_name:$('#editable-select').find('option:selected').text().trim(),
    //         chapter:$('#editable-select-chapter').find('option:selected').val().trim()
    //     };
    //     var url = '/animate/';
    //     $.ajax({
    //         url: url,
    //         type: "post",
    //         dataType: 'JSON',
    //         data:data,
    //         async: true,
    //         success: function (response) {
    //             data = response.data;
    //             // console.info(data);
    //             $('#mydiv').empty();
    //             data.forEach(function (value) {
    //                console.log(value.url);
    //                // $('<img width="360px" height="2100px" src="' + value.url  +'" /><br />').appendTo($('#mydiv'))
    //                $('<img src="' + value.url  +'" /><br />').appendTo($('#mydiv'))
    //             });
    //         },
    //         error: function (xhr, status, error) {
    //             alert("操作失败：" + error);
    //         }
    //     });
    // });

    $('#subscribe').click(function () {
        // load传递对象时为post 传递字符串时为get 成功时会将请求内容直接加载到元素内 失败时则不会加载内容到元素内
        $('#mydiv').load(
            '/animate/',
            {animate_name:$('#editable-select').find('option:selected').text().trim(),chapter:$('#editable-select-chapter').find('option:selected').val().trim()},
            function(res,status,xhr){
                // res 请求返回内容的字符串 status可能为success或其他 xhr 响应对象 200 OK
                if(status!='success'){
                    alert(res,xhr.status,xhr.statusText);
                }
            }
        )
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
