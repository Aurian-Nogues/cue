//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {
   
    $(document).on("click",".status-button",change_status);
    $(document).on("click","#delete-reminder",delete_reminder);

    ////////////////////////////////////////////////////////////////
    //These functions are required to obtain CSRF code and attach it to POST methods
    
            // CSRF code
            function getCookie(name) {
                var cookieValue = null;
                var i = 0;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (i; i < cookies.length; i++) {
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
            var csrftoken = getCookie('csrftoken');
        
            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            $.ajaxSetup({
                crossDomain: false, // obviates need for sameOrigin test
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type)) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            }); 
    /////////////////////////////////////////////////////////////////
});


//changes status of reminder
function change_status(){
    //get current post status and ID, set variable with opposit status
    status = $(this).text();
    id = $(this).val();

    if (status == "Active") {
        new_status = "Disabled"
    } else {
        new_status = "Active"
    };

    //make ajax post request, reload page when received confirmation
    $.ajax({
        type: "POST",
        url: "/change_status",
        dataType: "json",
        data: {"status": new_status, "id": id},
        success: function(data) {
            console.log(data.result);
            location.reload();
        }
    });
}


//delete reminder from database
function delete_reminder(){
    id = $(this).val();
    
    //make ajax post request
    $.ajax({
        type: "POST",
        url: "/delete_reminder",
        dataType: "json",
        data: {"id": id},
        success: function(data) {
            console.log(data.result);
            location.reload();
        }
    });
}
