var root = '/myapp/';

$(function(){
   $("input[name='btn-create-employee']").click(createEmployee);
});

function createEmployee(){

    var data = $("#form-create").serialize();

    $.ajax({
        url: root + 'save',
        type: 'post',
        data: data,
        success: function(result){
            if(result.indexOf('done')>-1) {
                $("#message").html("User created successfully");
                $("input[name='name']").val('');
            }
            else
                $("#message").html("Error creating user");
        }
    });
}