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
                   // $('<img width="360px" height="2100px" src="' + value.url  +'" /><br />').appendTo($('#mydiv'))
                   $('<img src="' + value.url  +'" /><br />').appendTo($('#mydiv'))
                });
            },
            error: function (xhr, status, error) {
                alert("操作失败：" + error);
            }
        });
    })

    // 下拉框漫画名
    $('#editable-select').editableSelect({ 
        bg_iframe: true,
        case_sensitive: false, 
        items_then_scroll: 10 ,
        isFilter:false
    }); 

    // 下拉框漫画章节
    $('#editable-select-chapter').editableSelect({ 
        bg_iframe: true,
        case_sensitive: false, 
        items_then_scroll: 10 ,
        isFilter:false
    }); 

    // 点击事件
    $('#editable-select-chapter_sele').click(function(){
        if($('#editable-select').val()){
            var url = '/animate/chapter/';
            $.ajax({
                url: url,
                type: "get",
                dataType: 'json',
                data:{animate_id: $('#editable-select').val().trim()},
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
        }else{
            return
        }
    });
})
