
function login(){


	var username = $('#username').val();
	var pwd = $('#pwd').val();
	var result = {"user_name": username,
				"pwd": pwd};
	$.ajax({
		type: 'GET',
        contentType: 'application/json',
        url: 'http://127.0.0.1:8000/save_logindetails/',
        data: JSON.stringify(result),
        dataType: 'json'

	})

	}