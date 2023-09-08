
// $(document).ready(function(){
//     function getCSRFToken() {
//         return $('input[name="csrfmiddlewaretoken"]').val();
//     }
//     console.log("ready");
//     $(".delete-button").click(function(){
//         console.log("button")
//         var deleteUrl = $(this).data("delete-url");
//         var userId = deleteUrl.split('/').slice(-2, -1)[0];
//         console.log(userId)

//         $.ajax({
//             type: "POST",
//             headers:{
//                 "X-CSRFToken":getCSRFToken()
//             },
//             url: deleteUrl,
            
//             success:function(response){
//                 console.log(response);
//                 $("#user-" + userId).remove();
//             },
//             error: function (xhr, status, error) {
//                 console.error(xhr.responseText);
//             }
//         });
//     })
// })

