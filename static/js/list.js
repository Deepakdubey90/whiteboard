$(document).ready(function() {
    function setTableContent(data)
    {
	for (var i = 0; i < data.length; i++) {
	    $("#tbDetails").append("<tr><td>" + data[i].vehical_name + "</td><td>" + data[i].vehical_number + "</td><td>" + data[i].vehical_type + "</td><td>" + data[i].vehical_intime +"</td><td>"+ data[i].vehical_outtime +"</td><td>"+ data[i].park_fare + "</td><td><p data-placement='top' data-toggle='tooltip' title='Edit'><a href='/update/vehical/"+ data[i].id +"' class='btn btn-primary btn-xs btnModify' data-id='"+ data[i].id +"'><span class='glyphicon glyphicon-pencil'></span></a></p></td><td><p data-placement='top' data-toggle='tooltip' title='Delete'><button data-id='"+ data[i].id +"' class='btn btn-danger btn-xs btnDelete' data-title='Delete' data-toggle='modal' data-target='#delete'><span class='glyphicon glyphicon-trash'></span></button></p></td></tr>");
	}
    }

    // Load  content document load
    $.ajax({
	type: "GET",
	url: "/vehicals/",
	dataType: 'json',
	success: function(data) {
	    setTableContent(data)
	},
	error: function(jqXHR, status, err){
	    console.log(err)
	}
    });

    $(document).on("click",".btnAdd",function() {
	window.location = 'http://localhost:8000/create/vehical/'
    })
});
