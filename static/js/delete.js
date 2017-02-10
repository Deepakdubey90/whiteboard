$(document).ready(function() {
    // To open model to confirm delete or cancel.
    $(document).on("click",".btnDelete",function() {
	var id = $(this).data('id');
	var $this = $(this);
	bootbox.confirm("Are you sure want to delete?", function(result) {
	    if (result){
		$.ajax({
		    type: "DELETE",
		    url: '/vehicals/'+id,
		    dataType: 'json',
		    success: function (data, status, jqXHR) {
			//location.reload();
			$this.closest('tr').remove();
		    },
		    error: function (jqXHR, status, err) {
			alert("error !!");
		    }
		});
	    }
	});
    });

});
