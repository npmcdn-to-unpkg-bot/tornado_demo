/**
 * Created by zhangmingyang on 2016-05-03.
 */
function getCookie(name) {
        var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return x ? x[1] : undefined;
    }
/**
 * 将JSON转为字符串。
 * @param obj
 */
function json_to_str(obj) {
        return JSON.stringify(obj);
    }
/**
 * 将字符串转为JSON。
 * @param str
 */
function str_to_json(str){
    return JSON.parse(str);
}
/**
 * 分页
 * @param page
 */
function do_page(page) {
    page_index = page;
    GetGrid()
}

/**
中间加载对话窗
*/
function Loading(bool, text) {
    var ajaxbg = top.$("#loading_background,#loading");
    if (!!text) {
        top.$("#loading").css("left", (top.$('body').width() - top.$("#loading").width()) / 2);
        top.$("#loading span").html(text);
    } else {
        top.$("#loading").css("left", (top.$('body').width() - top.$("#loading").width()) / 2);
        top.$("#loading span").html("正在拼了命为您加载…");
    }
    if (bool) {
        ajaxbg.show();
    } else {
        ajaxbg.hide();
    }
}

function get_ajax(url, postData, callBack) {
    $.ajax({
        url: url,
        dataType: 'json',
        data: postData,
        cache: false,
        async: false,
        beforeSend: function () {

        },
        success: function (data) {
            callBack(data);
        },
        error: function (data) {
            alert("error:" + JSON.stringify(data));
            Loading(false);
        }
    })
}


function post_ajax(url, postData, callBack) {
    $.ajax({
        type: 'post',
        url: url,
        dataType: 'json',
        data: postData,
        cache: false,
        async: false,
        beforeSend: function () {
            
        },
        success: function (data) {
            callBack(data);
        },
        error: function (data) {
            alert("error:" + JSON.stringify(data));
            Loading(false);
        }
    })
}


/**
 * checkbox全选，全不选
 */
$("#btn_check_all").click(function() {
        var checkbox = $(".widget-content").find('input:checkbox');
        checkbox.each(function () {
            if (!$(this).checked) {
                $(this).attr("checked", "true");
            }
        });

    })

$("#btn_check_none").click(function() {
    var checkbox = $(".widget-content").find('input:checkbox');

    checkbox.each(function () {
        if ($(this).attr("checked"))
            $(this).removeAttr("checked");
    });
})
// Form Validation
$("#basic_validate").validate({
    rules:{
        ////////// room
        obj__name:{
            required:true,
        },
        ////////// cabinet
        obj__room_id:{
            required:true,
        },
        obj__number:{
            required:true,
        },
        ////////// host
        obj__ip:{
            required:true,
            ip: true
        },
        obj__os_version:{
            required:true,
        },
        obj__room_id:{
            required:true,
        },
        obj__cabinet_id:{
            required:true,
        },
        obj__position:{
            required:true,
            u_position:true
        },
        obj__status:{
            required:true,
        },
        ////////// role
        obj__role_name:{
            required:true,
        },
        ////////// func
        obj__func_name:{
            required:true,
        },
        obj__path:{
            required:true,
        },
        obj__rights:{
            required:true,
        },
        ////////// user
        obj__username:{
            required:true,
        },
        obj__password:{
            required:true,
        },
        obj__email:{
            required:true,
            email: true
        },
        obj__role_id:{
            required:true,
        }

    },
    errorClass: "help-inline",
    errorElement: "span",
    highlight:function(element, errorClass, validClass) {
        $(element).parents('.control-group').addClass('error');
    },
    unhighlight: function(element, errorClass, validClass) {
        $(element).parents('.control-group').removeClass('error');
        $(element).parents('.control-group').addClass('success');
    }
});