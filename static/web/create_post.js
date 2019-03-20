//////////////Wrapper for to be executed only when page finished loading
document.addEventListener('DOMContentLoaded', () => {

    $(document).on("click","#create_reminder",create_reminder);


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

function create_reminder(){
    //get variables to pass
    title = $('#title').val();
    status = $('#status').val();
    
    //make ajax post request, reload home page when received confirmation
    $.ajax({
        type: "POST",
        url: "/record_reminder",
        dataType: "json",
        data: {"title": title, "status": status},  
        success: function(data) {
            console.log(data.result);
            window.location.pathname = '';
        }
    });

    
};