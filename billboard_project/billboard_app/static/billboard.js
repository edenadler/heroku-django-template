var Billboard = {};

Billboard.elemID = 0;
Billboard.comment = "";

Billboard.start = function(){
    $(document).ready(function () {
        $("#blank-form").hide();
        $(".form-container").hide();
        Billboard.activateListeners();
    });
};

Billboard.activateListeners = function(){
    $("#add-btn").bind("click", Billboard.showForm);
    $(".comment").bind("click",Billboard.showCommentForm);
};

Billboard.showCommentForm = function(){
    Billboard.elemId = $(this).attr("id")
    $(".comment_"+Billboard.elemId).collapse('toggle');
    $(".fa-paper-plane").click(function(){
        $(".comment_"+Billboard.elemId).collapse('hide');
        Billboard.comment = $("#comment-box_"+Billboard.elemId).val();
        Billboard.submitComment();
    })
};

Billboard.submitComment = function(){
    console.log("Here")
      function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');


    $.post("/comment",
        {"csrfmiddlewaretoken" : csrftoken,
            "comment": Billboard.comment,
            "id": Billboard.elemId},
            function(data, xhr, settings) {
                console.log(data);
                $(".previous-comments_"+Billboard.elemId).append(data)
            })
};


Billboard.showForm = function(){
    $(".no-msg-container").hide();
    $("#blank-form").show();
    $(".form-container").show();
    $(".add-post-container").hide();
    $("#check-btn").bind("click", Billboard.storeInfoInDB);
    $("#close-btn").bind("click", Billboard.closeForm);

};

Billboard.closeForm = function(){
    console.log("removeform");
    location.reload();
};

Billboard.storeInfoInDB = function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');

    $(".form-container").hide();
    $("#blank-form").hide();
    $(".add-post-container").show();


    $.post("/store",
        {"csrfmiddlewaretoken" : csrftoken,
            "title": $("#titleInput").val(),
            "text": $(".text-area").val(),
            "author": $("#authorInput").val()},
            function(data, xhr, settings) {
                console.log(data);
                $(".posts").append(data)
            })
};


Billboard.start();

