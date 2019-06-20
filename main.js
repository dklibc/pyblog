function pyblog_login()
{
	var form = document.getElementById("login_form");

	form.style.display = "inline-block";

	var link = document.getElementById("login_link");

	link.style.display = "none";
}

function pyblog_try_login()
{
	var login = document.getElementById('login');

	var pwd = document.getElementById('pwd');

	var req = new XMLHttpRequest();

	req.open("POST", "/pyblog/auth.py", false)

	req.setRequestHeader("Content-Type","application/x-www-form-urlencoded;charset=utf-8");

	req.send("login=" + login.value + "&pwd=" + pwd.value);

	if (req.status != 200) {
		failed = document.getElementById('login_failed_msg');
		failed.style.display = "inline";
		return;
	}

	document.location.reload(true);
}

function pyblog_logout()
{
	var req = new XMLHttpRequest();

	req.open("GET", "/pyblog/auth.py?logout=1", false)

	req.send();

	document.location.reload(true);
}

function pyblog_send_note()
{
	var note = document.getElementById("note_form");

	var formData = new FormData(note);

	var req = new XMLHttpRequest();

	req.open("POST", "/pyblog/store_note.py", false)

	req.send(formData);
}
