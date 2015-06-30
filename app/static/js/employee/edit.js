var root = '/myapp/';

$(function(){
   $("input[name='btn-update-employee']").click(updateEmployee);
});

function updateEmployee(){

    var data = $("#form-update").serialize();

    $.ajax({
        url: root + 'update',
        type: 'post',
        data: data,
        success: function(result){
            if(result.indexOf('done')>-1) {
                $("#message").html("User updated successfully");
            }
            else
                $("#message").html("Error updating user");
        }
    });
}